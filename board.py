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

class Board(Tk,Canvas,Label):

    def __init__(self):
        super().__init__()
        self.turn_num = 1

        #self.myInterface = Tk()
        self.minsize(Size_window_width,Size_window_height)
        self.canvas = Canvas(self, width=width, height=height, background= "#b69b4c")
        self.canvas.pack()

        #self.player1 = Player()
        #self.player1.entry_name.grid(column=1,row=0)
        #self.player2 = Player()
        #self.player2.entry_name.grid(column=2,row=0)

        #self.mainloop()
        #Buttons
        self.B = Button(self, text = "EXIT", font = "Helvetica 10 bold", command = self.Exit, bg = "gray", fg = "black",highlightthickness=0)
        self.B.pack()
        self.B.place(x = width / 2 * 0.5, y = height - Frame_Gap * 1.6 + 15, height = Chess_Radius * 4, width = Chess_Radius * 6)
        self.N = Button(self,text = "NEW", font = "Helvetica 10 bold", command = self.New,fg = "black",highlightthickness=0)
        self.N.pack()
        self.N.place(x = width / 2 * 0.5-Chess_Radius * 6, y = height - Frame_Gap * 1.6 + 15, height = Chess_Radius * 4, width = Chess_Radius * 6)
    def Create_board(self):
        self.canvas.create_rectangle(Board_X1 - Frame_Gap, Board_Y1 - Frame_Gap, Board_X1 + Frame_Gap + Board_GapX * Board_Size, Board_Y1 + Frame_Gap + Board_GapY * Board_Size, width = 3)

        for f in range(Board_Size + 1):
            self.canvas.create_line(Board_X1, Board_Y1 + f * Board_GapY, Board_X1 + Board_GapX * Board_Size, Board_Y1 + f * Board_GapY)
            self.canvas.create_line(Board_X1 + f * Board_GapX, Board_Y1, Board_X1 + f * Board_GapX, Board_Y1 + Board_GapY * Board_Size)

            self.canvas.create_text(Board_X1 - Frame_Gap * 1.7, Board_Y1 + f * Board_GapY, text = f + 1, font = "Helvetica 10 bold", fill = "black")
            self.canvas.create_text(Board_X1 + f * Board_GapX, Board_Y1 - Frame_Gap * 1.7, text = f + 1, font = "Helvetica 10 bold", fill = "black")
    
    def Create_piece(self,x, y, radius = Chess_Radius, fill = "white", outline = "black", width = 0.5):
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill = fill, outline = outline, width = width)

    def Player(self):
        pass
    def Exit(self):
        global Winner
        Winner = "Exit"
        self.destroy()
    def New(delf):
        pass
        
