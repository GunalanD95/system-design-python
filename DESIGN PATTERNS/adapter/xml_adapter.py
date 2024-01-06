from typing import  Any 
from bs4 import BeautifulSoup

class XMLConfig:
    
    def __init__(self , bs: BeautifulSoup ) -> None:
        self.bs = bs 
    
    def get(self, key: str) -> Any | None:
        value = self.bs.find(key)
        return value.get_text() if value else None