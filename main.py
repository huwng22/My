from tkinter import *
from board import *
from player import *

board = Board()

player1 = Player()
player1.pack()

#board.Create_board()
#while True:
    #board.Player_turn()
board.Create_board()
player1.turn = 2

player1.Player_turn(board.canvas,board.Create_piece)

board.mainloop()