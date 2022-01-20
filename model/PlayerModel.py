from tinydb import *
from view.error import ErrorMessage

_db = TinyDB('db.json', sort_keys=True, indent=4)
_player_table = _db.table("_player_table")


class Player:

    def __init__(self, f_name=None, l_name=None, sex=None, b_date=None, rank=None):
        self.f_name = f_name
        self.l_name = l_name
        self.sex = sex
        self.b_date = b_date
        self.rank = rank
        self.player_id = -1

    def serialize(self):
        return {
            "name": self.f_name,
            "forename": self.l_name,
            "sex": self.sex,
            "born_date": self.b_date,
            "ranking": self.rank,
            "id": self.player_id
        }

    def save_to_db(self):
        try:
            saving = _player_table.insert(self.serialize())
            if saving:
                Player.update_id(self)
                return True
            else:
                return False
        except ValueError:
            ErrorMessage.generic_error()

    def update_id(self):
        player_id = Player.search_to_db(self)
        _player_table.update({'id': player_id}, doc_ids=[player_id])

    def search_to_db(self):
        player = Query()
        try:
            search_result = _player_table.get((player.name == self.f_name) & (player.forename == self.l_name)
                                             & (player.born_date == self.b_date))
            if not search_result:
                return False
            else:
                player_id = search_result.doc_id
                return player_id
        except ValueError:
            ErrorMessage().generic_error()

    @staticmethod
    def get_player_elo(player_id):
        player = _player_table.get(doc_id=int(player_id))
        elo = player.get("ranking")
        return elo

    @staticmethod
    def get_player(player_id):
        player = _player_table.get(doc_id=int(player_id))
        return player

    @staticmethod
    def get_all_player():
        return _player_table.all()

    @staticmethod
    def update_player_rank(player_id, new_rank):
        _player_table.update({'ranking': new_rank}, doc_ids=[player_id])
        return True
