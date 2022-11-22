from tkinter import *
from test1 import *
from test2 import *
from data import *

Unfilled = 0
Black_Piece = 1
White_Piece = 2

board = Board()

player1 = Player()
player1.pack()

data = Data()

board.Create_board()
player1.turn = 1

Turn_Text = data.Score_Board(board.canvas,player1.turn_fill)

# player1.turn_fill = player1.entry_name.get()
# if player1.turn_fill == "white":
#     player1.turn = 1
# elif player1.turn_fill == "black":
#     player1.turn = 2

while Winner == None:
    
    board.update()

    Picked = player1.Player_turn(board.canvas)

    if Picked:
        board.canvas.delete(Turn_Text)
        board.Create_piece(Board_X1 + Board_GapX * (player1.X - 1), Board_Y1 + Board_GapY * (player1.Y - 1),fill = player1.turn_fill)

        if player1.turn % 2 == 1:
            White_Cord_PickedX.append(player1.X)
            White_Cord_PickedY.append(player1.Y)
            board_list[player1.Y - 1][player1.X - 1] = 2
            player1.turn_fill = "black"

        elif player1.turn % 2 == 0:
            Black_Cord_PickedX.append(player1.X)
            Black_Cord_PickedY.append(player1.Y)
            board_list[player1.Y - 1][player1.X - 1] = 1
            player1.turn_fill = "white"

        Turn_Text = data.Score_Board(board.canvas,player1.turn_fill)

        player1.turn = player1.turn + 1

        if player1.turn_fill == "white":
            Colour_Check = Black_Piece
            Win_Check = "black"

        else:
            Colour_Check = White_Piece
            Win_Check = "white"

        Winner = data.winCheck(Colour_Check, Win_Check, board_list)
        
board.canvas.delete(Turn_Text)
if Winner != "Exit":
    data.Score_Board(board.canvas,player1.turn_fill)
    board.Exit()
    
board.mainloop()
