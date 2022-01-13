import re
from view.error import ErrorMessage


class InputUtils:

    def __init__(self, word=None):
        self.word = word
        self.check_string_patern = r"^[A-Za-z\é\è\ê\ë\ç\ï\ô\-]+$"
        self.check_number_patern = r"^[0-9]+$"
        self.message = ErrorMessage()
        self.check_sex_patern = r"[m/f/M/F]+$"
        self.check_score_patern = r"[0-1\0.5]+$"
        self.check_date_patern = r"^(?:0[1-9]|1[0-9]|2[0-9]|3[01])\/(?:0[1-9]|1[12])\/(?:19[2-9]\d|[2-9]\d{3})$"

    def check_numbers(self):
        while True:
            self.word = input("").replace(" ", "")
            try:
                testing = re.match(self.check_number_patern, self.word)
                if not testing:
                    self.message.error_number()
                elif not len(self.word) == 1:
                    self.message.error_lenght()
                else:
                    return int(self.word)
            except ValueError:
                self.message.generic_error()

    def check_string(self):
        while True:
            self.word = input("").replace(" ", "").upper()
            try:
                testing = re.match(self.check_string_patern, self.word)
                if not testing:
                    self.message.error_string_only()
                elif not len(self.word) >= 2:
                    self.message.error_lenght_multiple()
                else:
                    return self.word
            except ValueError:
                self.message.generic_error()

    def check_sex(self):
        while True:
            self.word = input("").replace(" ", "").upper()
            try:
                testing = re.match(self.check_sex_patern, self.word)
                if not testing:
                    self.message.error_sex_string()
                else:
                    return self.word
            except ValueError:
                self.message.generic_error()

    def check_date(self):
        while True:
            self.word = input("").replace(" ", "")
            try:
                testing = re.match(self.check_date_patern, self.word)
                if not testing:
                    self.message.error_date()
                elif not len(self.word) >= 8:
                    self.message.error_lenght_date()
                else:
                    return self.word
            except ValueError:
                self.message.generic_error()

    def check_multiple_number(self):
        while True:
            self.word = input("").replace(" ", "")
            try:
                testing = re.match(self.check_number_patern, self.word)
                if not testing:
                    self.message.error_number()
                elif not len(self.word):
                    self.message.error_lenght()
                else:
                    return int(self.word)
            except ValueError:
                self.message.generic_error()

    def check_description(self):
        while True:
            self.word = input("")
            try:
                if not len(self.word):
                    self.message.is_empty()
                else:
                    return self.word
            except ValueError:
                self.message.generic_error()

    def check_player_score(self):
        while True:
            self.word = input("").replace(" ", "")
            try:
                testing = re.match(self.check_score_patern, self.word)
                if not testing:
                    self.message.score_error()
                elif len(self.word) < 1:
                    self.message.is_empty()
                elif len(self.word) > 3:
                    self.message.score_len_error()
                elif self.word == "1":
                    return 1
                elif self.word == "0":
                    return 0
                elif self.word == "0.5":
                    return 0.5
                else:
                    self.message.generic_error()
            except ValueError:
                self.message.generic_error()


