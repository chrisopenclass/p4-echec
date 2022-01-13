# view importation
from view.TournamentView import TournamentView
from view.error import ErrorMessage
# model importation
from model.TournamentModel import TournamentModel
from model.RoundModel import RoundModel
# controller importation
from controller.PlayerController import PlayerController
# custom utils importation
from utils.utils import InputUtils
# python module importation
import datetime


class TournamentController:
    def __init__(self):
        self.view = TournamentView()
        self.utils = InputUtils()
        self.message = ErrorMessage()
        self.player_list = []
        self.round = []
        self.tournament_id = None
        self.tournament = None

    def tournament_creation(self):
        tournament = self.tournament_data_retrieval()
        tournament_data = TournamentModel(**tournament)
        tournament_data.save_to_db()
        tournament = TournamentModel.serialize(tournament_data)
        return tournament

    def get_player_list(self):
        index = 0
        self.player_list = []
        while index < 8:
            player_id = PlayerController().search_player_from_db()
            self.player_list.append(player_id)
            index += 1
        return self.player_list

    def time_selection(self):
        self.view.time_choice_view()
        while True:
            user_entry = self.utils.check_numbers()
            if user_entry == 1:
                return "bullet"
            elif user_entry == 2:
                return "blitz"
            elif user_entry == 3:
                return "quick stroke"
            else:
                self.message.error_menu()

    def get_tournament_description(self):
        self.view.ask_for_description()
        user_input = self.utils.check_description()
        return user_input

    def tournament_data_retrieval(self):
        self.view.tournament_name()
        name = self.utils.check_string()
        self.view.tournament_location()
        location = self.utils.check_string()
        self.player_list = [1, 2, 3, 4, 5, 6, 7, 8]#self.get_player_list()
        time = self.time_selection()
        description = self.get_tournament_description()
        date = datetime.datetime.now().strftime("%d/%m/%Y")
        return {"name": name, "location": location, "player": self.player_list, "time": time,
                "description": description, "date": date, "round_list": self.round}

    def tournament_restoration(self):
        self.view.tournament_name()
        name = self.utils.check_string()
        self.view.tournament_location()
        location = self.utils.check_string()
        tournament_info = {"name": name, "location": location}
        tournament_to_search = TournamentModel(**tournament_info)
        try:
            tournament_exist = tournament_to_search.search_to_db()
            if not tournament_exist:
                self.view.tournament_not_exist()
            else:
                restored_tournament = TournamentModel(**tournament_exist)
                self.tournament = TournamentModel.serialize(restored_tournament)
                self.tournament_id = TournamentModel(**tournament_exist).get_tournament_id()
                self.round_menu()
        except ValueError:
            self.message.generic_error()

    def tournament_menu(self):
        while True:
            self.view.main_menu()
            user_entry = self.utils.check_numbers()
            if user_entry == 1:
                self.tournament = self.tournament_creation()
                while True:
                    self.view.start_now()
                    user_entry = self.utils.check_numbers()
                    if user_entry == 1:
                        self.round_menu()
                    elif user_entry == 2:
                        break
                    else:
                        self.message.error_menu()
            elif user_entry == 2:
                self.tournament_restoration()
            elif user_entry == 3:
                break
            else:
                self.message.error_menu()

    def round_menu(self):
        TournamentView.round_menu_view()
        user_choice = InputUtils().check_numbers()
        while True:
            if user_choice == 1:
                self.round_generation()
            elif user_choice == 2:
                self.set_player_score()
                break
            elif user_choice == 3:
                break
            else:
                ErrorMessage.generic_error()

    def round_generation(self):
        if len(self.tournament.get("round_list")) < 4:
            i = 1
            if not self.tournament.get("round_list"):
                round_name = f"round {i}"
                self.player_list = self.tournament.get("player")
                self.round.append(RoundModel().generate_round(self.player_list, round_name))
                self.tournament.get("round_list").append(self.round)
                TournamentModel.update_to_db(self.tournament, self.tournament_id)
            elif self.tournament.get("round_list"):
                round_name = len(self.tournament.get("round_list")) + 1
                round_list = self.tournament.get("round_list")
                all_round = RoundModel().get_all_round(round_list)
                match_list = all_round.get("match_list")
                player_list = RoundModel().get_all_player(match_list)
                RoundModel().generate_other_round(round_name, player_list)
                print(player_list)
            else:
                ErrorMessage.player_score_not_set()

        else:
            ErrorMessage.all_round_generated()

    def set_player_score(self):
        list_of_round = self.tournament.get("round_list")
        actual_round = RoundModel().select_actual_round(list_of_round)
        if actual_round:
            match_list = actual_round.get("match_list")
            for match in match_list:
                RoundModel().set_player_score(match)
            date = RoundModel().actual_date()
            actual_round.update({"end_date": date})
            TournamentModel.update_to_db(self.tournament, self.tournament_id)
        else:
            ErrorMessage().round_not_generated()
