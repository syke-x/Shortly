from dataclasses import dataclass , field
from datetime import datetime


@dataclass 
class User :

    
    user_id : int 
    name : str 
    email : str 
    hash_password : str 
    created_at : datetime = field(default_factory=datetime)