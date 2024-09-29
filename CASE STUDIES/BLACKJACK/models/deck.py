from models.card import Card


class Deck:
    def __init__(self):
        self.__cards = []

    @property
    def cards(self):
        return self.__cards
    
    @cards.setter
    def cards(self, value):
        self.__cards = value
        
    def get_card(self):
        return self.__cards.pop()
    
    
# Shoe is a device to hold multiple Deck, and it has a shuffle operation.
class Shoe:
    def __init__(self):
        self.__decks = []
        self.__no_of_decks : int = 0
        
        
    def shuffle(self):
        import random
        random.shuffle(random.choice(self.__decks))
        
    @property
    def decks(self):
        return self.__decks
    
    @decks.setter
    def decks(self, value):
        self.__decks = value
        
        
    @property
    def no_of_decks(self):
        return self.__no_of_decks
    
    @no_of_decks.setter
    def no_of_decks(self, value):
        self.__no_of_decks = value
        
        
class Hand:
    def __init__(self):
        self.__cards = []
        
    @property
    def cards(self):
        return self.__cards
    
    @cards.setter
    def cards(self, value):
        self.__cards = value

    
    def add_card(self, card):
        self.__cards.append(card)
        
    def clear_hand(self):
        self.__cards = []
        
        
    def get_score(self):
        total = 0
        for card in self.__cards:
            total += card.card_value
        return total
    
    
    def stand(self):
        pass
