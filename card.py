import random
import datetime
import sys

class card():
    def __init__(self):
        self.generate()
    

    def generate(self):
        randomNumber()
        self.cardFace = random.randint(1,13)
        # print("Card Value: "+str(self.cardValue))

        randomNumber()
        self.cardSuit = random.randint(1,4)
        # print("Card Suit: " + str(self.cardSuit))

        if self.cardFace >= 10:
            self.cardValue = 10
        else:
            self.cardValue = self.cardFace


def randomNumber():
    seedValue = random.randrange(sys.maxsize)
    random.seed(seedValue)
