from models.parking_gate import ParkingGate 
'''
CRUD Operations belonging to Gate Repo 
'''
from collections import defaultdict

class GateRepository:
    _gateMap = defaultdict()
    
    def find_gate_by_id(self, gate_id : int) -> ParkingGate:
        if gate_id in self._gateMap:
            return self._gateMap[gate_id]
        return None