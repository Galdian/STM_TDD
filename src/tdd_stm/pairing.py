from src.tdd_stm.player_list import Player, PlayerList
from dataclasses import dataclass, field
import itertools
import random

#
# def choose_pairing_method(playerlist: PlayerList, rounds: int):
#     # print(f"Chosing pairing method for {len(playerlist.list_of_players)} players and {rounds} rounds.")
#     players = len(playerlist.list_of_players)
#     if not len(playerlist.list_of_players) / 2 == 0:
#         players += 1
#     if players - rounds == 1:
#         # print("Round robin chosen")
#         round_robin_pairing(playerlist)
#     else:
#         # print("Swiss pairing chosen")
#         swiss_pairing(playerlist, rounds)
#
# def swiss_pairing(playerlist, rounds):
#     results_updated = True
#     r = 1
#     while results_updated and r <= rounds:
#         sp_next_round(playerlist)
#
#     resolve_round(pairs, playerlist)



def sp_pairing_for_next_round(playerlist: PlayerList):
    # roundnum = 1
    # for round in range(rounds):
    # print(f"Preparing pairing for round {roundnum}")
    # give bye
    current_bye = int
    if not (len(playerlist.list_of_players) % 2 == 0):
        for player in reversed(playerlist.list_of_players):
            if "0+" not in player.opponents:
                player.opponents.append("0+")
                # print(f"Giving bye to {player.starting_number}")
                player.points += 1
                current_bye = player.starting_number
                break
    players_to_be_paired = []
    for player in playerlist.list_of_players:
        if not player.starting_number == current_bye:
            players_to_be_paired.append(player.starting_number)
    # print(f"Players to be paired this round: {players_to_be_paired}")
    # create tier groups
    tiers = {}
    tier_group = 0
    # print("Preparing tiers based on number of points")
    while len(players_to_be_paired) > 0:
        points_required = playerlist.list_of_players[
            playerlist.find_player_by_starting_number(players_to_be_paired[0])].points
        tiers[tier_group] = []
        updated_players_to_be_paired = []
        tested_player = 0
        for player in players_to_be_paired:
            current_player: Player = playerlist.list_of_players[
                playerlist.find_player_by_starting_number(players_to_be_paired[tested_player])]
            if current_player.points == points_required:
                tiers[tier_group].append(player)
            else:
                updated_players_to_be_paired.append(player)
            tested_player += 1
        players_to_be_paired = updated_players_to_be_paired
        if not len(tiers[tier_group]) % 2 == 0:
            tiers[tier_group].append(players_to_be_paired[0])
            del players_to_be_paired[0]
        tier_group += 1
    # print(f"Tiers: \n {tiers}")
    # print("Trying to pair tiers")
    # try to pair inside tiers
    pairs = []
    tiers_paired = False
    while not tiers_paired:
        a = 0
        b = len(tiers)
        temporary_pairs = []
        all_tiers_paired = True
        unpaired_tiers = []
        for tier in range(b):
            # print(f"I am trying to pair tier {a}: {tiers[a]}")
            tried_pairs = try_to_pair_tier(playerlist, tiers[a])
            if len(tried_pairs) > 0:
                for pair in tried_pairs:
                    temporary_pairs.append(pair)
                # print(f"I have successfully paired tier {a}: {tiers[a]} \n current pairs: {temporary_pairs}")
            elif len(tiers[a]) == 0:
                pass
            else:
                # print(f"I couldn't pair tier {a}")
                unpaired_tiers.append(a)
                all_tiers_paired = False
            a += 1
        # print(temporary_pairs)
        if all_tiers_paired:
            tiers_paired = True
            pairs = temporary_pairs
        else:
            # print(f"I had tiers: \n {tiers} \n but couldn't pair tiers: {unpaired_tiers}")
            tiers = mix_tiers(tiers, unpaired_tiers)
            # print(f"I have mixed tiers, will try to pair the following tiers: \n {tiers}")
    # print(roundnum)
    # for p in pairs:
    #     print(p)
    #     print(f"p1 points: {playerlist.list_of_players[playerlist.find_player_by_starting_number(p.player1)].points}, p2 points: {playerlist.list_of_players[playerlist.find_player_by_starting_number(p.player2)].points}")
    return pairs

    # roundnum += 1


