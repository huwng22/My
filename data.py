from tkinter import *
from test2 import *

#Board Size
Size_window_width = 800
Size_window_height = 800
Board_Size = 15
Frame_Gap = 35
width = 800
height = 800

#Board
Board_Size = Board_Size - 1
Board_X1 = width / 10
Board_Y1 = height / 10
Board_GapX = (width - Board_X1 * 2) / Board_Size
Board_GapY = (height - Board_Y1 * 2) / Board_Size

#Chess Piece
Chess_Radius = (Board_GapX * (9 / 10)) / 4

Black_Cord_PickedX = []
Black_Cord_PickedY = []
White_Cord_PickedX = []
White_Cord_PickedY = []

Colour_CordX = []
Colour_CordY = []

Unfilled = 0
Black_Piece = 1
White_Piece = 2

Winner = None

class Data:
    def __init__(self):
        pass
    def Score_Board(self, canvas,Turn):

        if Winner == None:
            Turn_Text = canvas.create_text(width / 2, height - Frame_Gap + 15, text = "Turn = " + Turn, font = "Helvetica 25 bold", fill = Turn)
            return Turn_Text
        else:
            canvas.create_text(width / 2, height - Frame_Gap + 15, text = Winner.upper() + " WINS!", font = "Helvetica 25 bold", fill = Winner.lower())

    def winCheck(self, Piece_Number, Piece_Colour, board):
        if self.rowCheck(Piece_Number, board) or self.rowCheck(Piece_Number, self.transpose(board)) or self.rowCheck(Piece_Number, self.transposeDiagonalInc(board)) or self.rowCheck(Piece_Number, self.transposeDiagonalDec(board)):
            Winner = Piece_Colour
            return Winner

    def rowCheck(self, Piece_Number, board):
        for i in range(len(board)):
            if board[i].count(Piece_Number) >= 5:
            
                for z in range(len(board) - 3):
                    Connection = 0

                    for c in range(5):
                        if board[i][z + c] == Piece_Number:
                            Connection += 1

                        else:
                            break

                        if Connection == 5:
                            return True

    def getDiagonalDec(self, loa, digNum):
        lst=[]
        if digNum <= len(loa) - 1:
            index = len(loa) - 1
            for i in range(digNum, -1, -1):
                lst.append(loa[i][index])
                index -= 1
            return lst
        else:
            index = (len(loa) * 2 - 2) - digNum
            for i in range(len(loa) - 1, digNum - len(loa), -1):
                lst.append(loa[i][index])
                index -= 1
            return lst


    def transposeDiagonalDec(self, loa):
        lst = []
        for i in range(len(loa) * 2 - 1):
            lst.append(self.getDiagonalDec(loa, i))
            return lst

    def getDiagonalInc(self, loa, digNum):
        lst=[]
        if digNum <= len(loa) - 1:
            index = 0
            for i in range(digNum, -1, -1):
                lst.append(loa[i][index])
                index += 1
            return lst
        else:
            index =  digNum - len(loa) + 1
            for i in range(len(loa) - 1, digNum - len(loa), -1):
                lst.append(loa[i][index])
                index += 1
            return lst


    def transposeDiagonalInc(self, loa):
        lst = []
        for i in range(len(loa) * 2 - 1):
            lst.append(self.getDiagonalInc(loa, i))
        return lst

    def transpose(self, loa):
        lst = []
        for i in range(len(loa)):
            lst.append(self.getCol(loa, i))
        return lst
    
    def getCol(self, loa, colNum):
        lst = []
        for i in range(len(loa)):
            lst.append(loa[i][colNum])
        return lst

    def ndex2D_ICord(self, List, Find):
        for i, x in enumerate(List):
            if Find in x:
                Colour_CordX.append(i - 1)
                Colour_CordY.append(x.index(Find) - 1)
