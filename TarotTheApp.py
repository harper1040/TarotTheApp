from tkinter import *
import random
from PIL import Image, ImageTk
import os
import time

#Paths to the regular tarot card images and a flipped image of the same cards.
Path = 'C:/Users/Jack/PycharmProjects/untitled/Tarot/'
Path2 = "C:/Users/Jack/PycharmProjects/untitled/FlipTarot/"



#This dictionary is to provide the name of the card.
Tarot = {0 : "Fool", 1 : "The Magician", 2 : "The High Priestess", 3 : "The Empress", 4 : "The Emperor", 5 : "The Hierophant",
         6 : "The Lovers", 7 : "The Chariot", 8 : "Strength", 9 : "The Hermit", 10 : "Wheel Of Fortune", 11 : "Justice",
         12 : "The Hanged Man", 13 : "Death", 14 : "Temperance", 15 : "The Devil", 16 : "The Tower", 17 : "The Star",
         18 : "The Moon", 19 : "The Sun", 20 : "Judgement", 21 : "The World", 22 : "1 Swords", 23 : "2 Swords",
         24 : "3 Swords", 25 : "4 Swords", 26 : "5 Swords", 27 : "6 Swords", 28 : "7 Swords", 29 : "8 Swords",
         30 : "9 Swords", 31 : "10 Swords", 32 : "Page Swords", 33 : "Knight Swords", 34 : "Queen Swords",
         35 : "King Swords", 36 : "1 Wands", 37 : "2 Wands", 38 : "3 Wands", 39 : "4 Wands", 40 : "5 Wands", 41 : "6 Wands",
         42 : "7 Wands", 43 : "8 Wands", 44 : "9 Wands", 45 : "10 Wands", 46 : "Page Wands", 47 : "Knight Wands",
         48 : "Queen Wands", 49 : "King Wands", 50 : "1 Coins", 51 : "2 Coins", 52 : "3 Coins", 53 : "4 Coins",
         54 : "5 Coins", 55 : "6 Coins", 56 : "7 Coins", 57 : "8 Coins", 58 : "9 Coins", 59 : "10 Coins",
         60 : "Page Coins", 61 : "Knight Coins", 62 : "Queen Coins", 63 : "King Coins", 64 : "1 Cups", 65 : "2 Cups",
         66 : "3 Cups", 67 : "4 Cups", 68 : "5 Cups", 69 : "6 Cups", 70 : "7 Cups", 71 : "8 Cups", 72 : "9 Cups",
         73 : "10 Cups", 74 : "Page Cups", 75 : "Knight Cups", 76 : "Queen Cups", 77 : "King Cups"}

#This dictionary is to link to the card images.
FTarot = {0 : "A.jpg", 1 : "AB.jpg", 2 : "AC.jpg", 3 : "B.jpg", 4 : "BA.jpg", 5 : "BB.jpg", 6 : "C.jpg", 7 : "CA.jpg",
          8 : "CB.jpg", 9 : "D.jpg", 10 : "DA.jpg", 11 : "DB.jpg", 12 : "E.jpg", 13 : "EA.jpg", 14 : "EB.jpg",
          15 : "EC.jpg", 16 : "F.jpg", 17 : "FA.jpg", 18 : "FB.jpg", 19 : "G.jpg", 20 : "GA.jpg", 21 : "GB.jpg",
          22 : "H.jpg", 23 : "HA.jpg", 24 : "HB.jpg", 25 : "I.jpg", 26 : "IA.jpg", 27 : "IB.jpg", 28 : "J.jpg",
          29 : "JA.jpg", 30 : "JB.jpg", 31 : "K.jpg", 32 : "KA.jpg", 33 : "KB.jpg", 34 : "L.jpg", 35 : "LA.jpg",
          36 : "LB.jpg", 37 : "M.jpg", 38 : "MA.jpg", 39 : "MB.jpg", 40 : "N.jpg", 41 : "NA.jpg", 42 : "NB.jpg",
          43 : "O.jpg", 44 : "OA.jpg", 45 : "OB.jpg", 46 : "P.jpg", 47 : "PA.jpg", 48 : "PB.jpg", 49 : "Q.jpg",
          50 : "QA.jpg", 51 : "QB.jpg", 52 : "R.jpg", 53 : "RA.jpg", 54 : "RB.jpg", 55 : "S.jpg", 56 : "SA.jpg",
          57 : "SB.jpg", 58 : "T.jpg", 59 : "TA.jpg", 60 : "TB.jpg", 61 : "U.jpg", 62 : "UA.jpg", 63 : "UB.jpg",
          64 : "V.jpg", 65 : "VA.jpg", 66 : "VB.jpg", 67 : "W.jpg", 68 : "WA.jpg", 69 : "WB.jpg", 70 : "X.jpg",
          71 : "XA.jpg", 72 : "XB.jpg", 73 : "Y.jpg", 74 : "YA.jpg", 75 : "YB.jpg", 76 : "Z.jpg", 77 : "ZA.jpg", 78 : "ZAB.png", 79 : "zcloth2.jpg"}


