from card import card
from hand import hand

class dealer():
    def __init__(self):
        self.card1 = card()
        self.card2 = card()
        self.hand = hand(self.card1, self.card2)
        self.hand.total()