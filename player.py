from tkinter import *
from data import *

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

#2D Board List
board_list = []
#2D list for gameboard
for i in range(Board_Size + 1):
    board_list.append([0] * (Board_Size + 1))

class Player(Entry,Button):

    def __init__(self):
        super().__init__()
        self.turn = 1
        self.turn_fill = "white"
        self.name_person = ""
        #self.name_person2 = ""
        self.type_person = ""
        self.entry_name = Entry(width = 15)
        #self.entry_name2 = Entry(width = 15)
        
        self.X = None
        self.Y = None

    def Player_turn(self,canvas):

        Click_Cord = [None, None]

        #Click Detection Cord
        Game_CordX = []
        Game_CordY = []
        Actual_CordX1 = []
        Actual_CordY1 = []
        Actual_CordX2 = []
        Actual_CordY2 = []
        

        def Value_Check_int(Value):
            try:
                Value = int(Value)
            except ValueError:
                return "string"
            else:
                return "int"

        def MouseClick(event):
            #global Click_Cord
            X_click = event.x
            Y_click = event.y
            Click_Cord = Piece_Location(X_click, Y_click)
            print(Click_Cord)
            self.X = Click_Cord[0]
            self.Y = Click_Cord[1]

            # if self.turn % 2 == 1:
            #     self.turn_fill = "red"
            # else:
            #     self.turn_fill = "green"
            
            #Create_piece(Board_X1 + Board_GapX * (self.X - 1), Board_Y1 + Board_GapY * (self.Y - 1),fill = self.turn_fill)
            #print(self.turn_fill)
            #self.turn += 1


        canvas.bind("<Button-1>", MouseClick)
        
        def Piece_Location(X_click, Y_click):    
            self.X = None
            self.Y = None
            for i in range(len(Actual_CordX1)):
        
                if X_click > Actual_CordX1[i] and X_click < Actual_CordX2[i]:
                    self.X = Game_CordX[i]

                if Y_click > Actual_CordY1[i] and Y_click < Actual_CordY2[i]:
                    self.Y = Game_CordY[i]

            return self.X, self.Y

        for z in range(1, Board_Size + 2):
            for i in range(1, Board_Size + 2):
                Game_CordX.append(z)
                Game_CordY.append(i)
                Actual_CordX1.append((z - 1) * Board_GapX + Board_X1 - Chess_Radius)
                Actual_CordY1.append((i - 1) * Board_GapY + Board_Y1 - Chess_Radius)
                Actual_CordX2.append((z - 1) * Board_GapX + Board_X1 + Chess_Radius)
                Actual_CordY2.append((i - 1) * Board_GapY + Board_Y1 + Chess_Radius)

        canvas.update()

        if self.X == None or self.Y == None:
                return False
        
        elif board_list[self.Y - 1][self.X - 1] == 0:
            return True
    
    def Location_Validation(self):
        pass
            # X_click = event.x
            # Y_click = event.y
            # Click_Cord = Piece_Location(X_click, Y_click)
            # print(Click_Cord)
            # self.X = Click_Cord[0]
            # self.Y = Click_Cord[1]

            # if self.X == None or self.Y == None:
            #     return False
        
            # elif board_list[self.Y - 1][self.X - 1] == 0:
            #     return True

                
        

        
