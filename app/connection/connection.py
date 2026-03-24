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
    def execute_query(self , query : str , params : tuple = ()) : 
        pass 


class SQLiteConnection(Connection) : 

    def __init__(self , db_path : str):

        self.db_path = db_path
        self.conn = None

    def start_connection(self) -> None:
        
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
    
    def disconnect(self):
        if self.conn : 
            self.conn.close()
            self.conn = None 
    
    def execute_query(self, query , params : tuple = ()):

        if self.conn is None :
            self.start_connection
        
        cursor = self.conn.execute(query , params)
        self.conn.commit()
        return [dict(row) for row in cursor.fetchall()]


    
    
    
        