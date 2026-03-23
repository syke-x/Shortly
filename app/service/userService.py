from app.model.user import User 
from app.repository.userRepository import UserRepository

class UserService:

    _instance = None 

    def __new__(cls , user_repo : UserRepository):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._user_repo = user_repo
        return cls._instance
