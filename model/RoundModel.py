# model importation
from model.PlayerModel import Player
# python module importation
import datetime
from tinydb import *
from view.TournamentView import TournamentView
from utils.utils import InputUtils

_db = TinyDB('db.json', sort_keys=True, indent=4)
_tournament_table = _db.table("tournament_table")


class RoundModel:

    def __init__(self, match_list=None, name=None, starting_date=None, end_date=None):
        if match_list is None:
            self.match_list = []
        self.match_list = match_list
        self.name = name
        self.starting_date = starting_date
        if end_date is None:
            self.end_date = end_date

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
            "match_list": self.match_list,
            "starting_date": self.starting_date,
            "end_date": self.end_date
        }

    @staticmethod
    def actual_date():
        return datetime.datetime.now().strftime("%d/%m/%Y")

    @staticmethod
    def select_actual_round(list_of_round):
        for find_round in list_of_round:
            for actual_round in find_round:
                if not actual_round.get("end_date"):
                    return actual_round
                elif actual_round:
                    return False

    @staticmethod
    def set_player_score(match):
        for player in match:
            TournamentView().set_player_score_view(player[0])
            player[1] = InputUtils().check_player_score()
            if not player[0].get("total_score"):
                player[0].update({"total_score": player[1]})
            else:
                player[0].get("player_score")+player[0]

    def generate_other_round(self):
        """génération des autre round
        pour chopper le dernier élément de la liste lent(liste(-1))
        """
        pass