Shuffle = 0
screen = True
texts = Shuffle - 1
Reg = []

#Clears text boxes and image labels.
def Clear():
    text0.config(state="normal")
    text0.delete(1.0, "end")
    text1.config(state="normal")
    text1.delete(1.0, "end")
    text2.config(state="normal")
    text2.delete(1.0, "end")

    label1.configure(image=ath)
    label1.image = ath
    label2.configure(image=ath)
    label2.image = ath
    label3.configure(image=ath)
    label3.image = ath

#Creates deck and shuffles it.
def Shuffled():
    global Shuffle
    global Reg
    Clear()

    Reg = []
    Deck = [i for i in range(78)]

    Random = random.sample(Deck, 78)

    Shuffle = Random

    return Random

#There are 4 draw functions one draws 3 cards at one time calling the three single draw, and image functions. The other three draw one card to
#their respective image label positions, using the specific draw and image function.
def DrawCards():
    Draw1()
    FirstFlip(Reg)
    Draw2()
    SecondFlip(Reg)
    Draw3()
    ThirdFlip(Reg)

def DrawOne():
    Draw1()
    FirstFlip(Reg)

def DrawTwo():
    Draw2()
    SecondFlip(Reg)

def DrawThree():
    Draw3()
    ThirdFlip(Reg)

#The next 3 functions are the flip check functions. They check to see if the app displays a regular or flipped image in each spot.
def FirstFlip(Reg):
    if Reg[0] == 78:
        pic = ImageTk.PhotoImage(Image.open(os.path.join(Path2, FTarot[Shuffle[0]])))
        label1.configure(image=pic)
        label1.image = pic
    else:
        pic = ImageTk.PhotoImage(Image.open(os.path.join(Path, FTarot[Shuffle[0]])))
        label1.configure(image=pic)
        label1.image = pic

def SecondFlip(Reg):
    if Reg[1] == 78:
        pic = ImageTk.PhotoImage(Image.open(os.path.join(Path2, FTarot[Shuffle[1]])))
        label2.configure(image=pic)
        label2.image = pic
    else:
        pic = ImageTk.PhotoImage(Image.open(os.path.join(Path, FTarot[Shuffle[1]])))
        label2.configure(image=pic)
        label2.image = pic

def ThirdFlip(Reg):
    if Reg[2] == 78:
        pic = ImageTk.PhotoImage(Image.open(os.path.join(Path2, FTarot[Shuffle[2]])))
        label3.configure(image=pic)
        label3.image = pic
    else:
        pic = ImageTk.PhotoImage(Image.open(os.path.join(Path, FTarot[Shuffle[2]])))
        label3.configure(image=pic)
        label3.image = pic

