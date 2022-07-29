from src.tdd_stm.player_list import Player, PlayerList


def test_construction_player():
    new_player = Player("name", "surname", 1900)


def test_players_defaults():
    new_player = Player("name", "surname", 1900)
    print(new_player.points)


def test_construction_player_list():
    new_player_list = PlayerList()
    assert new_player_list.list_of_players == []


def test_add_player_to_player_list():
    new_player_list = PlayerList()
    new_player_list.add_player("name", "surname", 1900)


def test_player_list_sort():
    new_player_list = PlayerList()
    new_player_list.add_player("Adam", "Dziwoki", 1900)
    new_player_list.add_player("Krzysztof", "Sieja", 1800)
    new_player_list.sort_player_list()


def test_check_player_starting_number():
    new_player_list = PlayerList()
    new_player_list.add_player("Adam", "Dziwoki", 1900)
    assert new_player_list.list_of_players[0].starting_number


def test_find_player():
    new_player_list = PlayerList()
    new_player_list.add_player("Krzysztof", "Sieja", 1800)
    new_player_list.add_player("Adam", "Dziwoki", 1900)
    new_player_list.sort_player_list()
    tested_player = new_player_list.list_of_players[new_player_list.find_player_by_starting_number(2)]
    print(tested_player.name)
