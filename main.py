from src.tdd_stm.pairing import *
from src.tdd_stm.player_list import Player, PlayerList
import itertools
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# CONSTANTS
version = "0.8 beta"
FONT_NAME = "arial"


# TABLE
def update():
    game_frame = Frame(window)

    my_game = ttk.Treeview(game_frame)
    game_frame.grid(column=1, row=1)

    my_game['columns'] = (
    'Standing', 'Starting_Number', 'Name', 'Surname', 'Rating', 'Points', 'SOS', 'SOSOS', 'SODOS', 'Opponents')

    my_game.column("#0", width=0, stretch=NO)
    my_game.column("Standing", anchor=CENTER, width=80)
    my_game.column("Starting_Number", anchor=CENTER, width=80)
    my_game.column("Name", anchor=CENTER, width=80)
    my_game.column("Surname", anchor=CENTER, width=80)
    my_game.column("Rating", anchor=CENTER, width=80)
    my_game.column("Points", anchor=CENTER, width=60)
    my_game.column("SOS", anchor=CENTER, width=60)
    my_game.column("SOSOS", anchor=CENTER, width=60)
    my_game.column("SODOS", anchor=CENTER, width=60)
    my_game.column("Opponents", anchor=CENTER, width=120)

    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("Standing", text="Standing", anchor=CENTER)
    my_game.heading("Starting_Number", text="Starting Number", anchor=CENTER)
    my_game.heading("Name", text="Name", anchor=CENTER)
    my_game.heading("Surname", text="Surname", anchor=CENTER)
    my_game.heading("Rating", text="Rating", anchor=CENTER)
    my_game.heading("Points", text="Points", anchor=CENTER)
    my_game.heading("SOS", text="SOS", anchor=CENTER)
    my_game.heading("SOSOS", text="SOSOS", anchor=CENTER)
    my_game.heading("SODOS", text="SODOS", anchor=CENTER)
    my_game.heading("Opponents", text="Opponents", anchor=CENTER)

    a = 0
    for player in tournament_list.list_of_players:
        my_game.insert(parent='', index='end', iid=a, text='',
                       values=(f'{a + 1}', f'{player.starting_number}', f'{player.name}', f'{player.surname}',
                               f'{player.rating}', f'{player.points}', f'{player.sos}', f'{player.sosos}',
                               f'{player.sodos}', f'{player.opponents}'))
        a += 1
    my_game.grid(column=1, row=1)
    left_label = Label(text=f"Rounds: {rounds} \nPlayers: {len(tournament_list.list_of_players)}")
    left_label.grid(column=0, row=1)

# START

tournament_list = PlayerList()
rounds = 5
tournament_started = False
tournament_list.add_player("Adam", "Dziwoki", 1965)
tournament_list.add_player("Uladzislau", "Zakrzheuski", 2295)
tournament_list.add_player("Mariusz", "Stanaszek", 1651)
tournament_list.add_player("Krzysztof", "Sieja", 1840)

# COMMANDS

def addp_add():
    name = name_entry.get()
    surname = surname_entry.get()
    rating = rating_entry.get()
    tournament_list.add_player(name, surname, rating)
    addp.destroy()
    update()
    print(tournament_list.list_of_players)

def rmvp_rem():
    stn = int(stn_entry.get())
    player_to_delete = tournament_list.find_player_by_starting_number(stn)
    tournament_list.remove_player(stn)
    rmvp.destroy()
    update()

def srft_set():
    rnds = int(srft_entry.get())
    global rounds
    rounds = rnds
    srft.destroy()
    update()

def set_rounds_window():
    global srft
    srft = Toplevel(window)
    srft.config(padx=50, pady=50)
    srft.title('Set rounds')
    srft_label = Label(srft, text="Number of rounds:")
    srft_label.grid(column=0, row=0)
    global srft_entry
    srft_entry = Entry(srft, width=40)
    srft_entry.grid(column=1, row=0)

    srft_button = Button(srft, text="Set rounds", width=20, command=srft_set)
    srft_button.grid(column=0, row=1, columnspan=2)

