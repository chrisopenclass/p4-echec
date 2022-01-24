from tinydb import TinyDB, Query
from view.error import ErrorMessage


_db = TinyDB('db.json', sort_keys=True, indent=4)
_tournament_table = _db.table("tournament_table")


class TournamentModel:

    def __init__(
            self, name=None, location=None, player=None, time=None,
            description=None, date=None, round_list=None,
            finished="false", turn=4, id=None):
        self.name = name
        self.location = location
        self.player = player
        self.time = time
        self.description = description
        self.date = date
        self.round_list = round_list
        self.finished = finished
        self.turn = turn
        self.id = id

    def serialize(self):
        return {"name": self.name,
                "location": self.location,
                "date": self.date,
                "turn": self.turn,
                "player": self.player,
                "time": self.time,
                "description": self.description,
                "finished": self.finished,
                "round_list": self.round_list,
                "id": self.id
                }

    def update_id(self):
        tournament_id = TournamentModel.get_tournament_id(self)
        _tournament_table.update({'id': tournament_id}, doc_ids=[tournament_id])

    def save_to_db(self):
        try:
            saving = _tournament_table.insert(self.serialize())
            if saving:
                TournamentModel.update_id(self)
                return True
            else:
                return False
        except ValueError:
            ErrorMessage.generic_error()

    def search_to_db(self):
        tournament = Query()
        try:
            search_result = _tournament_table.get((tournament.name == self.name) &
                                                  (tournament.location == self.location) &
                                                  (tournament.finished == "false"))
            if not search_result:
                return False
            else:
                return search_result
        except ValueError:
            ErrorMessage().generic_error()

    def get_tournament_id(self):
        tournament = Query()
        try:
            search_result = _tournament_table.get((tournament.name == self.name) &
                                                  (tournament.location == self.location))
            if not search_result:
                return False
            else:
                tournament_id = search_result.doc_id
                return tournament_id
        except ValueError:
            ErrorMessage().generic_error()

    @staticmethod
    def update_to_db(tournament, tournament_id):
        _tournament_table.update(tournament, doc_ids=[tournament_id])

    @staticmethod
    def extract_all_tournament():
        return _tournament_table.all()

    def search_to_db_for_finished(self):
        tournament = Query()
        try:
            search_result = _tournament_table.get((tournament.name == self.name) &
                                                  (tournament.location == self.location) &
                                                  (tournament.finished == "true"))
            if not search_result:
                return False
            else:
                return search_result
        except ValueError:
            ErrorMessage().generic_error()