#These three are the specific draw funtions for each spot.
def Draw1():
    if Shuffle == 0:
        text0.insert('end', "Shuffle First!")
    else:
        Flip = (random.randint(0, 100) / 10)
        if Flip < 5 & flippable.get() == 1:
            Draw = Tarot[Shuffle[0]] + " Flipped"
            text0.insert('end', Draw)
            #text0('end', "\n")
            # Var.append(Draw)
            Reg.append(78)
        else:
            text0.insert('end', Tarot[Shuffle[0]])
            #text0('end', "\n")
            # Var.append(Draw)
            Reg.append(Shuffle[0])
    text0.config(state="disabled")
    FirstFlip(Reg)

def Draw2():
    if Shuffle == 0:
        text0.insert('end', "Shuffle First!")
    else:
        Flip = (random.randint(0, 100) / 10)
        if Flip < 5 & flippable.get() == 1:
            Draw = Tarot[Shuffle[1]] + " Flipped"
            text1.insert('end', Draw)
            #text0('end', "\n")
            # Var.append(Draw)
            Reg.append(78)
        else:
            text1.insert('end', Tarot[Shuffle[1]])
            #text0('end', "\n")
            # Var.append(Draw)
            Reg.append(Shuffle[1])
    text1.config(state="disabled")
    FirstFlip(Reg)

def Draw3():
    if Shuffle == 0:
        text0.insert('end', "Shuffle First!")
    else:
        Flip = (random.randint(0, 100) / 10)
        if Flip < 5 & flippable.get() == 1:
            Draw = Tarot[Shuffle[2]] + " Flipped"
            text2.insert('end', Draw)
            #text0('end', "\n")
            # Var.append(Draw)
            Reg.append(78)
        else:
            text2.insert('end', Tarot[Shuffle[2]])
            #text0('end', "\n")
            # Var.append(Draw)
            Reg.append(Shuffle[2])
    text2.config(state="disabled")
    FirstFlip(Reg)

def Minimize():
    global screen
    if screen == True:
        main.attributes("-fullscreen", False)
        screen = False
    else:
        main.attributes("-fullscreen", True)
        screen = True

def CoinFlip():
    top = Toplevel(main)
    top.geometry("750x650")
    top.title("The Flip!")
    '''pic = ImageTk.PhotoImage(Image.open(os.path.join(Path, "zCoin1.png")))
    coin = Label(top, text="FLIPS!", font=('BookmanOld 18 bold'), image=pic)
    coin.grid(row=0, column=2)
    Button(top, text="Flip The Coin!", command=Start).grid(row=1, column=2)'''
    Label(top, text="Coming Soon", font=("BellGothicStdBlack 20 bold"),).place(x=300, y=300)


def Start():
    Number = 0
    coin = Label
    while Number < 25:
        pic = ImageTk.PhotoImage(Image.open(os.path.join(Path, "zCoin1.png")))
        Label.configure(image=pic)
        Label.image = pic
        time.sleep(1)
        pic = ImageTk.PhotoImage(Image.open(os.path.join(Path, "zCoin2.png")))
        Label.configure(image=pic)
        Label.image = pic
        time.sleep(1)
        Number = Number + 1
    win = random.randint(0, 10)
    if win < 5:
        pic = ImageTk.PhotoImage(Image.open(os.path.join(Path, "zCoin1.png")))
        Label.configure(image=pic)
        Label.image = pic
    else:
        pic = ImageTk.PhotoImage(Image.open(os.path.join(Path, "zCoin2.png")))
        Label.configure(image=pic)
        Label.image = pic



'''def Clear():
    text0.config(state="normal")
    text0.delete(1.0, "end")
    text1.config(state="normal")
    text1.delete(1.0, "end")
    text2.config(state="normal")
    text2.delete(1.0, "end")'''

main = Tk()
main.title("Tarot The App")
main.geometry("1350x700")
main.resizable(height=False, width=False)
main.configure(bg="#5b1d7b")

main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=2)
main.columnconfigure(2, weight=2)
main.columnconfigure(3, weight=2)

