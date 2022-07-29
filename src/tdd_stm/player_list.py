from dataclasses import dataclass, field


@dataclass
class Player:
    name: str
    surname: str
    rating: int
    opponents: list = field(default_factory=list)
    starting_number: int = 0
    points: int = 0
    sos: int = 0
    sosos: int = 0
    msos: int = 0


@dataclass
class PlayerList:
    list_of_players: list = field(default_factory=list)

    def add_player(self, name, surname, rating):
        new_player = Player(name, surname, rating)
        self.list_of_players.append(new_player)
        self.sort_player_list()
        starting_number = 1
        for player in self.list_of_players:
            player.starting_number = starting_number
            starting_number += 1

    def sort_player_list(self):
        self.list_of_players.sort(key=lambda player: (player.surname, player.name))
        self.list_of_players.sort(reverse=True, key=lambda player: (player.points, player.sos, player.sosos, player.msos, player.rating))

    def find_player_by_starting_number(self, number=int):
        index = next((i for i, player in enumerate(self.list_of_players) if player.starting_number == number), -1)
        return index
