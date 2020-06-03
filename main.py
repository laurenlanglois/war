# import tkinter
import random

# FOLLOWING BLOCK OF CODE WAS FOR TESTING TKINTER
# window = tkinter.Tk()
# window.geometry("800x600")
# window.title("war")
# but = tkinter.Button(window, text="lune", bg="pink", fg="purple").pack()
# welcomeText = tkinter.Text(window, width=40, height=10)
# tkinter.Text.insert('1.0', 'here is my text to insert')
# response = input("Would you like to give your rival a name? [enter 'n' to decline]\n")
# window.mainloop()

# functions for printing:
# pack() -> organizes the widgets in the block to occupy entire available width
# grid() -> organizes widgets in a table-like structure
# place() -> places widgets at a specific location


# card class
class Card(object):
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

    # essentially a toString
    def reveal(self):  # returns card's face value and suit
        if self.value == 11:
            print("{} of {}".format("Jack", self.suit))
        elif self.value == 12:
            print("{} of {}".format("Queen", self.suit))
        elif self.value == 13:
            print("{} of {}".format("King", self.suit))
        elif self.value == 14:
            print("{} of {}".format("Ace", self.suit))
        else:
            print("{} of {}".format(self.value, self.suit))

    def __cmp__(self, other):  # returns + if this card is higher, - if this card is lower, and 0 if they are equal
        c1 = self.value
        c2 = other.value
        return (c1 > c2) - (c1 < c2)


# deck of cards
class Deck(object):
    def __init__(self, empty):  # (self, boolean isEmpty)
        self.cards = []

        if not empty:
            self.build()

    def build(self):
        print("Building deck....")
        for suitOfCard in ["Clubs ♣", "Diamonds ♦", "Hearts ♥", "Spades ♠"]:
            for valueOfCard in range(2, 15):
                self.cards.append(Card(suitOfCard, valueOfCard))

    # essentially a toString
    def reveal(self):
        for c in self.cards:
            c.reveal()

    # start at last element of deck and increment towards to the front
    def shuffle(self):
        print("Shuffling cards....")
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)  # random card to swap
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]  # swap

    # return next card in deck
    def draw(self):
        if len(self.cards) <= 0:
            return "Can not draw from an empty deck"
        else:
            return self.cards.pop()

    def add(self, card):
        self.cards.append(card)


class Player(object):
    def __init__(self, name):
        # a player's hand is a deck of cards
        self.hand = Deck(True)
        self.discardPile = Deck(True)
        self.cardsInPlay = Deck(True)
        self.name = name

    def draw(self, deck):
        self.hand.add(deck.draw())  # add the next card of the deck to the player's hand

    # prints out all of the player's cards
    def revealHand(self):
        for i in self.hand:
            i.reveal()

    def playCard(self):
        return self.cardsInPlay.add(self.hand.draw())


# main
p1 = Player("Player 1")
p2 = Player("Rival Computer")
turnCount = 0
winner = ""

print("Welcome to the game of war!\nYou will be facing off against an enemy computer that you must destroy!")
response = input("Would you like to give your rival a name? [enter 'n' to decline]\n")
if response != "n":
    p2.name = input("Please enter your rival's new name.\n")
print("Get ready to face the ultimate challenger: ", p2.name)
p1.name = input("... and now that we know what you'll be up against, what is your name?\n")
print("Welcome to the arena! I hope you are ready for a war, ", p1.name)

# make deck and shuffle
mainDeck = Deck(False)
# print("Cards created: ")
# mainDeck.reveal() # just prints out the whole deck before it's shuffled and distributed to ensure proper deck creation
mainDeck.shuffle()

# deal cards, half to each player
while len(mainDeck.cards) > 0:
    p1.draw(mainDeck)
    p2.draw(mainDeck)

# play turns until someone has all the cards
while len(p1.hand.cards) > 0 and len(p2.hand.cards) > 0:
    p1.playCard()
    p2.playCard()
    # if p1's most recently played card is higher:
    if p1.cardsInPlay.cards[-1].value > p2.cardsInPlay.cards[-1].value:
        # p1 draw all cards that were just in play
        for i in p1.cardsInPlay.cards:
            p1.draw(p1.cardsInPlay)
        for i in p2.cardsInPlay.cards:
            p1.draw(p2.cardsInPlay)

        print(p1.name + " wins the battle")

    # else, if p2's most recently played card is higher
    elif p1.cardsInPlay.cards[-1].value < p2.cardsInPlay.cards[-1].value:
        # p2 draw all cards that were just in play
        for i in p1.cardsInPlay.cards:
            p2.draw(p1.cardsInPlay)
        for i in p2.cardsInPlay.cards:
            p2.draw(p2.cardsInPlay)

        print(p2.name + " wins the battle")

    # else, if both player's most recently played cards are equal in value (in other words, a "war")
    elif p1.cardsInPlay.cards[-1].value == p2.cardsInPlay.cards[-1].value:
        print("Time for a WAR!")
        # play two more cards per player
        for i in range(2):
            p1.playCard()
            p2.playCard()

    # declare winner
    if len(p1.hand.cards) == 0:
        print(p2.name + " WINS THE GAME!!!")
    if len(p2.hand.cards) == 0:
        print(p1.name + " WINS THE GAME!!!")




# FOLLOWING BLOCK OF CODE FOR TESTING TKINTER
# window = tkinter.Tk()
# window.geometry("800x600")
# window.title("war")
# if len(p1.hand.cards) == 0:
#     welcomeText = tkinter.Label(window, text=p2.name + " WINS THE GAME!!!")
# if len(p2.hand.cards) == 0:
#     welcomeText = tkinter.Label(window, text=p1.name + " WINS THE GAME!!!")


# if len(p1.hand.cards) == 0:
#     tkinter.Text.insert(welcomeText, "a", p2.name + " WINS THE GAME!!!")
#     window.mainloop()
# if len(p2.hand.cards) == 0:
#     tkinter.Text.insert(welcomeText, "a", p1.name + " WINS THE GAME!!!")
#     window.mainloop()

# but = tkinter.Button(window, text="lune", bg="pink", fg="purple").pack()
# response = input("Would you like to give your rival a name? [enter 'n' to decline]\n")
# window.mainloop()

# welcomeText.pack()
# window.mainloop()

# functions for printing:
# pack() -> organizes the widgets in the block to occupy entire available width
# grid() -> organizes widgets in a table-like structure
# place() -> places widgets at a specific location
