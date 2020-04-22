import random


class Card(object):
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    faceValues = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def _init_(self, suit=0, faceValue=2): # initializes basic values for a card
        self.suit = suit
        self.faceValue = faceValue

    def _str_(self): # returns card's face value and suit
        return "%s of %s" % (Card.faceValues[self.faceValue], Card.suits[self.suit])

    def _cmp_(self, other): # returns positive if this card is higher, negative if this card is lower and 0 if they are the same value
        c1 = self.faceValue
        c2 = other.faceValue
        return (c1>c2)-(c1<c2)