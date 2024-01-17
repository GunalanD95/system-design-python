from models.ticket import Ticket


class TicketRepository:
    _tickets = {}
    last_saved_id = 0
    
    def find_ticket_number(self,ticket_num : int ):
        for ticket in self._tickets.values():
            if ticket.ticket_num == ticket_num:
                return ticket 
        return None 
    
    def save(self,ticket_obj) -> Ticket:
        self.last_saved_id += 1
        self._tickets[self.last_saved_id] = ticket_obj
        return self._tickets[id]