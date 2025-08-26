import tkinter as tk
import random
from tkinter import font
#Tic-Tac-Toe By Python
#Program to create the tictactoe board
class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe Game");
        self.cells = {}
        
    def create_board_display(self):
        fill_frame = tk.Frame(master=self)
        fill_frame.pack(tk.X)
        self.display = tk.Label( master = display_frame, text = "Ready?", font = tk.font.Font(size=28,weight="Bold"))

    self.display.pack()

    def create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        '''r = int(input("Enter the number of rows:"))
        c = int(input("ENter the number of columns:"))
        if r.isnull():
            alt_r = 3
        elif c.isnull():
            alt_c = 3'''
        for r in range(3):
            self.rowconfigure(r,weight=80,minsize=75)
            self.columnconfigure(c,weight=80,minsize=75)
            for c in range(3):
                button = tk.Button(master=grid_frame)
                self.grid(r=row, c=column, padx=5, pady=5, sticky='nsew')
            
                                 
