from random import shuffle
import random

#criando o baralho
#deck = [{'value':i, 'suit':c}
#        for c in ['espadas', 'paus', 'copas', 'ouro']
#        for i in range(2, 15)]

#embaralhando
#shuffle(deck)

#printando primeira carta
#print(deck[0]['value'], 'de', deck[0]['suit'])

class Card:
        def __init__(self, value,suit):
                self.value = value
                self.suit = suit
        
        def __str__(self):
                names = ['Jack', 'Queen', 'King', 'Ace']
                if self.value <= 10:
                        return '{} of {}'.format(self.value, self.suit)
                else:
                        return '{} of {}'.format(names[self.value-11], self.suit)

class Card_group:
        def __init__(self, cards=[]):
                self.cards = cards
        
        def nextCard(self):
                return self.cards.pop(0)
        
        def hasCard(self):
                return len(self.cards)>0
        
        def size(self):
                return len(self.cards)
        
        def shuffle(self):
                random.shuffle(self.cards)

class Standard_deck(Card_group):
        def __init__(self):
                self.cards = []
                for s in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
                        for v in range(2,15):
                                self.cards.append(Card(v, s))

a = Standard_deck()

