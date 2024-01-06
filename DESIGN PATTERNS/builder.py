'''
GOAL OF BUILDER PATTERN:
- SEPARATE CONSTRUCTION OF OBJECT AND REPRESENTATION OF THE OBJECT


Builder Class : HouseBuilder (creation of the builder object)
 - it will have setter methods and attributes of the class
 - also have build() to build the house object -> House Constructor()
'''
from abc import ABC ,abstractclassmethod , abstractmethod

class House:
    def __init__(self , builder) -> None:
        self.floor = builder.floor
        self.rooms = builder.rooms 
        self.wall  = builder.wall
        self.roof_type = builder.roof_type 

    def __repr__(self) -> str:
        return f"{self.rooms} BHK | {self.floor} floor | {self.wall} walls"
    
    
class HouseBuilder:
    def __init__(self):
        self.floor = None
        self.rooms = None 
        self.wall  = None
        self.roof_type = None

     
    def set_rooms(self,rooms):
        self.rooms = rooms 
        return self # return builder object 
    
     
    def set_wall(self,wall):
        self.wall = wall 
        return self
        
     
    def set_roof_type(self,roof_type):
        self.roof_type = roof_type    
        return self 
        
     
    def set_floor(self,floor):
        self.floor = floor   
        return self 
    
    # build method
    def build(self):
        return House(self) # passing builder with all attributes
    
    
class HouseBuilder2BHK:
    def __init__(self):
        self.builder = HouseBuilder() 
        
    def build(self):
        return self.builder.set_rooms(2).build()   

class HouseDirector:
    def __init__(self,builder):
        self.builder = builder 
        
    def build(self):
        return self.builder.build()


hb  = HouseBuilder2BHK()
dire = HouseDirector(hb)
bhk  = dire.build()
print(bhk) 
       

########################################################################################################################
# Dosa-Builder 
# Product : Dosa
class Dosa:
    def __init__(self,dosa_type,size,ghee_needed=False):
        self.dosa_type   = dosa_type
        self.ghee_needed = ghee_needed
        self.size        = size

    def __str__(self):
        return f"{self.dosa_type} | {self.ghee_needed} | {self.size}"

#Abstract Dosa Builder    
class DosaBuilder:
    def __init__(self):
        self.dosa = None

    @abstractmethod
    def build_dosa(self):
        pass
    
    @abstractmethod
    def get_dosa(self):
        return self.dosa
    
# Concrete Builder: Gobi Dosa
class GobiDosaBuilder(DosaBuilder):
    def build_dosa(self):
        self.dosa = Dosa('Gobi-Dosa','Medium',True)
        return self
# Concrete Builder: Masal Dosa
class MasalDosaBuilder(DosaBuilder):
    def build_dosa(self):
        self.dosa = Dosa('Masal-Dosa','Medium',True)
        return self
# Concrete Builder: Oninon Dosa
class OninonDosaBuilder(DosaBuilder):
    def build_dosa(self):
        self.dosa =  Dosa('Onion-Dosa','Medium',True)
        return self
        
# Director: DosaDirector
class DosaDirector:
    def construct_dosa(self, dosa_builder):
        return dosa_builder.build_dosa().get_dosa()
    

gobi_dosa_builder = GobiDosaBuilder()   
dosa_diretor = DosaDirector()    
dosa = dosa_diretor.construct_dosa(gobi_dosa_builder)