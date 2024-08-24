from models.core import AmazonLocker 
from services.lockerservice import LockerService
from models.enums import LockerStatus

class LockerController():
    def __init__(self):
        self.service = LockerService()
        
    def assign_locker(self, locker_id, package_id, location) -> AmazonLocker:
        if locker_id is None or package_id is None:
            raise ValueError("Locker ID and Package ID are required")
        locker = AmazonLocker()
        locker.location_id = location
        locker.package_id = package_id
        locker.locker_status = LockerStatus.BOOKED
        return self.service.create_locker(locker)
    
    def get_locker_by_id(self, locker_id):
        return self.service.get_locker_by_id(locker_id)
    
    def update_locker(self, locker_id, location):
        locker = self.service.get_locker_by_id(locker_id)
        if not locker:
            raise ValueError("Locker not found")
        locker.location_id = location
        locker.locker_id = locker_id
        locker.location_id = location
        locker.locker_status = LockerStatus.Available
        return self.service.update_locker(locker)
    
    def delete_locker(self, locker_id):
        return self.service.delete_locker(locker_id)