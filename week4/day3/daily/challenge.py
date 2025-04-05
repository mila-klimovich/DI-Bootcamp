import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # def __print__(self):
    def __repr__(self):
        return f"{self.value} {self.suit}"
    
class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        self.deck = [Card(suit, value) for suit in self.suits for value in self.values]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        card = self.deck[0]
        del self.deck[0]
        return card
    
deck = Deck()
deck.shuffle()
card = deck.deal()
print(card)