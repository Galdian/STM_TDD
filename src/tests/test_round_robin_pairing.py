from src.tdd_stm.pairing import Pair, round_robin_pairing, add_pair, resolve_round, choose_pairing_method, swiss_pairing, try_to_pair_tier, played_already

from src.tdd_stm.player_list import Player, PlayerList

test_list = PlayerList()
test_list.add_player("Adam", "Dziwoki", 1900)
test_list.add_player("Krzysztof", "Sieja", 1800)
test_list.add_player("Grzegorz", "Adaszewski", 1600)
test_list.add_player("Miłosz", "Roman", 1750)
test_list.add_player("Dawid", "Paradowski", 1850)
test_list.add_player("Dawid", "Paradowski", 2850)
test_list.add_player("Dawid", "Paradowski", 6850)
# test_list.list_of_players[0].points = 1
# test_list.list_of_players[1].points = 1
# test_list.list_of_players[2].points = 1
test_list.list_of_players[0].opponents.append("3+")
test_list.list_of_players[0].opponents.append("4+")
# test_list.list_of_players[0].opponents.append("2+")
# test_list.list_of_players[0].opponents.append("5+")
test_list.list_of_players[0].opponents.append("6+")
test_list.list_of_players[0].opponents.append("7+")

def test_choose_pairing_method(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "a")
    choose_pairing_method(test_list, 4)


# def test_played_already():
#     print(played_already(test_list, 1, 2))
#     test_list.list_of_players[0].opponents.append("2+")
#     print(test_list.list_of_players[0].opponents)
#     print(played_already(test_list, 1, 2))



#
# def test_construction_pair():
#     new_pair = Pair(1, 2)
#
#
# def test_pairing(monkeypatch):
#     monkeypatch.setattr('builtins.input', lambda _: "a")
#     round_robin_pairing(test_list)
#
#
# def test_add_pair():
#     add_pair(1,2)
#
#
# def test_resolve_round(monkeypatch):
#     monkeypatch.setattr('builtins.input', lambda _: "a")
#     pairs = [add_pair(1, 2), add_pair(3, 4)]
#     resolve_round(pairs, test_list)
