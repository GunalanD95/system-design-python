from abc import ABC , abstractmethod
import random 
from models.parking_spot import ParkingSpot

class SpotAssignmentStrategy(ABC):
    @abstractmethod
    def get_parking_spot(self,vehicle_type , parking_lot ,entry_gate):
        pass 
    

class RandomSpotAssignmentStrategy(SpotAssignmentStrategy):
    def get_parking_spot(self,vehicle_type , parking_lot ,entry_gate):
        available_spots = self._get_available_spots(vehicle_type, parking_lot)

        if not available_spots:
            return None  # No available spots of the required type

        # Randomly select an empty spot
        try:
            selected_spot = random.choice(available_spots)
        except Exception as e:
            selected_spot = None
        return selected_spot

    def _get_available_spots(self, vehicle_type, parking_lot) -> [ParkingSpot]:
        available_spots = []

        for floor in parking_lot.parking_floors:
            floor_spots = [spot for spot in floor.parking_spots if spot.is_empty() and vehicle_type in spot._vehicle_types]
            available_spots.extend(floor_spots)

        return available_spots