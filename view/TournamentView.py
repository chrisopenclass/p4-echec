class TournamentView:

    @staticmethod
    def main_menu():
        print("what did you want to do ? ")
        print("type 1 to create a new tournament")
        print("type 2 to restore unfinished tournament")
        print("type 3 to quit")

    @staticmethod
    def tournament_name():
        print("please enter the tournament name")

    @staticmethod
    def tournament_location():
        print("please enter the tournament location")

    @staticmethod
    def tournament_date():
        print("please enter the tournament date like this format DD/MM/YYY")

    @staticmethod
    def save_confirmation():
        print("tournament correctly saved to the data base")

    @staticmethod
    def time_choice_view():
        print("what is the time of the tournament ? type 1 for bullet type 2 for blitz or type 3 for a quick stroke")

    @staticmethod
    def ask_for_description():
        print("you can type the tournament description here")

    @staticmethod
    def start_now():
        print("would you want to start the tournament now ? ")

    @staticmethod
    def tournament_not_exist():
        print("no tournament unfinished find please verify the given information")

    @staticmethod
    def round_menu_view():
        print("what did you want to do ?")
        print("type 1 to generate a new round")
        print("type 2 to enter the player score for the round")
        print("type 3 to go back")

    @staticmethod
    def set_player_score_view(player):
        print("please enter the score for :")
        print(player)