def mix_tiers(tiers: dict, unpaired_tiers: list):
    # while len(unpaired_tiers) > 0:
    #     tier_to_update = unpaired_tiers[0]
    #     if tier_to_update +1 == len(tiers):
    #         a = -1
    #         while len(tiers[tier_to_update + a]) == 0:
    #             a -= 1
    #         tier_to_mix_in = tier_to_update + a
    #         for player in tiers[tier_to_update]:
    #             tiers[tier_to_mix_in].append(player)
    #         tiers[tier_to_update] = []
    #         unpaired_tiers.remove(tier_to_update)
    #     else:
    #         tier_to_try_if_empty = 1
    #         while len(tiers[tier_to_update + tier_to_try_if_empty]) == 0:
    #             tier_to_try_if_empty += 1
    #         tier_to_mix_in = tier_to_update + tier_to_try_if_empty
    #         tiers[tier_to_update].append(tiers[tier_to_mix_in][0])
    #         tiers[tier_to_update].append(tiers[tier_to_mix_in][1])
    #         del tiers[tier_to_mix_in][0:2]
    #         unpaired_tiers.remove(tier_to_update)
    #         if tier_to_mix_in in unpaired_tiers:
    #             unpaired_tiers.remove(tier_to_mix_in)

    while len(unpaired_tiers) > 0:
        tier_to_update = unpaired_tiers[0]
        a = 1
        if len(tiers) > tier_to_update + 1:
            while (len(tiers[tier_to_update + a]) == 0) and ((tier_to_update + a) < (len(tiers) - 1)):
                a += 1
            if len(tiers[tier_to_update + a]) == 0:
                a = -1
                while (len(tiers[tier_to_update + a]) == 0) and ((tier_to_update + a) < len(tiers)):
                    a -= 1
            tier_to_mix_in = tier_to_update + a
        else:
            tier_to_try_if_empty = 1
            while len(tiers[tier_to_update - tier_to_try_if_empty]) == 0:
                tier_to_try_if_empty += 1
            tier_to_mix_in = tier_to_update - tier_to_try_if_empty
        # print(f"tier to update: {tier_to_update} tier to mix: {tier_to_mix_in}")
        for player in tiers[tier_to_mix_in]:
            tiers[tier_to_update].append(player)
        tiers[tier_to_mix_in] = []
        unpaired_tiers.remove(tier_to_update)
        if tier_to_mix_in in unpaired_tiers:
            unpaired_tiers.remove(tier_to_mix_in)
    return tiers


def try_to_pair_tier(playerlist: PlayerList, tier: list):
    tlen = len(tier)
    if tlen == 0:
        return []
    else:
        temporary_pairs = []
        tier_paired = True
        # 1st attempt - higher vs lower half
        player_in_list = 0
        # print("Trying to perform higher vs lower half pairing")
        for player in range(int(tlen / 2)):
            temporary_pairs.append(add_pair(tier[player_in_list], tier[player_in_list + int(tlen / 2)]))
            # print(f"Higher: {tier[player_in_list]}, lower: {tier[player_in_list + int(tlen/2)]}")
            if played_already(playerlist, tier[player_in_list], tier[player_in_list + int(tlen / 2)]):
                tier_paired = False
                temporary_pairs = []
                # print(f"I couldn't pair higher vs lower half because {tier[player_in_list]} has already played with {tier[int(player_in_list+tlen/2)]}")
                break
            player_in_list += 1
        if tier_paired:
            # print("Higher vs lower half pairing successfull")
            return temporary_pairs
        # 2nd attempt
        if not tier_paired:
            # print("Will try to pair anyway!")
            possible_pairings = []
            if len(tier) <= 8:
                all_combinations = list(itertools.permutations(tier, tlen))
            else:
                all_combinations = []
                c = []
                c = tier
                for a in range(5000):
                    b = []
                    for value in sorted(tier, key=lambda _: random.random()):
                        b.append(value)
                    all_combinations.append(b)
            all_possible_pairings = []
            # sorting combinations
            for combination in all_combinations:
                a = 0
                temporary_combination = []
                for pair in range(int(tlen / 2)):
                    if combination[a] < combination[a + 1]:
                        temporary_combination.append([combination[a], combination[a + 1]])
                    else:
                        temporary_combination.append([combination[a + 1], combination[a]])
                    a += 2
                temporary_combination.sort()
                new_combination = []
                for pair in temporary_combination:
                    new_combination.append(pair[0])
                    new_combination.append(pair[1])
                all_possible_pairings.append(new_combination)
            no_duplicate_pairings = []
            for pairing in all_possible_pairings:
                if pairing not in no_duplicate_pairings:
                    no_duplicate_pairings.append(pairing)

            for pairing in no_duplicate_pairings:
                a = 0
                pairs_to_analyze = []
                for r in range(int(tlen / 2)):
                    if not played_already(playerlist, pairing[a], pairing[a + 1]):
                        pairs_to_analyze.append(add_pair(pairing[a], pairing[a + 1]))
                    a += 2
                if len(pairs_to_analyze) == int(tlen / 2):
                    possible_pairings.append(pairs_to_analyze)

            # print("I have the following possible pairings:")
            possible_pairing = 0
            for pairing in possible_pairings:
                # print(possible_pairings[possible_pairing])
                possible_pairing += 1
            # print("Will try to choose the best one")
            best_pairing = sort_pairings(playerlist, possible_pairings)
            if not best_pairing == -1:
                # print(f"I have found the best pairing to be: \n {possible_pairings[best_pairing]}")
                return possible_pairings[best_pairing]
            else:
                # print("I couldn't find any pairing for this tier")
                return []


