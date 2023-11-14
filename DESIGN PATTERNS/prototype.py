'''
PROTOTYPE DESIGN PATTERN:
 - USED TO COPY A OBJECT EFFICIENTLY
 - CONSIDER OBJECT WITH MINIAL CHANGE IN ATTRIBUTES ( ITS BETTER TO CLONE THE PROTOTYPE )
 - CREATION OF NEW OBJECT IS TIME CONSUMING ( IF MORE ATTRS ARE THERE) 
'''

'''
We are gonna Design a Game Class 
 - diff types of enemy
 - each enemy will have diff characterstics
'''

from abc import  abstractclassmethod , ABC 

# PROTOTYPE CLASS
class EnemyPrototype(ABC):
    @abstractclassmethod
    def clone(self):
        pass
    
    @abstractclassmethod
    def attack(self):
        pass
    
# CONCERTE PROTOTYPE
# two different type of enemy 
# Doctor Octopus and Sandman

class Sandman(EnemyPrototype):
    def clone(self):
        return Sandman() 
    
    def attack(self):
        print(f"Sandman is attacking")
    
class DoctorOctopus(EnemyPrototype):
    def clone(self):
        return DoctorOctopus() 
    
    def attack(self):
        print(f"Doctor Octopus is attacking")
 
 
# Registry : Manage our enemy prototypes
class EnemyRegistry:
    def __init__(self) -> None:
        self.prototypes = {}
    
    def register_enemy(self,enemy_type,prototype):
        self.prototypes[enemy_type]  = prototype
        
    def clone_enemy(self,enemy_type):
        return self.prototypes[enemy_type].clone()
    
registry         = EnemyRegistry()
sandman_prototype = Sandman()
dcoctps_prototype = DoctorOctopus()  

registry.register_enemy('sandman',sandman_prototype)
registry.register_enemy('doctor octpus',dcoctps_prototype)

print(registry.prototypes)

# clone prototypes
sandman_clone = registry.clone_enemy('sandman')
dcoctps_clone = registry.clone_enemy('doctor octpus')


print("sandman_clone",sandman_clone)
print("dcoctps_clone",dcoctps_clone)

    

    
    
    
    
    
    