def remove_player_window():
    global rmvp
    rmvp = Toplevel(window)
    rmvp.config(padx=50, pady=50)
    rmvp.title('Remove player')
    stn_label = Label(rmvp, text="Starting number:")
    stn_label.grid(column=0, row=0)

    global stn_entry
    stn_entry = Entry(rmvp, width=40)
    stn_entry.grid(column=1, row=0)

    addp_button = Button(rmvp, text="Remove player", width=20, command=rmvp_rem)
    addp_button.grid(column=0, row=1, columnspan=2)

    # update()


def add_player_window():
    global addp
    addp = Toplevel(window)
    addp.config(padx=50, pady=50)
    addp.title('Add player')
    name_label = Label(addp, text="Name:")
    name_label.grid(column=0, row=0)

    global name_entry
    name_entry = Entry(addp, width=40)
    name_entry.grid(column=1, row=0)

    surname_label = Label(addp, text="Surname:")
    surname_label.grid(column=0, row=1)

    global surname_entry
    surname_entry = Entry(addp, width=40)
    surname_entry.grid(column=1, row=1)

    rating_label = Label(addp, text="Rating:")
    rating_label.grid(column=0, row=2)

    global rating_entry
    rating_entry = Entry(addp, width=40)
    rating_entry.grid(column=1, row=2)

    addp_button = Button(addp, text="Add player", width=20, command=addp_add)
    addp_button.grid(column=0, row=3, columnspan=2)

    # update()
current_pairing = []
def start_tournament():
    global tournament_started
    tournament_started = True
    add_player_button.destroy()
    remove_player_button.destroy()
    start_tournament_button.destroy()
    set_rounds_button.destroy()
    # choose_pairing_method(tournament_list, rounds)
    global current_pairing
    current_pairing = sp_pairing_for_next_round(tournament_list)
    set_results_window(current_pairing, tournament_list)

def reswin_input(pairlist):
    results_inputted = ""
    for pair in pairlist:
        results_inputted += str((pair.get()))
    resolve_round(current_pairing, tournament_list, results_inputted)
    reswin.destroy()
    update()

def set_results_window(pairs, playerlist):
    global reswin
    reswin = Toplevel(window)
    reswin.config(padx=50, pady=50)
    reswin.title('Round results')
    global pairlist
    pairlist = []
    a = 0
    for p in pairs:
        player_A = playerlist.list_of_players[playerlist.find_player_by_starting_number(p.player1)]
        player_B = playerlist.list_of_players[playerlist.find_player_by_starting_number(p.player2)]
        winner = IntVar()
        pA = Radiobutton(reswin, text=f"{player_A.name} {player_A.surname}", variable=winner, value=1).grid(row=a, column=0)
        pB = Radiobutton(reswin, text=f"{player_B.name} {player_B.surname}", variable=winner, value=2).grid(row=a, column=1)
        pairlist.append(winner)
        a+=1
    reswin_button = Button(reswin, text="Input results", width=20, command=lambda: reswin_input(pairlist))
    reswin_button.grid(row=a+1, column=0, columnspan=2)





#UI

window = Tk()
window.title("Shogi Tournament Manager")

window.config(padx=50, pady=50)

# canvas = Canvas(width=500, height=400)
# logo = PhotoImage(file="logo2.png")
# canvas.create_image(170, 100, image=logo, anchor = N)
# canvas.grid(column=0, row=0)
title_label = Label(text="Shogi Tournament Manager", font=(FONT_NAME, 40, "bold"), fg="red")
title_label.grid(column=0, row=0, columnspan=2)


set_rounds_button = Button(text="Set number of rounds", width=20, command=set_rounds_window)
set_rounds_button.grid(column=0, row=3)

add_player_button = Button(text="Add player", width=20, command=add_player_window)
add_player_button.grid(column=0, row=4)

remove_player_button = Button(text="Remove player", width=20, command=remove_player_window)
remove_player_button.grid(column=0, row=5)

start_tournament_button = Button(text="Start tournament", width=20, command=start_tournament)
start_tournament_button.grid(column=0, row=6)





update()



exit = False
while not exit:
    window.update()
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