main.rowconfigure(0, weight=2)
main.rowconfigure(1, weight=2)
main.rowconfigure(2, weight=2)
main.rowconfigure(3, weight=2)

buttonpic = ImageTk.PhotoImage(Image.open(os.path.join(Path, "zd1button.png")))
buttonpic2 = ImageTk.PhotoImage(Image.open(os.path.join(Path, "zd3button.png")))
buttonpic3 = ImageTk.PhotoImage(Image.open(os.path.join(Path, "zshbutton.png")))
background1 = ImageTk.PhotoImage(Image.open(os.path.join(Path, "zcloth2.jpg")))
ath = ImageTk.PhotoImage(Image.open(os.path.join(Path, "ZAC.png")))

'''background = Label(main, image=background1)
background.place(y=0, x=0)'''

frame1 = Frame(main)
frame1.grid(rowspan=3, row=1)
frame2 = Frame(main)
frame2.grid(row=2, column=1)
frame3 = Frame(main)
frame3.grid(row=2, column=2)
frame4 = Frame(main)
frame4.grid(row=2, column=3)

Text1 = Frame(main)
Text1.grid(row=1, column=1)
Text2 = Frame(main)
Text2.grid(row=1, column=2)
Text3 = Frame(main, bg="#000000")
Text3.grid(row=1, column=3)

text0 = Text(Text1, width=25, height=2, bg="#57e4aa", border=0, font="Ariel 15")
text0.pack()
text1 = Text(Text2, width=25, height=2, bg="#57e4aa", border=0, font="Ariel 15")
text1.pack()
text2 = Text(Text3, width=25, height=2, bg="#57e4aa", border=0, font="Ariel 15")
text2.pack()


button1 = Button(main, text="Draw 1 Card", command=DrawOne, image=buttonpic, border=0, bg="#5b1d7b")
button1.grid(row=3, column=1, sticky=N)
button = Button(main, text="Draw 1 Card", command=DrawTwo, image=buttonpic, border=0, bg="#5b1d7b")
button.grid(row=3, column=2, sticky=N)
button2 = Button(main, text="Draw 1 Card", command=DrawThree, image=buttonpic, border=0, bg="#5b1d7b")
button2.grid(row=3, column=3, sticky=N)

button3 = Button(main, text="Shuffle", command=Shuffled, image=buttonpic3, border=0, bg="#5b1d7b")
button3.grid(row=1, column=0, sticky=NW)
button4 = Button(main, text="Draw", command=DrawCards, image=buttonpic2, border=0, bg="#5b1d7b")
button4.grid(row=1, column=0, sticky=NE)


label = Label(frame1, bg="#5b1d7b", image=ath)
label.pack()
label1 = Label(frame2, bg="#5b1d7b", image=ath)
label1.pack()
label2 = Label(frame3, bg="#5b1d7b", image=ath)
label2.pack()
label3 = Label(frame4, bg="#5b1d7b", image=ath)
label3.pack()

flippable = IntVar()
C1 = Checkbutton(main, text='Flippable', variable=flippable, onvalue=1, offvalue=0, bg="#5b1d7b")
C1.grid(row=1, column=0, sticky="S")

menu = Menu(main)
filemenu = Menu(menu, tearoff=0)
filemenu.add_command(label="Open", command=lambda:print(2))
filemenu.add_command(label="Save", command=lambda:print(3))
filemenu.add_command(label="Coin Flip", command=CoinFlip)
filemenu.add_command(label="Fullscreen", command=Minimize)
filemenu.add_command(label="Close", command=main.destroy)
menu.add_cascade(label="File", menu=filemenu)

'''label4 = Label(main, text="HarperDesigns")
label4.pack()'''


'''text_box = Text(canvas, font=("Times 20"))
text_box.grid(column=2, row=2)'''

main.attributes("-fullscreen", screen)
main.config(menu=menu)
main.mainloop()
