from tkinter import *
import random
from PIL import Image, ImageTk
import os

Path = 'C:/Users/Jack/PycharmProjects/untitled/Tarot/'
Path2 = "C:/Users/Jack/PycharmProjects/untitled/FlipTarot/"

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
          71 : "XA.jpg", 72 : "XB.jpg", 73 : "Y.jpg", 74 : "YA.jpg", 75 : "YB.jpg", 76 : "Z.jpg", 77 : "ZA.jpg", 78 : "ZAB.jpg"}

Cards = {0 : "card0.jpg"}

Shuffle = 0

Var = [78, 78, 78]


Deck = [i for i in range(78)]

#Shuffle = random.sample(Deck, 78)


main = Tk()
main.title("Tarot The App")

'''width= main.winfo_screenwidth()
height= main.winfo_screenheight()

main.geometry("%dx%d" % (width, height))'''
main.geometry("1440x720")
text_box = Text(main, height=6, width=20, font=("Times 20"))
text_box.pack()

def Shuffled():
    global Shuffle
    Deck = [i for i in range(78)]

    Random = random.sample(Deck, 78)

    Shuffle = Random

    return Random

def Cardview():
    pass
    #img = Image.open(os.path.join(Path, FTarot[Draw]))  Need to relabel Tarot dict.
    # place.insert(img)

def Delete():
    text_box.delete(1.0, "end")

def DrawCards():
    Count = 0
    text_box.delete(1.0, "end")
    Var.clear()
    Reg = []
    Flips = []
    if Shuffle == 0:
        text_box.insert('end', "Shuffle First!")
    else:
        while Count < 3:
            for card in Shuffle:
                Draw = Tarot[card]
                Flip = random.randint(0, 10)
                if Flip < 3 & flippable.get() == 1:
                    Draw2 = Draw + " Flipped"
                    text_box.insert('end', Draw2)
                    text_box.insert('end', "\n")
                    Var.append(Draw)
                    Flips.append(card)
                    Reg.append(78)
                else:
                    text_box.insert('end', Draw)
                    text_box.insert('end', "\n")
                    Var.append(Draw)
                    Reg.append(card)
                    Flips.append(78)

                if Count == 2:
                    break
                Count = Count + 1
            Count = Count + 1
    ImageFlip(Reg)

'''def ImageDraw():
    print(Shuffle)
    pic = ImageTk.PhotoImage(Image.open(os.path.join(Path, FTarot[Shuffle[0]])))
    card1.configure(image=pic)
    card1.image = pic

    pic2 = ImageTk.PhotoImage(Image.open(os.path.join(Path, FTarot[Shuffle[1]])))
    card2.configure(image=pic2)
    card2.image = pic2

    pic3 = ImageTk.PhotoImage(Image.open(os.path.join(Path, FTarot[Shuffle[2]])))
    card3.configure(image=pic3)
    card3.image = pic3'''

def ImageFlip(Reg):

    if Reg[0] == 78:
        pic = ImageTk.PhotoImage(Image.open(os.path.join(Path2, FTarot[Shuffle[0]])))
        card1.configure(image=pic)
        card1.image = pic
    else:
        pic = ImageTk.PhotoImage(Image.open(os.path.join(Path, FTarot[Shuffle[0]])))
        card1.configure(image=pic)
        card1.image = pic

    if Reg[1] == 78:
        pic1 = ImageTk.PhotoImage(Image.open(os.path.join(Path2, FTarot[Shuffle[1]])))
        card2.configure(image=pic1)
        card2.image = pic1
    else:
        pic1 = ImageTk.PhotoImage(Image.open(os.path.join(Path, FTarot[Shuffle[1]])))
        card2.configure(image=pic1)
        card2.image = pic1

    if Reg[2] == 78:
        pic3 = ImageTk.PhotoImage(Image.open(os.path.join(Path2, FTarot[Shuffle[2]])))
        card3.configure(image=pic3)
        card3.image = pic3
    else:
        pic3 = ImageTk.PhotoImage(Image.open(os.path.join(Path, FTarot[Shuffle[2]])))
        card3.configure(image=pic3)
        card3.image = pic3

frame1 = Frame(main)
frame1.pack()
label = Label(frame1, text="Hello World!")
label.pack()

img = 1
pic = ImageTk.PhotoImage(Image.open(os.path.join(Path, FTarot[Var[0]])))
img2 = 1
pic2 = ImageTk.PhotoImage(Image.open(os.path.join(Path, FTarot[Var[0]])))
img3 = 1
pic3 = ImageTk.PhotoImage(Image.open(os.path.join(Path, FTarot[Var[0]])))

flippable = IntVar()
C1 = Checkbutton(main, text='Flippable', variable=flippable, onvalue=1, offvalue=0)
C1.pack()
button1 = Button(frame1, text="Shuffle", command=Shuffled)
button1.pack()
button2 = Button(frame1, text="Draw", command=DrawCards)
button2.pack()
button3 = Button(frame1, text="Reset", command=Delete)
button3.pack()
card1 = Label(frame1, image=pic, width=150, height=300)
card1.pack(side="left")
card2 = Label(frame1, image=pic2)
card2.pack(side="right")
card3 = Label(frame1, image=pic3)
card3.pack()

main.mainloop()


