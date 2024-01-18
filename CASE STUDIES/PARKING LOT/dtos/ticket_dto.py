from pydantic import BaseModel
from models.vehicle import VehicleType
from .response_status_dto import ResponseStatusDTO

class TicketRequestDTO(BaseModel):
    vehicle_number: int
    vehicle_type: VehicleType
    gate_id: int
    
class TicketResponseDTO(BaseModel):
    ticket_id : int
    operator_id : int 
    spot_number : int 
    response_status : ResponseStatusDTO