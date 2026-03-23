from app.model.user import User 
from app.repository.userRepository import UserRepository

from datetime import datetime

class UserService:

    _instance = None 

    def __new__(cls , user_repo : UserRepository):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._user_repo = user_repo
        return cls._instance


    def create_user(self , name : str , email :str , password : str) -> User:

        # check if the email is already present 
        exisiting = self._user_repo.find_by_email(email)

        if exisiting:
            raise ValueError("Email is already present")
        
        hash_password = AuthService.hash_password(password)

        user = User(
            user_id=utils.generate_user_id(),
            name = name,
            email=email,
            hash_password=hash_password,
            created_at=datetime.utc()
        )

        self._user_repo.save(user)
        return user 
    
    def login_user(self , email : str , password : str) -> User:

        user = self._user_repo.find_by_email(email)

        if user is None:
            raise ValueError("user with this email doesn't exsist")
        
        return user 
    
    
