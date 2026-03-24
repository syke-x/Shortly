from abc import ABC , abstractmethod
import sqlite3 
class Connection(ABC):

    @abstractmethod
    def start_connection(self  ):
        pass

    @abstractmethod
    def disconnect(self ):
        pass

    @abstractmethod
    def execute_query(self , query : str) : 
        pass 


class SQLiteConnection(Connection) : 

    def __init__(self , db_path : str):

        self.db_path = db_path
        self.conn = None

    def start_connection(self):
        
        self.conn = sqlite3.connect(self.db_path)
        return self.conn
    
    def disconnect(self):
        if self.conn : 
            self.conn.close()
            self.conn = None 
    
    
    
    
        