import sys 
sys.path.insert(0, 'C:\\Users\\admin\\Desktop\\system-design-python\\CASE STUDIES\\PARKING LOT')

from dtos.ticket_dto import TicketRequestDTO , TicketResponseDTO
from dtos.response_status_dto import ResponseStatusDTO

class TicketController:
    
    def __init__(self , ticket_service):
        self._ticket_service = ticket_service
    
    def generate_ticket(self, request: TicketRequestDTO) -> TicketResponseDTO:
        """
        Generates a ticket for a vehicle based on the provided information.

        Parameters:
        - request (TicketRequestDTO): An object containing information about the vehicle and the gate.
          - vehicle_number (int): The number or identifier of the vehicle.
          - vehicle_type (VehicleType): The type of the vehicle (e.g., car, truck).
          - gate_id (int): The identifier of the gate where the ticket is generated.

        Returns:
        - TicketResponseDTO: An object containing the generated ticket information.
          - ticket_number (int): The unique identifier of the generated ticket.
          - issue_datetime (datetime): The date and time when the ticket was issued.
          - gate_id (int): The identifier of the gate where the ticket was generated.


        """
        # get args here  here 
        vehicle_number = request.vehicle_number
        vehicle_type = request.vehicle_type
        gate_id = request.gate_id
        
        # call service to generate ticket 
        ticket = self._ticket_service.generate_ticket(
            vehicle_number,
            vehicle_type,
            gate_id
        )      
        
        # generate response using DTO 
        response = TicketResponseDTO(ticket.ticket_num,ticket.operator.id,ticket.parking_spot.id,ResponseStatusDTO.SUCCESS)
        
        return response 
    

