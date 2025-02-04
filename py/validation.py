from pydantic import ValidationError
from structure import ExpectedTaskStructure
import json

def validate_receive_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = ExpectedTaskStructure(**parsed_data)  
        return True 
    except ValidationError as e:
        return False 
