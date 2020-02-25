from tkinter import *
from tkinter import ttk  # provide combo box
from PIL import ImageTk
from tkinter import messagebox


class tic_tac_toe:
    def __init__(self,window):
        self.window = window
        self.window.title("Tic Tak Toe")
        self.window.geometry("500x700")

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

        # -------- Manage Board ----------------------------------
        self.board = [["","",""],["","",""],["","",""]]

        # player buttons------
        self.stepsCount = 0
        self.buttons_()
        #  Variables --------

    def buttons_(self): # todo

        # 00
        self.btn_00 = Button(window,bg ="white",command = self.changeImage('00'), text="Registration", width=10)
        self.btn_00.place(x=76,y=360,width=80,height=80)

        # 01
        self.btn_01 = Button(window,bg ="white", text="Registration", width=10)
        self.btn_01.place(x=176, y=360, width=120, height=80)

        # 02
        self.btn_02 = Button(window, text="Registration", width=10)
        self.btn_02.place(x=320, y=360, width=80, height=80)

        # 10
        self.btn_10 = Button(window, text="Registration", width=10)
        self.btn_10.place(x=76, y=460, width=80, height=95)

        # 11
        self.btn_11 = Button(window, text="Registration", width=10)
        self.btn_11.place(x=176, y=460, width=120, height=95)

        # 12
        self.btn_12 = Button(window, text="Registration", width=10)
        self.btn_12.place(x=320, y=460, width=80, height=95)

        # 20
        self.btn_20 = Button(window, text="Registration", width=10)
        self.btn_20.place(x=76, y=575, width=80, height=80)

        # 21
        self.btn_21 = Button(window, text="Registration", width=10)
        self.btn_21.place(x=176, y=575, width=120, height=80)

        # 22
        self.btn_22 = Button(window, text="Registration", width=10)
        self.btn_22.place(x=320, y=575, width=80, height=80)


    def changeImage(self,hj):
        '''if (self.stepsCount < 9) :
            self.stepsCount += 1
            if self.stepsCount % 2 == 0:
                # if odd then O
                img.configure(image=self.o_image)

            else:
                # if odd then X
                img.configure(image=self.x_image)


        else:
            # print game over
            messagebox.showinfo("Game Over")'''
        print("Clicked")
        print(hj)
        print(self)



window = Tk()
obj = tic_tac_toe(window)
window.mainloop()
