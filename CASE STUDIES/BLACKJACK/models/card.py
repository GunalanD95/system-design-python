from enum import Enum

class CardType(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    
class CardSuit(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4
    
class Card:
    def __init__(self):
        self.__card_id = 0
        self.__card_type = None
        self.__card_suit = None
        self.__card_value = 0

    @property
    def card_id(self):
        return self.__card_id
    
    @property
    def card_type(self):
        return self.__card_type
    
    @property
    def card_suit(self):
        return self.__card_suit
    
    @property
    def card_value(self):
        return self.__card_value
    
    @card_id.setter
    def card_id(self, value):
        self.__card_id = value
    
    @card_type.setter
    def card_type(self, value):
        self.__card_type = value
    
    @card_suit.setter
    def card_suit(self, value):
        self.__card_suit = value
    
    @card_value.setter
    def card_value(self, value):
        self.__card_value = value