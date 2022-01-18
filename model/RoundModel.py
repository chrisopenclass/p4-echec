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
        self.name = name
        self.starting_date = starting_date
        if end_date is None:
            self.end_date = end_date

    def generate_round(self, player_list, round_name):
        self.name = round_name
        list_of_player = []
        for players in player_list:
            player = Player.get_player(players)
            player.update({"opponent_history": []})
            list_of_player.append(player)
        sorted_player = sorted(list_of_player, key=lambda ele: ele["ranking"], reverse=True)
        sorted_player[0].update({"opponent_history": [sorted_player[4].get("id")]})
        sorted_player[4].update({"opponent_history": [sorted_player[0].get("id")]})
        sorted_player[1].update({"opponent_history": [sorted_player[5].get("id")]})
        sorted_player[5].update({"opponent_history": [sorted_player[1].get("id")]})
        sorted_player[2].update({"opponent_history": [sorted_player[6].get("id")]})
        sorted_player[6].update({"opponent_history": [sorted_player[2].get("id")]})
        sorted_player[3].update({"opponent_history": [sorted_player[7].get("id")]})
        sorted_player[7].update({"opponent_history": [sorted_player[3].get("id")]})
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
    def set_player_score(match):
        for player in match:
            TournamentView().set_player_score_view(player[0])
            player[1] = InputUtils().check_player_score()
            if not player[0].get("total_score"):
                player[0].update({"total_score": player[1]})
            else:
                actual_score = player[0].get("total_score")
                print(actual_score)
                round_score = player[1]
                print(type(round_score))
                total_score = actual_score + round_score
                player[0].update({"total_score": total_score})

    @staticmethod
    def get_all_player(match):
        player_list = []
        for players in match:
            for player in players:
                player_list.append(player[0])
        return player_list

    def generate_other_round(self, player_list, round_name):
        self.name = round_name
        list_of_player = []
        for players in player_list:
            list_of_player.append(players)
        sorted_player = sorted(list_of_player, key=lambda ele: (ele["total_score"], ele["ranking"]), reverse=True)
        if not sorted_player[4].get("id") in sorted_player[0].get("opponent_history"):
            sorted_player[0].get("opponent_history").append(sorted_player[4].get("id"))
            sorted_player[4].get("opponent_history").append(sorted_player[0].get("id"))
            sorted_player[1].get("opponent_history").append(sorted_player[5].get("id"))
            sorted_player[5].get("opponent_history").append(sorted_player[1].get("id"))
            sorted_player[2].get("opponent_history").append(sorted_player[6].get("id"))
            sorted_player[6].get("opponent_history").append(sorted_player[2].get("id"))
            sorted_player[3].get("opponent_history").append(sorted_player[7].get("id"))
            sorted_player[7].get("opponent_history").append(sorted_player[3].get("id"))
            self.match_list = [
                ([sorted_player[0], -1], [sorted_player[4], -1]),
                ([sorted_player[1], -1], [sorted_player[5], -1]),
                ([sorted_player[2], -1], [sorted_player[6], -1]),
                ([sorted_player[3], -1], [sorted_player[7], -1])
                ]
        else:
            sorted_player[0].get("opponent_history").append(sorted_player[5].get("id"))
            sorted_player[5].get("opponent_history").append(sorted_player[0].get("id"))
            sorted_player[1].get("opponent_history").append(sorted_player[4].get("id"))
            sorted_player[4].get("opponent_history").append(sorted_player[1].get("id"))
            sorted_player[2].get("opponent_history").append(sorted_player[6].get("id"))
            sorted_player[6].get("opponent_history").append(sorted_player[2].get("id"))
            sorted_player[3].get("opponent_history").append(sorted_player[7].get("id"))
            sorted_player[7].get("opponent_history").append(sorted_player[3].get("id"))
            self.match_list = [
                ([sorted_player[0], -1], [sorted_player[5], -1]),
                ([sorted_player[1], -1], [sorted_player[4], -1]),
                ([sorted_player[2], -1], [sorted_player[6], -1]),
                ([sorted_player[3], -1], [sorted_player[7], -1])
            ]
        self.starting_date = self.actual_date()
        return self.serialize()

    @staticmethod
    def get_all_round(list_of_round):
        for find_round in list_of_round:
            return find_round[-1]
