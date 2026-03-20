from app.model.user import User

class UserRepository :

    _instance = None 

    def __new__(cls , conn ):
        
        if cls._instance is None :
            cls._instance = super().__new__(cls)
            cls._instance._conn = conn 
            cls._instance.create_table()
        return cls._instance
    
