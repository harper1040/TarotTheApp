import random

# Tarot deck some of the suits may be out of order from what some are use to. I pulled this order from wikipedia
# where it was stated that this was the order of the original latin deck. Ultimately order doesn't matter as this
# dictionary is shuffled.
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


Deck = [i for i in range(78)]

Count = 0

Shuffle = random.sample(Deck, 78)
# Generated 78 numbers then randomized them, Shuffled the Deck.
#print(Shuffle[0:3])
# Loop through my shuffled deck 3 times and print out a card each loop. 40% chance of a flipped card can be changed.
while Count < 3:
    for card in Shuffle:
        Draw = Tarot[card]
        Flip = random.randint(0, 10)
        if Flip < 3:
            Draw2 = Draw + " Flipped"
            print(Draw2)
        else:
            print(Draw)
        if Count == 2:
            break
        Count = Count + 1
    Count = Count + 1

#while Count < 3:
    #print(Tarot[Count])

# Putting the deck shuffle into a function for use in a GUI app with a button.
def Shuffled():
    Deck = [i for i in range(78)]

    Shuffle = random.sample(Deck, 78)
    print(Shuffle)
    return Shuffle

