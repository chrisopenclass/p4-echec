class ErrorMessage:

    @staticmethod
    def error_number():
        print("this field can only contain number")
        print("please try again")

    @staticmethod
    def error_lenght():
        print("this field can only contain one character")
        print("please try again")

    @staticmethod
    def error_string_only():
        print("only letters are allowed on this field ")
        print("please try again")

    @staticmethod
    def error_lenght_multiple():
        print(" this field need at least 2 character minimum ")
        print("please try again ")

    @staticmethod
    def error_sex_string():
        print(" this field can only contain M/F or m/f ")
        print("please try again ")

    @staticmethod
    def error_date():
        print("the date must be on this format DD/MM/YYYY")
        print("please try again")

    @staticmethod
    def error_lenght_date():
        print("the date you entered is not valid be sure the format is like DD/MM/YYYY")
        print("please try again")

    @staticmethod
    def error_menu():
        print(" sorry i didn't understand your choice please try again")

    @staticmethod
    def generic_error():
        print("unexpected error Occurred please contact an administrator")

    @staticmethod
    def data_base_save_error():
        print("data not saved to the data base unknown error append ")

    @staticmethod
    def player_not_found():
        print("no player found on the data base be sure player is on the data base try again")

    @staticmethod
    def is_empty():
        print("this field can't be empty please enter at least one character")

    @staticmethod
    def player_score_not_set():
        print("you must enter player score for each match before generating a new round")

    @staticmethod
    def all_round_generated():
        print("all round as been generated please enter the score for the last round to complete"
              "the tournament")

    @staticmethod
    def score_error():
        print("this field can only contain 1 or 0.5 or 0")

    @staticmethod
    def score_len_error():
        print("this field can have more than 3 character")

    @staticmethod
    def round_not_generated():
        print("you need to generate a round first")
