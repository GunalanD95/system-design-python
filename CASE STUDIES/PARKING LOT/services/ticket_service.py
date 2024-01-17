from models.ticket import Ticket
from models.vehicle import Vehicle , VehicleType
from repo.gate_repo import GateRepository
from repo.vehicle_repo import VehicleRepository
from repo.ticket_repo import TicketRepository
from repo.parking_lot_repo import ParkingLotRepository

from strategies.spot_assign_strategy import RandomSpotAssignmentStrategy
from datetime import datetime

class GateNotFoundException(Exception):
    def __init__(self, gate_id):
        self.gate_id = gate_id
        super().__init__(f"Gate with ID {gate_id} not found in the repository.")


class NoSpotException(Exception):
    def __init__(self, ):
        super().__init__(f"No spot avaiable")

class TicketService:

    # Business Logic
    def __init__(self , gate_repo , vehicle_repo , spot_assign_strategy , ticket_repo, parking_repo) -> None:
        self.gate_repo = gate_repo
        self.vehicle_repo =  vehicle_repo
        self.spot_assign_strategy = spot_assign_strategy
        self.ticket_repo = ticket_repo
        self.parking_repo = parking_repo
    
    def generate_ticket(self, vehicle_number: int, vehicle_type: VehicleType, gate_id: int) -> Ticket:
        """
        Generate a ticket based on the provided information.

        Parameters:
        - vehicle_number (int): The number or identifier of the vehicle.
        - vehicle_type (VehicleType): The type of the vehicle.
        - gate_id (int): The identifier of the parking gate.

        Returns:
        - Ticket: The generated ticket.

        Raises:
        - GateNotFoundException: If the specified gate_id is not found in the repository.
        """
        gate = self.gate_repo.find_gate_by_id(gate_id)
        
        if not gate:
            raise GateNotFoundException(gate_id)

        operator = gate.operator
        vehicle  = self.vehicle_repo.check_vehicle(vehicle_number)
        
        if not vehicle:
            new_vehicle = Vehicle()
            new_vehicle.vehicle_num = vehicle_number
            new_vehicle.vehicle_type = vehicle_type
            vehicle = new_vehicle
            
            
        # for parking spot -> we need spot assign strategy
        parking_lot = self.parking_repo(gate)
        
        parking_spot = self.spot_assign_strategy.get_parking_spot(vehicle.vehicle_type,parking_lot,gate)
        
        if not parking_spot:
            raise NoSpotException()
        
        # creating ticket object now  
        ticket       = Ticket()
        ticket.ticket_num = 1
        ticket.enter_time = datetime.now()
        ticket.parking_spot = parking_spot
        ticket.parking_gate = gate
        ticket.operator = operator
        ticket.vehicle  = vehicle
        
        self.ticket_repo.save(ticket)
        
        return ticket 

