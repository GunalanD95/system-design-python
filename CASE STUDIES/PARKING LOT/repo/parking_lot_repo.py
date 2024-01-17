from models.parking_lot import ParkingLot
from collections import defaultdict


class ParkingLotRepository:    
    _parkingLotMap = defaultdict()
    
    def get_parking_from_gate(self, gate) -> ParkingLot:
        '''
        get parking lot using gate
        '''
        
        for parkinglot in self._parkingLotMap.values():
            for pgate in parkinglot.parking_gates:
                if pgate.id == gate.id:
                    return parkinglot
        return None