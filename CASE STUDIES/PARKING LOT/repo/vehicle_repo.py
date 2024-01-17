from models.vehicle import Vehicle

'''
CRUD Operations belonging to Vehicle Repo 
'''


class VehicleRepository:
    _vehicles = {}
    last_save_id = 0
    
    def check_vehicle_by_number(self, vehicle_number: int) -> Vehicle:
        for vehicle in self._vehicles.values():
            if vehicle.vehicle_num == vehicle_number:
                return vehicle
        return None 
            
            
    def save(self,vehicle_obj) -> Vehicle:
        self.last_save_id += 1
        self._vehicles[self.last_save_id] = vehicle_obj
        return self._vehicles[id]