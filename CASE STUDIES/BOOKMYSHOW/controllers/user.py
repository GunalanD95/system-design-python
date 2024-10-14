from models.user import User
from services.user import UserService

class UserController:

    def __init__(self):
        self.service = UserService()
        
    def create_user(self, name: str, email: str, password: str) -> User:
        if not(name and email and password):
            return ValueError("All fields are required")
        
        user_obj = self.service.create_user(name, email, password)
        return {"user": user_obj}

    def update_user(self,name: str, email: str, password: str) -> User:
        if not email:
            return ValueError("Email is required")
        update_user = self.service.update_user(name, email, password)
        if not update_user:
            return ValueError("User not found")
        return {"user": update_user}

    def get_user_by_email(self, email: str) -> User:
        if not email:
            return ValueError("Email is required")
        
        user = self.service.get_user_by_email(email)
        if not user:
            return ValueError("User not found")
        return {"user": user}
    
    def get_user_by_id(self, user_id: int) -> User:
        if not user_id:
            return ValueError("User id is required")
        
        user = self.service.get_user_by_id(user_id)
        if not user:
            return ValueError("User not found")
        return {"user": user}   
    
    