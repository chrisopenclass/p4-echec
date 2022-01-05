from tinydb import TinyDB
from view.error import ErrorMessage
from tinydb import Query

_db = TinyDB('db.json', sort_keys=True, indent=4)
_tournament_table = _db.table("tournament_table")


class TournamentModel:

    def __init__(self, name=None, location=None, player=None, time=None,
                 description=None, date=None, round_list=None, finished="false", turn=4):
        self.name = name
        self.location = location
        self.player = player
        self.time = time
        self.description = description
        self.date = date
        self.round_list = round_list
        self.finished = finished
        self.turn = turn

    def serialize(self):
        return {"name": self.name,
                "location": self.location,
                "date": self.date,
                "turn": self.turn,
                "player": self.player,
                "time": self.time,
                "description": self.description,
                "finished": self.finished,
                "round_list": self.round_list
                }

    def save_to_db(self):
        _tournament_table.insert(self.serialize())

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

