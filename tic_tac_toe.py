import tkinter as tk
import random
from tkinter import messagebox


def check_win(buttons):
    """Checks for a win condition in the Tic-Tac-Toe game."""
    win_conditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],  # horizontal
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],  # vertical
        [0, 4, 8],
        [2, 4, 6],  # diagonal
    ]
    for condition in win_conditions:
        if (
            buttons[condition[0]]["text"]
            == buttons[condition[1]]["text"]
            == buttons[condition[2]]["text"]
            != ""
        ):
            return buttons[condition[0]]["text"]
    return None


def disable_buttons(buttons):
    """Disables all buttons on the game board."""
    for button in buttons:
        button["state"] = "disabled"


def new_game():
    """Starts a new Tic-Tac-Toe game."""
    global current_player
    current_player = random.choice(["X", "O"])
    for button in buttons:
        button["text"] = ""
        button["state"] = "normal"
        button["bg"] = "white"  # Reset button color


def click(button):
    """Handles a button click in the Tic-Tac-Toe game."""
    global current_player
    button["text"] = current_player
    button["state"] = "disabled"

    winner = check_win(buttons)
    if winner:
        messagebox.showinfo("Winner!", f"Player {winner} wins!")
        for i in range(9):
            if buttons[i]["text"] == winner:
                buttons[i]["bg"] = "green"
        disable_buttons(buttons)
    elif all(button["state"] == "disabled" for button in buttons):
        messagebox.showinfo("Tie!", "The game is a tie!")  # Display a tie message
        disable_buttons(buttons)  # Disable buttons after tie
    else:
        current_player = "O" if current_player == "X" else "X"


root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = []
for i in range(9):
    button = tk.Button(
        root,
        text="",
        width=6,
        height=2,
        font=("Arial", 20),
        command=lambda b=i: click(buttons[b]),
    )
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

new_game_button = tk.Button(root, text="New Game", command=new_game)
new_game_button.grid(row=3, column=0, columnspan=3)

new_game()

root.mainloop()