def sort_pairings(playerlist: PlayerList, possible_pairings: list):
    pairings = []
    index = 0
    for pairing in possible_pairings:
        highest_points_diff = 0
        total_points_diff = 0
        sos_diff = 0
        sosos_diff = 0
        sodos_diff = 0
        for pair in possible_pairings[index]:
            p1 = playerlist.list_of_players[playerlist.find_player_by_starting_number(pair.player1)]
            p2 = playerlist.list_of_players[playerlist.find_player_by_starting_number(pair.player2)]
            if p1.points - p2.points > highest_points_diff:
                highest_points_diff = p1.points - p2.points
            if p2.points - p1.points > highest_points_diff:
                highest_points_diff = p2.points - p1.points
            if p1.points > p2.points:
                total_points_diff += (p1.points - p2.points)
            if p2.points > p1.points:
                total_points_diff += (p2.points - p1.points)
            if p1.sos > p2.sos:
                sos_diff += (p1.sos - p2.sos)
            if p2.sos > p1.sos:
                sos_diff += (p2.sos - p1.sos)
            if p1.sosos > p2.sosos:
                sosos_diff += (p1.sosos - p2.sosos)
            if p2.sosos > p1.sosos:
                sosos_diff += (p2.sosos - p1.sosos)
            if p1.sodos > p2.sodos:
                sodos_diff += (p1.sodos - p2.sodos)
            if p2.sodos > p1.sodos:
                sodos_diff += (p2.sodos - p1.sodos)
            # print(f"{p1}, {p2}, {p1.sodos}, {p2.sodos}, {sodos_diff}")
        new_pairing = Pairing(index, highest_points_diff, total_points_diff, sos_diff, sosos_diff, sodos_diff)
        pairings.append(new_pairing)
        index += 1
    pairings.sort(key=lambda pairing: (
    pairing.highest_points_diff, pairing.total_points_diff, pairing.sos_diff, pairing.sosos_diff))
    for pairing in pairings:
        print(pairing)
    if len(pairings) > 0:
        return pairings[0].index
    else:
        return -1


def played_already(playerlist: PlayerList, player1: int, player2: int):
    p1 = playerlist.list_of_players[playerlist.find_player_by_starting_number(player1)]
    played = False
    for opponent in p1.opponents:
        opponent = int(opponent[:-1])
        if opponent == player2:
            played = True
    return played


def round_robin_pairing(playerlist: PlayerList):
    players_num = len(playerlist.list_of_players)
    players_to_be_paired = []
    starting_number = 1
    for player in range(players_num):
        players_to_be_paired.append(starting_number)
        starting_number += 1
    # add dummy player if number of players is odd
    if not len(players_to_be_paired) % 2 == 0:
        players_to_be_paired.append(0)
    players_num = len(players_to_be_paired)

    rounds = players_num - 1
    pairs = int(players_num / 2)
    # print(players_to_be_paired)
    pairlist = []
    for r in range(rounds):
        first_paired_player = 0
        second_paired_player = rounds
        current_pairs = []
        for p in range(pairs):
            current_pairs.append(
                add_pair(players_to_be_paired[first_paired_player], players_to_be_paired[second_paired_player]))
            first_paired_player += 1
            second_paired_player -= 1
        pairlist.append(current_pairs)
        player_moved = players_to_be_paired[rounds]
        players_to_be_paired.insert(1, player_moved)
        players_to_be_paired.pop()
    return pairlist

def resolve_round(pairs: list, playerlist: PlayerList, results: str):
    a = 0
    for p in pairs:
        if p.player1 == 0:
            player_with_bye = playerlist.list_of_players[playerlist.find_player_by_starting_number(p.player2)]
            # print(f"{player_with_bye.name} {player_with_bye.surname} got BYE")
            player_with_bye.points += 1
            player_with_bye.opponents.append(f"0+")
        elif p.player2 == 0:
            player_with_bye = playerlist.list_of_players[playerlist.find_player_by_starting_number(p.player1)]
            # print(f"{player_with_bye.name} {player_with_bye.surname} got BYE")
            player_with_bye.points += 1
            player_with_bye.opponents.append(f"0+")
        else:
            player_A = playerlist.list_of_players[playerlist.find_player_by_starting_number(p.player1)]
            player_B = playerlist.list_of_players[playerlist.find_player_by_starting_number(p.player2)]
            # print(f"{player_A.name} {player_A.surname} vs {player_B.name} {player_B.surname}")
            # result = input("Which player has won? a or b")
            # print(f"Which player has won? a or b? {result}")
            print(results)
            if results[a] == "1":
                player_A.points += 1
                player_A.opponents.append(f"{player_B.starting_number}+")
                player_B.opponents.append(f"{player_A.starting_number}-")
            if results[a] == "2":
                player_B.points += 1
                player_A.opponents.append(f"{player_B.starting_number}-")
                player_B.opponents.append(f"{player_A.starting_number}+")
            a += 1
    playerlist.update_tiebreaks()
    playerlist.print_player_list()
    # c = input("next round - enter")


def add_pair(player1: int, player2: int):
    return Pair(player1, player2)


@dataclass
class Pair:
    player1: int
    player2: int


@dataclass
class Pairing:
    index: int
    highest_points_diff: int
    total_points_diff: int
    sos_diff: int
    sosos_diff: int
    sodos_diff: int


def add_pairing(self, index, highest_point_diff, total_points_diff, sos_diff):
    new_pairing = Pairing(index, highest_point_diff, total_points_diff, sos_diff)
