class View:

    @staticmethod
    def f_name():
        print("please enter the player name")

    @staticmethod
    def l_name():
        print("please enter the player last name")

    @staticmethod
    def sex():
        print("please enter the player sex ( M for male or F for female")

    @staticmethod
    def borne_date():
        print("please enter player born date ( good format DD/MM/YYYY")

    @staticmethod
    def rank():
        print("please enter player rank")

    @staticmethod
    def creation_confirmation():
        print("player correctly added to the database")

    @staticmethod
    def get_menu():
        print("type 1 to add player \n")
        print("type 2 to list all player sorted by alphabetical order  \n")
        print("type 3 to list all player sorted by rank order  \n")
        print("type 4 to edit player rank \n")
        print("type 5 to quit \n")

    @staticmethod
    def print_player(sorted_player):
        for player in sorted_player:
            print(f"{player.get('name')} {player.get('forename')} rank: {player.get('ranking')} \n")

