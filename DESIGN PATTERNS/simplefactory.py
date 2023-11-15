'''
FACTORY DESIGN PATTERN :
 - SIMPLE FACTORY
 - FACTORY METHOD
 - ABSTRACT METHOD
'''

'''
SIMPLE FACTORY:
 - GIVING CLIENT ABILTIY TO CREATE OBJECTS WITHOUT EXPOSING THE OBJECT CREATIONAL LOGIC 
 - HELPS TO PROMOTE ENCAPSULATION
 - ENCAPSULATE THE OBJECT CREATION FROM CLINET CODE 
'''

'''
PIZZA ORDERING APP:
 TYPES OF PIZZA:
  - CHEESE PIZZA
  - VEG PIZZA
  - PEPPORONI PIZZA
'''
class Pizza:
    def __init__(self) -> None:
        self.name = ""
        self.ingridents = []
        
    def prepare(self):
        print(f"preparing {self.name}.....")
        print(f"Adding {self.ingridents}....")
        
    def bake(self):
        print(f"Baking {self.name} Pizaa")
        
    def putinbox(self):
        print(f"Putting {self.name} in Box")    
        
        
class CheesePizza(Pizza): 
    def __init__(self) -> None:
        super().__init__()
        self.name = "Cheese Pizza" 
        self.ingridents = ['pizza dough', 'tomato sauce','cheese']
        
        
class VegPizza(Pizza): 
    def __init__(self) -> None:
        super().__init__()
        self.name = "Veg Pizza" 
        self.ingridents = ['pizza dough', 'tomato sauce','spinach']
        
        
class PeporoniPizza(Pizza): 
    def __init__(self) -> None:
        super().__init__()
        self.name = "Peporoni Pizza" 
        self.ingridents = ['pizza dough', 'tomato sauce','peporoni']
        
        
# We need a Pizza Factory Class
class PizzaFactoy():
    def __init__(self) -> None:
        self.pizzas = {
            'cheese'   : CheesePizza(),
            'vegie'    : VegPizza(),
            'peporoni' : PeporoniPizza(),   
        }
        
    def get_pizza(self,name):
        return self.pizzas[name]
    
    
pizza_factory = PizzaFactoy()

cheese_pizza   = pizza_factory.get_pizza('cheese')
vegie_pizza    = pizza_factory.get_pizza('vegie')
peporoni_pizza = pizza_factory.get_pizza('peporoni')

print(" ")

print(cheese_pizza,"cheese_pizza",cheese_pizza.__dict__)

print(" ")

print(vegie_pizza,"vegie_pizza",vegie_pizza.__dict__)

print(" ")

print(peporoni_pizza,"peporoni_pizza",peporoni_pizza.__dict__)
    
