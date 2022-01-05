from view.MainView import MainView
from utils.utils import InputUtils
from controller.TournamentController import TournamentController
from controller.PlayerController import PlayerController
from view.error import ErrorMessage


class MainControler:

    def __init__(self):
        self.view = MainView()
        self.utils = InputUtils()
        self.message = ErrorMessage()

    def main_menu(self):
        while True:
            self.view.main_menu()
            user_entry = self.utils.check_numbers()
            if user_entry == 1:
                run = TournamentController()
                run.tournament_menu()
            elif user_entry == 2:
                run = PlayerController()
                run.main_controller()
            elif user_entry == 5:
                quit()
            else:
                self.message.error_menu()
