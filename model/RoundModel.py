# model importation
from model.PlayerModel import Player
# python module importation
import datetime
from tinydb import *
from view.error import ErrorMessage
from tinydb import Query

_db = TinyDB('db.json', sort_keys=True, indent=4)
_tournament_table = _db.table("tournament_table")


class RoundModel:

    def __init__(self):
        self.match_list = None
        self.name = None
        self.starting_date = None
        self.end_date = None

    def generate_round(self, player_list, round_name):
        self.name = round_name
        list_of_player = []
        for players in player_list:
            player = Player.get_player(players)
            list_of_player.append(player)
        sorted_player = sorted(list_of_player, key=lambda ele: ele["ranking"], reverse=True)
        self.match_list = [
            ([sorted_player[0], -1], [sorted_player[4], -1]),
            ([sorted_player[1], -1], [sorted_player[5], -1]),
            ([sorted_player[2], -1], [sorted_player[6], -1]),
            ([sorted_player[3], -1], [sorted_player[7], -1])
            ]
        self.starting_date = self.actual_date()
        return self.serialize()

    def serialize(self):
        return{
            "name": self.name,
            "match list": self.match_list,
            "starting date ": self.starting_date,
            "end date": self.end_date
        }

    def other_round(self):
        pass

    @staticmethod
    def actual_date():
        date = datetime.datetime.now().strftime("%d/%m/%Y")
        return date
