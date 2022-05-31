from card import card

class hand():
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2

    def total(self):
        self.total = self.card1.cardValue + self.card2.cardValue
        print(self.total)