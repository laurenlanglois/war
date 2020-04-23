import random
import tkinter


# card class
class Card(object):
    def __init__(self, suit, value):

        if value == 11:
            self.value = "Jack"
        elif value == 12:
            self.value = "Queen"
        elif value == 13:
            self.value = "King"
        elif value == 14:
            self.value = "Ace"
        else:
            self.value = value

        self.suit = suit

    # essentially a toString
    def reveal(self):  # returns card's face value and suit
        print("{} of {}".format(self.value, self.suit))

    def __cmp__(self, other):  # returns positive if this card is higher, negative if this card is lower and 0 if
        # they are the same value
        c1 = self.value
        c2 = other.value
        return (c1 > c2) - (c1 < c2)


# deck of cards
class Deck(object):
    def __init__(self):
        self.cards = []
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
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        # a player's hand is a deck of cards
        self.hand = []
        self.name = name

    def draw(self, deck):
        self.hand.append(deck.draw())  # add the next card of the deck to the player's hand

    def revealHand(self):
        for card in self.hand:
            card.reveal()


# main
p1 = Player("Player 1")
p2 = Player("Rival Computer")


print("Welcome to the game of war!\nYou will be facing off against an enemy computer that you must destroy!")
response = input("Would you like to give your rival a name? [enter 'n' to decline]\n")
if response != "n":
    p2.name = input("Please enter your rival's new name.\n")
print("Get ready to face the ultimate challenger: ", p2.name)
p1.name = input("... and now that we know what you'll be up against, what is your name?\n")
print("Welcome to the arena! I hope you are ready for a war, ", p1.name)
deck = Deck()
deck.shuffle()


# m = tkinter.Tk()
# m.mainloop();
# img = tk.PhotoImage(file="")