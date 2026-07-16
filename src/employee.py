from dataclasses import dataclass
from datetime import date

@dataclass
class Employee:
    first_name: str
    last_name: str
    age: int 
    department : str
    position : str
    salary : float
    email : str
    phone : str
    hire_date : date