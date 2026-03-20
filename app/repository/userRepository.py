from app.model.user import User

class UserRepository :

    _instance = None 

    def __new__(cls , conn ):
        
        if cls._instance is None :
            cls._instance = super().__new__(cls)
            cls._instance._conn = conn 
            cls._instance._create_table()
        return cls._instance
    

    def _create_table(self) -> None:

        self._conn.execute_query(
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                hash_password TEXT NOT NULL,
                created_at TIMESTAMP NOT NULL            
            )
            """
        )

    
