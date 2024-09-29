from models.user import User

class UserService:
    
    def __init__(self) -> None:
        self.users = []    

    def create_user(self, name: str, email: str, password: str) -> User:
        user = User()
        user.user_id = len(self.users) + 1
        user.name = name
        user.email = email
        user.password = password
        self.users.append(user)
        return user
    
    def get_user_by_email(self, email: str) -> User:
        for user in self.users:
            if user.email == email:
                return user
        return None

    def get_user_by_id(self, user_id: int) -> User:
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
    
    def update_user(self, user_id: int, name: str, email: str, password: str) -> User:
        user = self.get_user_by_id(user_id)
        if user:
            user.name = name
            user.email = email
            user.password = password
            return user
        return None

    def get_all_users(self) -> list[User]:
        return self.users