#1
import tkinter as tk
import random
#3
from itertools import cycle
from tkinter import font
#2
from typing import NamedTuple
#Tic-Tac-Toe By Python
#Program to create the tictactoe board


class TicTacToeGame:
    def __init__(self,players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self.players
        self.board_size = board_size
        self.current_player = next(self.players)
        self.winner_combo = []
        self._current_moves = []
        self._has_winner = False
        self._winning_combos = []
        self._setup_board()


class TicTacToeBoard(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe Game");
        self.cells = {}
        self.create_board_display()
        self.create_board_grid()
        
    def create_board_display(self):
        fill_frame = tk.Frame(master=self)
        fill_frame.pack(tk.X)
        self.display = tk.Label( master = display_frame, text = "Ready?", font = font.Font(size=28,weight="Bold"))
    self.display.pack()

    def create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        for r in range(3):
            self.rowconfigure(r,weight=80,minsize=75)
            self.columnconfigure(c,weight=80,minsize=75)
            for c in range(3):
                button = tk.Button(master=grid_frame)
                self.grid(r=row, c=column, padx=5, pady=5, sticky='nsew')
                

    
    
class Player(NamedTuple):
    label:str
    color:str


class Move(NamedTuple):
    row:int
    col:int
    label: str = ""




        
def main():
    board = TicTacToeBoard()
    board.mainloop()
    if __name__ == "__main__":
        main()
    
