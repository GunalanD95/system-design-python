from services.ticket_service import TicketService
from repo.gate_repo import GateRepository
from repo.parking_lot_repo import ParkingLotRepository
from repo.ticket_repo import TicketRepository
from repo.vehicle_repo import VehicleRepository 
from strategies.spot_assign_strategy import RandomSpotAssignmentStrategy
from controllers.ticket_controller import TicketController
from dtos.ticket_dto import TicketRequestDTO 
from dtos.response_status_dto import ResponseStatusDTO

from models.vehicle import Vehicle , VehicleType

class ParkingLotApplication:
    
    
    def main(self):
        # Create everything from topological sorting
        # repos 
        gate_repo = GateRepository()
        vehicle_repo = VehicleRepository()
        spot_assign_strategy =  RandomSpotAssignmentStrategy()
        ticket_repo = TicketRepository()
        parking_repo = ParkingLotRepository()
        
        
        ticket_service = TicketService(gate_repo ,vehicle_repo, spot_assign_strategy , ticket_repo , parking_repo)

        ticket_controller = TicketController(ticket_service)
                
        request_ticket_dto = TicketRequestDTO(
            vehicle_number=123,
            vehicle_type=VehicleType.BIKE,
            gate_id=0,
        )
        
        # generate ticket 
        try:
            response  = ticket_controller.generate_ticket(
                request_ticket_dto
            )
        except Exception as e:
            response = ResponseStatusDTO.FAILURE
            return response 
        
        
        return response
        
        
        
parking_app = ParkingLotApplication()
parking_app.main()