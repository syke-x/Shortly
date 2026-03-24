from abc import ABC , abstractmethod
<<<<<<< HEAD
from sqlite3 import connect
=======
>>>>>>> e2563c5136eac518b6321c312eecfea85e86d7b9

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


<<<<<<< HEAD
class SQLiteConnection(Connection):

    def __init__(self , db_path : str) : 
        self.db_path = db_path

        

=======
>>>>>>> e2563c5136eac518b6321c312eecfea85e86d7b9
