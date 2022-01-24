# view importation
from view.TournamentView import TournamentView
from view.error import ErrorMessage
from view.PlayerView import View
# model importation
from model.TournamentModel import TournamentModel
from model.RoundModel import RoundModel
from model.PlayerModel import Player
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
        self.tournament_id = TournamentModel(**tournament).get_tournament_id()
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
        self.player_list = self.get_player_list()
        time = self.time_selection()
        description = self.get_tournament_description()
        date = None
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
                self.print_all_tournament()
            elif user_entry == 4:
                self.tournament_finished_to_find()
            elif user_entry == 5:
                break
            else:
                self.message.error_menu()

    @staticmethod
    def print_all_tournament():
        tournaments = TournamentModel.extract_all_tournament()
        TournamentView.print_tournament(tournaments)

    def round_menu(self):
        while True:
            TournamentView.round_menu_view()
            user_choice = InputUtils().check_numbers()
            if user_choice == 1:
                self.round_generation()
            elif user_choice == 2:
                self.set_player_score()
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
                round = RoundModel().generate_round(self.player_list, round_name)
                self.round.append(round)
                self.tournament.get("round_list").append(round)
                self.tournament.update({"date": RoundModel.actual_date()})
                TournamentModel.update_to_db(self.tournament, self.tournament_id)
            elif self.tournament.get("round_list"):
                round_list = self.tournament.get("round_list")
                last_round = round_list[-1]
                if last_round.get("end_date"):
                    i = len(self.tournament.get("round_list")) + 1
                    round_name = f"round {i}"
                    all_round = RoundModel().get_all_round(round_list)
                    match_list = all_round.get("match_list")
                    player_list = RoundModel().get_all_player(match_list)
                    new_round = RoundModel().generate_other_round(player_list, round_name)
                    round_list.append(new_round)
                    TournamentModel.update_to_db(self.tournament, self.tournament_id)
                else:
                    ErrorMessage.player_score_not_set()
        else:
            ErrorMessage.all_round_generated()

    def set_player_score(self):
        is_finished = self.tournament.get("finished")
        if not is_finished == "true":
            list_of_round = self.tournament.get("round_list")
            actual_round = list_of_round[-1]
            if not actual_round.get("end_date"):
                match_list = actual_round.get("match_list")
                for match in match_list:
                    RoundModel().set_player_score(match)
                date = RoundModel().actual_date()
                actual_round.update({"end_date": date})
                if actual_round.get("name") == "round 4":
                    self.tournament.update({"finished": "true"})
                TournamentModel.update_to_db(self.tournament, self.tournament_id)
            else:
                ErrorMessage().round_not_generated()
        else:
            self.view.finished()

    def tournament_finished_to_find(self):
        self.view.tournament_name()
        name = self.utils.check_string()
        self.view.tournament_location()
        location = self.utils.check_string()
        tournament_info = {"name": name, "location": location}
        tournament_to_search = TournamentModel(**tournament_info)
        try:
            tournament_exist = tournament_to_search.search_to_db_for_finished()
            if not tournament_exist:
                self.view.tournament_not_exist()
            else:
                restored_tournament = TournamentModel(**tournament_exist)
                self.tournament = TournamentModel.serialize(restored_tournament)
                self.tournament_id = TournamentModel(**tournament_exist).get_tournament_id()
                self.generate_report()
        except ValueError:
            self.message.generic_error()

    def generate_report(self):
        while True:
            self.view.report_menu()
            user_choice = InputUtils().check_numbers()
            if user_choice == 1:
                player_to_retrieve = self.tournament.get("player")
                list_of_players = []
                for players in player_to_retrieve:
                    list_of_players.append(Player.get_player(players))
                sorted_players = sorted(list_of_players, key=lambda ele: ele["ranking"], reverse=True)
                View.print_player(sorted_players)
            elif user_choice == 2:
                player_to_retrieve = self.tournament.get("player")
                list_of_players = []
                for players in player_to_retrieve:
                    list_of_players.append(Player.get_player(players))
                sorted_players = sorted(list_of_players, key=lambda ele: ele["name"])
                View.print_player(sorted_players)
            elif user_choice == 3:
                list_of_all_round = self.tournament.get("round_list")
                for round in list_of_all_round:
                    self.view.print_round_and_match(round)
            elif user_choice == 4:
                break
            else:
                ErrorMessage.generic_error()
