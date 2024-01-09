from abc import ABC , abstractclassmethod , abstractmethod

# Transport interface and concerte class
class Transport(ABC):
    """AN interface for each mode of transport"""

    @abstractmethod
    def operation(self):
        ''' each class will have its own implementation '''
        pass 
    
class Bus(Transport):
    speed = 50
    
    def operation(self , distance : int) -> float:
        estimated_hours = distance / self.speed
        return estimated_hours
    
class Bike(Transport):
    speed = 80
    
    def operation(self , distance : int) -> float:
        estimated_hours = distance / self.speed
        return estimated_hours
    
class Car(Transport):
    speed = 1000
    
    def operation(self , distance : int) -> float:
        estimated_hours = distance / self.speed
        return estimated_hours
    
    
################################################################################################################
# Route Strategy :

class RouteSelection:
    
    def __init__(self, transport : Transport):
        """self._transport references the objects of other transport classes. Its called composition."""
        self._transport = transport


    def time_estimation(self,distance) -> int:
        """Call the operation's function from referenced instance variable."""
        return self._transport.operation(distance)
    
    
if __name__ == '__main__':

    public_transport = Bus()
    route_selection = RouteSelection(public_transport)
    print('Estimated time to reach destination VIA Bus: ', route_selection.time_estimation(60))

    car = Car()
    route_selection = RouteSelection(car)
    print('Estimated time to reach destination VIA Car: ', route_selection.time_estimation(60))

    bike = Bike()
    route_selection = RouteSelection(bike)
    print('Estimated time to reach destination VIA Bike: ', route_selection.time_estimation(60))