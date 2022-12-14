from src.tdd_stm.pairing import *
from src.tdd_stm.player_list import PlayerList
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import date
import random

# CONSTANTS
FONT_NAME = "arial"


# TABLE
def update():
    game_frame = Frame(window)

    my_game = ttk.Treeview(game_frame)
    game_frame.grid(column=1, row=1, rowspan=6)

    my_game['columns'] = (
        'Standing', 'Starting_Number', 'Name', 'Surname', 'Rating', 'Points', 'SOS', 'SOSOS', 'SODOS', 'Opponents')

    my_game.column("#0", width=0, stretch=NO)
    my_game.column("Standing", anchor=CENTER, width=60)
    my_game.column("Starting_Number", anchor=CENTER, width=60)
    my_game.column("Name", anchor=CENTER, width=70)
    my_game.column("Surname", anchor=CENTER, width=70)
    my_game.column("Rating", anchor=CENTER, width=50)
    my_game.column("Points", anchor=CENTER, width=50)
    my_game.column("SOS", anchor=CENTER, width=50)
    my_game.column("SOSOS", anchor=CENTER, width=50)
    my_game.column("SODOS", anchor=CENTER, width=50)
    my_game.column("Opponents", anchor=CENTER, width=260)

    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("Standing", text="Standing", anchor=CENTER)
    my_game.heading("Starting_Number", text="Start Num", anchor=CENTER)
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
    my_game.grid(column=1, row=1, rowspan=5)
    left_label = Label(text=f"Rounds: {rounds} \nPlayers: {len(tournament_list.list_of_players)}")
    left_label.grid(column=0, row=1)


# START

tournament_list = PlayerList()
rounds = 0
tournament_started = False

# COMMANDS AND GUI ELEMENTS

def addp_add():
    if rating_entry.get().isdigit() and int(rating_entry.get()) < 3000:
        name = name_entry.get()
        surname = surname_entry.get()
        rating = int(rating_entry.get())
        tournament_list.add_player(name, surname, rating)
        addp.destroy()
        update()
    else:
        messagebox.showinfo(title="Ooops...", message="The rating of the player should be a number below 3000!")


def rmvp_rem():
    stn = int(stn_entry.get())
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
    srft.attributes('-topmost', 'true')
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
    rmvp.attributes('-topmost', 'true')
    rmvp.config(padx=50, pady=50)
    rmvp.title('Remove player')
    stn_label = Label(rmvp, text="Starting number:")
    stn_label.grid(column=0, row=0)

    global stn_entry
    stn_entry = Entry(rmvp, width=40)
    stn_entry.grid(column=1, row=0)

    addp_button = Button(rmvp, text="Remove player", width=20, command=rmvp_rem)
    addp_button.grid(column=0, row=1, columnspan=2)


def add_player_window():
    global addp
    addp = Toplevel(window)
    addp.attributes('-topmost', 'true')
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


current_pairing = []
is_round_robin = False


def start_tournament():
    if rounds == 0:
        messagebox.showinfo(title="Ooops...",
                            message="The number of planned rounds is 0, please set a higher number of rounds!")
    else:
        if len(tournament_list.list_of_players) - rounds <= 0:
            messagebox.showinfo(title="Ooops...",
                                message="There is too many rounds for such number of players. Please set less rounds or add additional players!")
        else:
            global tournament_started
            tournament_started = True
            add_player_button.destroy()
            remove_player_button.destroy()
            start_tournament_button.destroy()
            set_rounds_button.destroy()
            global is_round_robin
            if len(tournament_list.list_of_players) - rounds == 1:
                is_round_robin = True
            if is_round_robin:
                tournament_type = "round robin"
            else:
                tournament_type = "swiss"
            messagebox.showinfo(title="Onegaishimasu!",
                                message=f"The tournament is ready to go. According to the number of players and rounds, it will be paired in a {tournament_type} system. Please enjoy your games!")
            global next_round_button
            next_round_button = Button(text="Next round", width=20, command=next_round)
            next_round_button.grid(column=0, row=2)
            next_round()


rr_pairing = []
round = 1


def next_round():
    global round
    global current_pairing
    global rr_pairing
    if is_round_robin:
        if round == 1:
            rr_pairing = round_robin_pairing(tournament_list)
        current_pairing = rr_pairing[round - 1]
    else:
        current_pairing = sp_pairing_for_next_round(tournament_list)
    set_results_window(current_pairing, tournament_list)
    round += 1


def export_results(playerlist):
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")
    rand = random.randint(10000, 99999)
    global filename
    filename = f"tournament_results_{rand}"
    with open(f'{filename}.txt', 'w') as r:
        r.write("[Tournament, City]\n")
        r.write(f"[{d1}]\n")
        a = 1
        for player in playerlist.list_of_players:
            ops = ""
            b = 0
            for op in player.opponents:
                if b == 1:
                    ops += " "
                b = 1
                searched_ind = op[:-1]
                ind = playerlist.find_player_by_starting_number(int(searched_ind))
                ops += str(ind + 1)
                ops += op[-1]
            r.write(f"{a} [{player.surname}] [{player.name}] [{ops}] {player.points}\n")
            a += 1


def exit_program():
    global exit
    exit = True


def reswin_input(pairlist):
    results_inputted = ""
    for pair in pairlist:
        results_inputted += str((pair.get()))
    if "0" in results_inputted:
        messagebox.showinfo(title="Ooops...",
                            message="It seems that not all results has been inputted. Please check it!")
        reswin.grab_set_global()
    else:
        resolve_round(current_pairing, tournament_list, results_inputted)
        reswin.destroy()
        if round > rounds:
            messagebox.showinfo(title="Arigato gozaimashita!", message="The tournament is completed!")
            next_round_button.destroy()
            exit_button = Button(text="Exit", width=20, command=exit_program)
            exit_button.grid(column=0, row=2)
            export_results(tournament_list)
            messagebox.showinfo(title="Results exported", message=f"Results has been exported to the {filename}.txt")
        update()


def set_results_window(pairs, playerlist):
    global reswin
    reswin = Toplevel(window)
    reswin.attributes('-topmost', 'true')
    reswin.config(padx=50, pady=50)
    reswin.title('Round results')
    reswin_label = Label(reswin, text="Please input results:")
    reswin_label.grid(row=0, column=0, columnspan=3)
    global pairlist
    pairlist = []
    a = 1
    for p in pairs:
        player_A = playerlist.list_of_players[playerlist.find_player_by_starting_number(p.player1)]
        player_B = playerlist.list_of_players[playerlist.find_player_by_starting_number(p.player2)]
        board_label = Label(reswin, text=f"Board {a}:").grid(row=a, column=0)
        winner = IntVar()
        pA = Radiobutton(reswin, text=f"{player_A.name} {player_A.surname}", variable=winner, value=1).grid(row=a, column=1)
        pB = Radiobutton(reswin, text=f"{player_B.name} {player_B.surname}", variable=winner, value=2).grid(row=a, column=2)
        pairlist.append(winner)
        a += 1
    reswin_button = Button(reswin, text="Input results", width=20, command=lambda: reswin_input(pairlist))
    reswin_button.grid(row=a + 1, column=1)


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
