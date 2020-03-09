from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


class tic_tac_toe:
    def __init__(self,window):
        self.window = window
        self.window.title("Tic Tak Toe")
        self.window.geometry("500x700")
        self.window.resizable(0,0)

        # setting background image
        self.bg_image = ImageTk.PhotoImage(file="Images/bg_image.jpg")
        self.x_image = ImageTk.PhotoImage(file="Images/x_image.png")
        self.o_image = ImageTk.PhotoImage(file="Images/o_image.png" )


        self.bg_image_lable = Label(window,image=self.bg_image)
        self.bg_image_lable.place(relx=0,rely=0)

        # Lables
        title = Label(self.window, text="Tic Tac Toe", font=("times new roman", 40, "bold"),
                      bg="yellow", fg="red", bd=10, relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)  # relwidth =1 --> set relative width according to window


        self.palyer_o_points = 0
        self.palyer_x_points = 0



        # player buttons------
        self.newBoard()

    def newBoard(self):
        # -------- Manage Board ----------------------------------
        self.board = []
        self.numaricBoard = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.stepsCount = 0

        # player x points lable
        self.palyer_x_points_lable = Label(self.window, font=("times new roman", 40, "bold"), text=self.palyer_x_points,
                                           bg="white", fg="black", bd=0, relief=GROOVE)
        self.palyer_x_points_lable.place(x=170, y=210, width=70, height=70)

        # player o points lable
        self.palyer_x_points_lable = Label(self.window, font=("times new roman", 40, "bold"), text=self.palyer_o_points,
                                           bg="white", fg="black",bd=0, relief=GROOVE)
        self.palyer_x_points_lable.place(x=410, y=210, width=70, height=70)


        self.buttons_()

    def buttons_(self): # todo

        # 00
        self.btn_00 = Button(window,bg ="white",command=lambda:self.changeImage('00'), width=10)
        self.btn_00.place(x=76,y=360,width=80,height=80)

        # 01
        self.btn_01 = Button(window,bg ="white",command=lambda:self.changeImage('01'), width=10)
        self.btn_01.place(x=176, y=360, width=120, height=80)

        # 02
        self.btn_02 = Button(window,bg ="white",command=lambda:self.changeImage('02'), width=10)
        self.btn_02.place(x=320, y=360, width=80, height=80)

        # 10
        self.btn_10 = Button(window,bg ="white",command=lambda:self.changeImage('10'), width=10)
        self.btn_10.place(x=76, y=460, width=80, height=95)

        # 11
        self.btn_11 = Button(window,bg ="white",command=lambda:self.changeImage('11'), width=10)
        self.btn_11.place(x=176, y=460, width=120, height=95)

        # 12
        self.btn_12 = Button(window,bg ="white",command=lambda:self.changeImage('12'), width=10)
        self.btn_12.place(x=320, y=460, width=80, height=95)

        # 20
        self.btn_20 = Button(window,bg ="white",command=lambda:self.changeImage('20'), width=10)
        self.btn_20.place(x=76, y=575, width=80, height=80)

        # 21
        self.btn_21 = Button(window,bg ="white",command=lambda:self.changeImage('21'), width=10)
        self.btn_21.place(x=176, y=575, width=120, height=80)

        # 22
        self.btn_22 = Button(window,bg ="white",command=lambda:self.changeImage('22'), width=10)
        self.btn_22.place(x=320, y=575, width=80, height=80)


    def changeImage(self,position):
        if (self.stepsCount < 8) :
            self.selectImage(position)

        else:
            # print game over
            messagebox.showinfo("Winner","Match Is Draw \n Both Players Are Equal")
            self.newBoard()



    def selectImage(self,position):
        if position not in self.board:
            positionCode = [int(position[0]), int(position[1])]

            if self.stepsCount % 2 == 0:
                image_type = self.o_image
                self.numaricBoard[positionCode[0]][positionCode[1]] = "o"
                player = "O"

            else:
                image_type = self.x_image
                self.numaricBoard[positionCode[0]][positionCode[1]] = "x"
                player = "X"


            if position == "00":
                self.btn_00.configure(image=image_type)

            elif position == "01":
                self.btn_01.configure(image=image_type)

            elif position == "02":
                self.btn_02.configure(image=image_type)

            elif position == "10":
                self.btn_10.configure(image=image_type)

            elif position == "11":
                self.btn_11.configure(image=image_type)

            elif position == "12":
                self.btn_12.configure(image=image_type)

            elif position == "20":
                self.btn_20.configure(image=image_type)

            elif position == "21":
                self.btn_21.configure(image=image_type)

            elif position == "22":
                self.btn_22.configure(image=image_type)

            # setting board
            self.stepsCount += 1
            self.board.append(position)
            self.gameWinning(player)


    def gameWinning(self,player): #todo
        win = False
        #print(self.numaricBoard)
        for i in range(3):
            if (self.numaricBoard[i][0] == self.numaricBoard[i][1] == self.numaricBoard[i][2] and self.numaricBoard[i][1] != "") or (self.numaricBoard[0][i] == self.numaricBoard[1][i] == self.numaricBoard[2][i] and self.numaricBoard[1][i] != ""):
                win = True

        if (self.numaricBoard[0][0] == self.numaricBoard[1][1] == self.numaricBoard[2][2]) or (self.numaricBoard[0][2] == self.numaricBoard[1][1] == self.numaricBoard[2][0] and (self.numaricBoard[1][1]!="")):
            if self.numaricBoard[1][1] != "":
                win = True

        if win == True:
            # print game win
            if player == "X":
                self.palyer_x_points+=1
            if player == "O":
                self.palyer_o_points+=1

            messagebox.showinfo("Winner", "Player {} \n Wins The Match".format(player))
            self.newBoard()




window = Tk()
obj = tic_tac_toe(window)
window.mainloop()
