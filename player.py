from tkinter import *

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

#Turn


class Player(Entry,Button):

    def __init__(self):
        super().__init__()
        self.turn = 1
        self.turn_fill = ""
        self.name_person = ""
        #self.name_person2 = ""
        self.type_person = ""
        self.entry_name = Entry(width = 15)
        #self.entry_name2 = Entry(width = 15)


    def Player_turn(self,canvas,Create_piece):

        Click_Cord = [None, None]

        #Click Detection Cord
        Game_CordX = []
        Game_CordY = []
        Actual_CordX1 = []
        Actual_CordY1 = []
        Actual_CordX2 = []
        Actual_CordY2 = []
        #2D Board List
        board = []

        def Value_Check_int(Value):
            try:
                Value = int(Value)
            except ValueError:
                return "string"
            else:
                return "int"

        def MouseClick(event):
            global Click_Cord
            def Value_Check_int(Value):
                try:
                    Value = int(Value)
                except ValueError:
                    return "string"
                else:
                    return "int"

            X_click = event.x
            Y_click = event.y
            Click_Cord = Piece_Location(X_click, Y_click)
            print(Click_Cord)
            X = Click_Cord[0]
            Y = Click_Cord[1]

            if self.turn % 2 == 1:
                self.turn_fill = "red"
            else:
                self.turn_fill = "green"
            
            Create_piece(Board_X1 + Board_GapX * (X - 1), Board_Y1 + Board_GapY * (Y - 1),fill = self.turn_fill)
            print(self.turn_fill)
            self.turn += 1


        canvas.bind("<Button-1>", MouseClick)
        
        def Piece_Location(X_click, Y_click):    
            X = None
            Y = None
            for i in range(len(Actual_CordX1)):
        
                if X_click > Actual_CordX1[i] and X_click < Actual_CordX2[i]:
                    X = Game_CordX[i]

                if Y_click > Actual_CordY1[i] and Y_click < Actual_CordY2[i]:
                    Y = Game_CordY[i]

            return X, Y

        def Location_Validation():

            if X == None or Y == None:
                return False
        
            elif board[Y - 1][X - 1] == 0:
                return True

        for z in range(1, Board_Size + 2):
            for i in range(1, Board_Size + 2):
                Game_CordX.append(z)
                Game_CordY.append(i)
                Actual_CordX1.append((z - 1) * Board_GapX + Board_X1 - Chess_Radius)
                Actual_CordY1.append((i - 1) * Board_GapY + Board_Y1 - Chess_Radius)
                Actual_CordX2.append((z - 1) * Board_GapX + Board_X1 + Chess_Radius)
                Actual_CordY2.append((i - 1) * Board_GapY + Board_Y1 + Chess_Radius)

        canvas.update()

                
        

        
