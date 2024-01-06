class Player:
    
    def __init__(self,name : str,symbol : str) -> None:
        self.name   = name 
        self.symbol = symbol
        
class PlayerBuilder:
    def __init__(self,name=None,symbol=None) -> None:
        self.name   = '' 
        self.symbol = ''
        
    def set_name(self,name : str) :
        print("name-->",name)
        self.name = name 
        return self 
        
    def set_symbol(self,symbol : str):
        self.symbol = symbol 
        return self
    
    
    def build(self) -> Player:
        return Player(self.name,self.symbol)