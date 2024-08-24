class LockerService():
    def __init__(self):
        self._lockers = []
        
    def create_locker(self, locker):
        locker.locker_id = len(self._lockers)
        self._lockers.append(locker)
        return locker
    
    def get_locker_by_id(self, locker_id):
        for locker in self._lockers:
            if locker.locker_id == locker_id:
                return locker
        return None
    
    def update_locker(self, locker):
        for idx, existing_locker in enumerate(self._lockers):
            if existing_locker.locker_id == locker.locker_id:
                self._lockers[idx] = locker
                return locker
        return None
    
    def delete_locker(self, locker_id):
        for idx, locker in enumerate(self._lockers):
            if locker.locker_id == locker_id:
                del self._lockers[idx]
                return True
        return False