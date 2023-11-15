'''
FACTORY METHOD DESIGN PATTERN:
 - DESIGN A GAME WITH PLAYERS
 - EACH PLAYER CAN CREATE DIFF CHARACTERS
 - BUT THE CHARACTER SHOULD NOT BE TIGHTLY COUPLED TO THAT CHARACTER
 
WHY :
 - FLEXIBILITY
 - EXTENSIBILITY
 - CREATE OBJECTS WITHOUT USING ACTUAL CLASS
'''

class Villan:
    pass
        
class Hero:
    pass

class Monster:
    pass

class CharacterFactory:
    
    @staticmethod
    def create_character(CHARACTER_TYPE):
        if CHARACTER_TYPE == 'hero':
            return Hero()
        elif CHARACTER_TYPE == 'villan':
            return Villan()
        elif CHARACTER_TYPE == 'monster':
            return Monster()
        else:
            raise ValueError('no such character type')
        
hero = CharacterFactory.create_character('hero')
villan = CharacterFactory.create_character('villan')
monster = CharacterFactory.create_character('monster')
