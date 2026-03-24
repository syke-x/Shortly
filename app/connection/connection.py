from abc import ABC , abstractmethod
from sqlite3 import connect

class Connection(ABC):

    @abstractmethod
    def start_connection(self , db_path ):
        pass

    @abstractmethod
    def disconnect(self , db_path):
        pass

    @abstractmethod
    def execute_query(self , query : str) : 
        pass 


class SQLiteConnection(Connection):

    def __init__(self , db_path : str) : 
        self.db_path = db_path

        

