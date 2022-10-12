import tkinter as tk
import tkinter.messagebox as tm
import random

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("300x300")
        self.resizable(0, 0)
        self.buttons = []
        self.turn = 0
        self.player = "X"
        self.computer = "O"
        self.game_over = False
        self.create_buttons()
        self.create_menu()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self, text=" ", width=5, height=2, command=lambda row=i, column=j: self.button_clicked(row, column))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def create_menu(self):
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New Game", command=self.new_game)
        filemenu.add_command(label="Quit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.config(menu=menubar)

    def new_game(self):
        self.turn = 0
        self.player = "X"
        self.computer = "O"
        self.game_over = False
        for button in self.buttons:
            button.config(text=" ")

    def button_clicked(self, row, column):
        if self.game_over:
            return
        if self.turn % 2 == 0:
            self.buttons[row * 3 + column].config(text=self.player)
            self.turn += 1
            self.check_win(self.player)
            self.computer_turn()
        else:
            tm.showinfo("Error", "It's not your turn")

    def computer_turn(self):
        if self.game_over:
            return
        if self.turn % 2 == 1:
            self.turn += 1
            self.check_win(self.computer)
            self.computer_turn()
        else:
            self.turn += 1
            self.check_win(self.player)
            self.computer_turn()

    def check_win(self, player):
        if self.buttons[0].cget("text") == player and self.buttons[1].cget("text") == player and self.buttons[2].cget("text") == player:
            self.game_over = True
            tm.showinfo("Winner", player + " wins!")
        elif self.buttons[3].cget("text") == player and self.buttons[4].cget("text") == player and self.buttons[5].cget("text") == player:
            self.game_over = True
            tm.showinfo("Winner", player + " wins!")
        elif self.buttons[6].cget("text") == player and self.buttons[7].cget("text") == player and self.buttons[8].cget("text") == player:
            self.game_over = True
            tm.showinfo("Winner", player + " wins!")
        elif self.buttons[0].cget("text") == player and self.buttons[3].cget("text") == player and self.buttons[6].cget("text") == player:
            self.game_over = True
            tm.showinfo("Winner", player + " wins!")
        elif self.buttons[1].cget("text") == player and self.buttons[4].cget("text") == player and self.buttons[7].cget("text") == player:
            self.game_over = True
            tm.showinfo("Winner", player + " wins!")
        elif self.buttons[2].cget("text") == player and self.buttons[5].cget("text") == player and self.buttons[8].cget("text") == player:
            self.game_over = True
            tm.showinfo("Winner", player + " wins!")
        elif self.buttons[0].cget("text") == player and self.buttons[4].cget("text") == player and self.buttons[8].cget("text") == player:
            self.game_over = True
            tm.showinfo("Winner", player + " wins!")
        elif self.buttons[2].cget("text") == player and self.buttons[4].cget("text") == player and self.buttons[6].cget("text") == player:
            self.game_over = True
            tm.showinfo("Winner", player + " wins!")
        elif self.turn == 9:
            self.game_over = True
            tm.showinfo("Tie", "It's a tie!")

if __name__ == "__main__":
    root = TicTacToe()
    root.mainloop()