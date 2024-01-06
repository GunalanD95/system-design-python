from typing import Protocol , Any 

class Config(Protocol):
    
    def get(self, key: str) -> Any | None:
        '''
        takes_input : Key 
        
        returns : any data type or None value associated with the key
        
        '''
        
    