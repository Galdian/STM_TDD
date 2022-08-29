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
    sodos: int = 0
    is_paired: bool = False


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
        self.list_of_players.sort(reverse=True, key=lambda player: (player.points, player.sos, player.sosos, player.sodos, player.rating))

    def find_player_by_starting_number(self, number: int):
        index = next((i for i, player in enumerate(self.list_of_players) if player.starting_number == number), -1)
        return index

    def print_player_list(self):
        for player in self.list_of_players:
            print(f"SN{player.starting_number} N: {player.name} S: {player.surname} R: {player.rating} P:{player.points} S:{player.sos} SS: {player.sosos} SD: {player.sodos} O: {player.opponents}")


    def update_tiebreaks(self):
        for player in self.list_of_players:
            sos = 0
            opponent_checked = 0
            for o in range(len(player.opponents)):
                starting_number = int(player.opponents[opponent_checked][:-1])
                if starting_number == 0:
                    if len(player.opponents) == 1:
                        pass
                    else:
                        sos += player.points
                else:
                    opponent = self.find_player_by_starting_number(starting_number)
                    sos += self.list_of_players[opponent].points
                opponent_checked += 1
            player.sos = sos
        for player in self.list_of_players:
            sosos = 0
            opponent_checked = 0
            for o in range(len(player.opponents)):
                starting_number = int(player.opponents[opponent_checked][:-1])
                if starting_number == 0:
                    if len(player.opponents) == 1:
                        pass
                    else:
                        sosos += player.sos
                else:
                    opponent = self.find_player_by_starting_number(starting_number)
                    sosos += self.list_of_players[opponent].sos
                opponent_checked += 1
            player.sosos = sosos
        for player in self.list_of_players:
            sodos = 0
            opponent_checked = 0
            for o in range(len(player.opponents)):
                if player.opponents[opponent_checked][-1] == "+":
                    starting_number = int(player.opponents[opponent_checked][:-1])
                    if starting_number == 0:
                        sodos += player.sodos
                    else:
                        opponent = self.find_player_by_starting_number(starting_number)
                        sodos += self.list_of_players[opponent].sos
                opponent_checked += 1
            player.sodos = sodos
        self.sort_player_list()



