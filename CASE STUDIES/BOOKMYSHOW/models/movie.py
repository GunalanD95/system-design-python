from models.basemodel import BaseModel
from typing import Optional 
from enum import Enum
from datetime import datetime

class MovieGenre(str, Enum):
    action = "action"
    adventure = "adventure"
    animation = "animation"
    comedy = "comedy"
    crime = "crime"
    documentary = "documentary"
    drama = "drama"
    family = "family"
    fantasy = "fantasy"
    history = "history"
    horror = "horror"
    music = "music"
    mystery = "mystery"
    romance = "romance"
    scifi = "scifi"
    thriller = "thriller"
    war = "war"
    western = "western"
    
class Actor(BaseModel):
    def __init__(self):
        self._id: Optional[int] = None
        self._name: Optional[str] = None
        
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
class Language(Enum):
    tamil = "tamil"
    hindi = "hindi"
    english = "english"
    spanish = "spanish"


class Movie(BaseModel):
    def __init__(self):
        self._id: Optional[int] = None
        self._name: Optional[str] = None
        self._genre: Optional[MovieGenre] = None
        self._language: Optional[Language] = None
        self._duration: Optional[int] = None
        self._release_date: Optional[datetime] = None
        self._rating: Optional[int] = None
        self._summary: Optional[str] = None
        self._cast = Optional[Actor] = []
  
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def genre(self):
        return self._genre
    
    @property
    def language(self):
        return self._language
    
    @property
    def duration(self):
        return self._duration
    
    @property
    def release_date(self):
        return self._release_date
    
    @property
    def rating(self):
        return self._rating
    
    @property
    def summary(self):
        return self._summary
    
    @property
    def cast(self):
        return self._cast
    
    
    @name.setter
    def name(self, name):
        self._name = name
        
    @genre.setter
    def genre(self, genre):
        self._genre = genre
        
    @language.setter
    def language(self, language):
        self._language = language
        
    @duration.setter
    def duration(self, duration):
        self._duration = duration
        
    @release_date.setter
    def release_date(self, release_date):
        self._release_date = release_date
        
    @rating.setter
    def rating(self, rating):
        self._rating = rating
        
    @summary.setter
    def summary(self, summary):
        self._summary = summary 
        
    @cast.setter
    def cast(self, cast):
        self._cast = cast
        