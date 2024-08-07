import tkinter as tk
import random
from tkmacosx import Button

playerO = "O"
playerX = "X"

curr_player = playerX
game_over = False
turns = 0
score_X = 0
score_O = 0

color_yellow = "#FFD700"
color_light_gray = "#D3D3D3"
color_blue = "#00BFFF"
color_red = "#FF4500"
color_green = "#32CD32"
color_dark = "#000000"
color_tile = "#011111"
color_white = "#ffffff"

root = tk.Tk()
root.title("Tic Tac Toe")
root.configure(bg=color_dark)
root.resizable(width=False, height=True)


def set_tile(row, column):
    global curr_player, game_over

    if game_over or board[row][column]["text"] != "":
        return

    board[row][column]["text"] = curr_player
    board[row][column]["fg"] = color_blue if curr_player == playerX else color_red

    check_winner()

    curr_player = playerO if curr_player == playerX else playerX
    label["text"] = f"{curr_player}'s Turn" if not game_over else label["text"]


def check_winner():
    global turns, game_over, score_X, score_O
    turns += 1

    for row in range(3):
        if board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] and board[row][0]["text"] != "":
            highlight_winner(row, 0, row, 1, row, 2)
            game_over = True
            update_score(board[row][0]["text"])
            return

    for column in range(3):
        if board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] and board[0][column]["text"] != "":
            highlight_winner(0, column, 1, column, 2, column)
            game_over = True
            update_score(board[0][column]["text"])
            return

    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] and board[0][0]["text"] != "":
        highlight_winner(0, 0, 1, 1, 2, 2)
        game_over = True
        update_score(board[0][0]["text"])
        return

    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] and board[0][2]["text"] != "":
        highlight_winner(0, 2, 1, 1, 2, 0)
        game_over = True
        update_score(board[0][2]["text"])
        return

    if turns == 9:
        label.config(text="It's a Draw!", fg=color_green)
        game_over = True


def highlight_winner(r1, c1, r2, c2, r3, c3):
    for (r, c) in [(r1, c1), (r2, c2), (r3, c3)]:
        board[r][c].config(fg=color_yellow, bg=color_light_gray)
    label.config(text=f"{board[r1][c1]['text']} Wins!", fg=color_yellow)


def update_score(winner):
    global score_X, score_O
    if winner == playerX:
        score_X += 1
    else:
        score_O += 1
    score_label.config(text=f"Score - X: {score_X}  O: {score_O}")


def reset_game():
    global game_over, turns, curr_player
    game_over = False
    turns = 0
    curr_player = random.choice([playerX, playerO])
    label.config(text=f"{curr_player}'s Turn", fg=color_blue)

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", fg=color_white, bg=color_dark)


board = [[None for _ in range(3)] for _ in range(3)]

for row in range(3):
    for column in range(3):
        button = Button(root, text="", font=("Consolas", 36, "bold"), width=150, height=150, bg=color_tile,
            fg='#5F4B8B', borderless=1,
            activebackground=('#AE0E36', '#D32E5E'),
            activeforeground='#E69A8D', command= lambda r=row, c=column: set_tile(r, c))

        button.grid(row=row, column=column, padx=5, pady=5)
        board[row][column] = button

label = tk.Label(root, text=f"{curr_player}'s Turn", font=("Consolas", 20, "bold"), bg=color_dark, fg=color_white)
label.grid(row=3, column=0, columnspan=3, pady=(10, 0))

score_label = tk.Label(root, text=f"Score - X: {score_X}  O: {score_O}", font=("Consolas", 16, "bold"), bg=color_dark, fg=color_white)
score_label.grid(row=4, column=0, columnspan=3)

reset_button = tk.Button(root, text="Reset Game", font=("Consolas", 16, "bold"), command=reset_game, bg=color_light_gray)
reset_button.grid(row=5, column=0, columnspan=3, pady=10)

root.update()

window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

root.mainloop()
