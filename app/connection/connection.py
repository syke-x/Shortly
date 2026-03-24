from abc import ABC , abstractmethod

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


