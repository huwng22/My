from tkinter import *
from test2 import *

#Board Size
Size_window_width = 1200
Size_window_height = 1000
Board_Size = 15
Frame_Gap = 35
width = 1000
height = 1000

#Board
Board_Size = Board_Size - 1
Board_X1 = width / 10
Board_Y1 = height / 10
Board_GapX = (width - Board_X1 * 2) / Board_Size
Board_GapY = (height - Board_Y1 * 2) / Board_Size

#Chess Piece
Chess_Radius = (Board_GapX * (9 / 10)) / 4

class Data:
    def __init__(self):
def Score_Board():
    if Winner == None:
        Turn_Text = s.create_text(width / 2, height - Frame_Gap + 15, text = "Turn = " + Turn, font = "Helvetica 25 bold", fill = Turn)
        return Turn_Text
    else:
        s.create_text(width / 2, height - Frame_Gap + 15, text = Winner.upper() + " WINS!", font = "Helvetica 25 bold", fill = Winner.lower())

def winCheck(Piece_Number, Piece_Colour, board):
    if rowCheck(Piece_Number, board) or rowCheck(Piece_Number, transpose(board)) or rowCheck(Piece_Number, transposeDiagonalInc(board)) or rowCheck(Piece_Number, transposeDiagonalDec(board)):
        Winner = Piece_Colour
        return Winner

def rowCheck(Piece_Number, board):
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

def getDiagonalDec(loa, digNum):
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


def transposeDiagonalDec(loa):
    lst = []
    for i in range(len(loa) * 2 - 1):
        lst.append(getDiagonalDec(loa, i))
    return lst

def getDiagonalInc(loa, digNum):
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


def transposeDiagonalInc(loa):
    lst = []
    for i in range(len(loa) * 2 - 1):
        lst.append(getDiagonalInc(loa, i))
    return lst

def transpose(loa):
    lst = []
    for i in range(len(loa)):
        lst.append(getCol(loa, i))
    return lst
    
def getCol(loa, colNum):
    lst = []
    for i in range(len(loa)):
        lst.append(loa[i][colNum])
    return lst

def Index2D_Cord(List, Find):
    for i, x in enumerate(List):
        if Find in x:
            Colour_CordX.append(i - 1)
            Colour_CordY.append(x.index(Find) - 1)

def Exit():
    global Winner
    Winner = "Exit"
    myInterface.destroy()