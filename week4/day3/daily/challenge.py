#Part 1
# A class is like a blueprint for creating objects, defining the attributes (data) and methods (actions) that objects of that type will have. It's a template for organizing related data and functionality.   

# An instance is a specific object created from a class. It's a concrete realization of the blueprint, with its own unique set of attribute values. For example, if "Car" is a class, then "my_red_sedan" would be an instance.   

# Encapsulation is the practice of bundling data (attributes) and the methods that operate on that data within a single unit (a class). It helps to protect the internal state of an object and prevent unintended modifications from outside.   

# Abstraction involves hiding complex implementation details and showing only the essential information to the user. It simplifies how we interact with objects by focusing on "what" an object does rather than "how" it does it.

# Inheritance is a mechanism where a new class (subclass or derived class) can inherit attributes and methods from an existing class (superclass or base class). This promotes code reuse and allows for creating specialized versions of a class.   

# Multiple inheritance is a feature where a class can inherit attributes and methods from more than one parent class. While powerful, it can sometimes lead to complexity in determining the origin of inherited members.   

# Polymorphism means "many forms" and allows objects of different classes to respond to the same method call in their own way. This enables writing more flexible and adaptable code that can work with various types of objects.   

# Method Resolution Order (MRO) is the order in which Python looks for a method in a class hierarchy when a method is called on an object. It's particularly important in multiple inheritance to determine which parent class's method to execute.

#Part 2
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