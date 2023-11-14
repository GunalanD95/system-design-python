'''
GOAL OF BUILDER PATTERN:
- SEPARATE CONSTRUCTION OF OBJECT AND REPRESENTATION OF THE OBJECT


Builder Class : HouseBuilder (creation of the builder object)
 - it will have setter methods and attributes of the class
 - also have build() to build the house object -> House Constructor()
'''


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
       


