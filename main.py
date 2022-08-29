from src.tdd_stm.pairing import *
from src.tdd_stm.player_list import Player, PlayerList
import itertools
from tkinter import *
from tkinter import messagebox


# CONSTANTS
version = "0.8 beta"

#UI

window = Tk()
window.title("Shogi Tournament Manager")

window.config(padx=50, pady=50)


window.mainloop()
#
# test = PlayerList()
# # test.add_player("Janik", "Kruse", 1563)
# # test.add_player("Paradowski", "Dawid", 1909)
# # test.add_player("Paily", "Andriy", 1857)
# # test.add_player("Adam", "Dziwoki", 2018)
# # test.add_player("Omelchuk", "Roman", 1870)
# # test.add_player("Markowski", "Sebastian", 1223)
# # test.add_player("Roman", "Milosz", 1754)
# # test.add_player("Adaszewski", "Grzegorz", 1601)
#
# # test.add_player("Pfaffel", "Thomas", 1965)
# # test.add_player("Kasai", "Takehiko", 1485)
# # test.add_player("Cain", "Steven", 1861)
# # test.add_player("Vyletel", "Lukas", 1521)
# # test.add_player("Trauner", "Andrej", 1331)
# # test.add_player("Schmied", "Horst", 1257)
# # test.add_player("Katona", "Timea", 830)
# # test.add_player("Saito", "Yusuke", 1)
#
# def add_13_players():
#     test.add_player("Adam", "Dziwoki", 1965)
#     test.add_player("Uladzislau", "Zakrzheuski", 2295)
#     test.add_player("Mariusz", "Stanaszek", 1651)
#     test.add_player("Stefanos", "Mandalas", 1918)
#     test.add_player("Milosz", "Roman", 1693)
#     test.add_player("Iori", "Matsumoto", 1625)
#     test.add_player("Krzysztof", "Sieja", 1854)
#     test.add_player("Michal", "Mordarski", 1551)
#     test.add_player("Pawel", "Hunczak", 1332)
#     test.add_player("Grzegorz", "Adaszewski", 1615)
#     test.add_player("Franciszek", "Mordarski", 1346)
#     test.add_player("Jacek", "Prochal", 1207)
#     test.add_player("Krzysztof", "Orlinski", 1231)
# # test.add_player("Marcin", "Kozlowski", 941)
#
# test.print_player_list()
#
# a = 0
# while a < 1:
#     # blockPrint()
#     add_13_players()
#     choose_pairing_method(test, 9)
#     test.list_of_players = []
#     a+= 1
#     # enablePrint()
#     # print(a)







