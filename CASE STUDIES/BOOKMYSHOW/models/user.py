from models.basemodel import BaseModel


class User(BaseModel):
    def __init__(self):
        super().__init__()
        self.name = None
        self.email = None
        self.is_active = None
        self.is_deleted = None
        self.phone_number = None
        
        
class Customer(User):
    def __init__(self):
        super().__init__()
        self.customer_id = None
        self.customer_name = None
        self.customer_location = None
        
        
class Admin(User):
    def __init__(self):
        super().__init__()
        self.admin_id = None