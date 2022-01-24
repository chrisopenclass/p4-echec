class TournamentView:

    @staticmethod
    def main_menu():
        print("what did you want to do ? ")
        print("type 1 to create a new tournament ")
        print("type 2 to restore unfinished tournament ")
        print("type 3 to list all tournament ")
        print("type 4 to generate report for tournament")
        print("type 5 to quit")

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
        print("maybe the tournament is finished ?")
        input("press any key to continue")

    @staticmethod
    def round_menu_view():
        print("what did you want to do ?")
        print("type 1 to generate a new round")
        print("type 2 to enter the player score for the round")
        print("type 3 to go back")

    @staticmethod
    def set_player_score_view(player):
        name = player.get("name")
        f_name = player.get("forename")
        rank = player.get("ranking")
        print(f"please enter the score for {name} {f_name} rank: {rank}\n")

    @staticmethod
    def print_tournament(tournaments):
        for tournament in tournaments:
            print(f"tournament name :{tournament.get('name')} \n")
            print(f"tournament description :{tournament.get('description')}\n")
            print(f"tournament location :{tournament.get('location')}\n")
            print(f"tournament date :{tournament.get('date')}\n")
            if tournament.get("status"):
                print("the tournament is finished \n")
            else:
                print("this tournament is not finished yet\n")
            input("press any key to continue\n")
        print("all tournament as been printed")

    @staticmethod
    def print_round_and_match(round):
        round_name = round.get("name")
        match_list = round.get("match_list")
        i = 0
        print(f"{round_name}:\n")
        print(f"all match for the {round_name} are:\n")
        for matchs in match_list:
            i += 1
            print(f"match number {i} is :\n")
            for match in matchs:
                print(f"name: {match[0].get('name')} forename: {match[0].get('forename')}"
                      f" rank: {match[0].get('ranking')}")
            input("press any key to continue \n")

    @staticmethod
    def finished():
        print("you can't enter any score the tournament is finished")

    @staticmethod
    def report_menu():
        print("type 1 to list all player of the tournament sorted by rank")
        print("type 2 to list all player sorted by alphabetical")
        print("type 3 to see all round and match")
        print("type 4 to go back")

