from view.PlayerView import View
from model.PlayerModel import Player
from utils.utils import InputUtils
from view.error import ErrorMessage


class PlayerController:
    def __init__(self):
        self.view = View()
        self.utils = InputUtils()
        self.message = ErrorMessage()

    def main_controller(self):
        while True:
            self.view.get_menu()
            user_entry = self.utils.check_numbers()
            if user_entry == 1:
                self.player_creation()
            elif user_entry == 2:
                list_of_player = Player.get_all_player()
                sorted_player = sorted(list_of_player, key=lambda ele: ele["ranking"], reverse=True)
                View.print_player(sorted_player)
            elif user_entry == 3:
                list_of_player = Player.get_all_player()
                sorted_player = sorted(list_of_player, key=lambda ele: ele["name"])
                View.print_player(sorted_player)
            elif user_entry == 4:
                player = self.search_player_from_db()
                View.new_player_rank()
                new_rank = self.utils.check_multiple_number()
                if Player.update_player_rank(player, new_rank):
                    View.new_rank_set()
                else:
                    ErrorMessage.generic_error()
            elif user_entry == 5:
                break
            else:
                self.message.error_menu()

    def player_data_retrieval(self):
        self.view.f_name()
        f_name = self.utils.check_string()
        self.view.l_name()
        l_name = self.utils.check_string()
        self.view.sex()
        sex = self.utils.check_sex()
        self.view.borne_date()
        born_date = self.utils.check_date()
        self.view.rank()
        rank = self.utils.check_multiple_number()
        return {"f_name": f_name, "l_name": l_name, "sex": sex,
                "b_date": born_date, "rank": rank}

    def player_creation(self):
        player = self.player_data_retrieval()
        player_data = Player(**player)
        save_completed = player_data.save_to_db()
        if save_completed:
            self.view.creation_confirmation()
            self.main_controller()
        else:
            self.message.data_base_save_error()

    def search_player_from_db(self):
        while True:
            View().f_name()
            name = self.utils.check_string()
            View().l_name()
            l_name = self.utils.check_string()
            View().borne_date()
            b_date = self.utils.check_date()
            player_info = {"f_name": name, "l_name": l_name, "b_date": b_date}
            player_to_search = Player(**player_info)
            try:
                player_exist = player_to_search.search_to_db()
                if not player_exist:
                    self.message.player_not_found()
                else:
                    return player_exist
            except ValueError:
                self.message.generic_error()
