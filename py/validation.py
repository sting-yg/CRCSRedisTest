from pydantic import ValidationError
from structure import ExpectedTaskStructure
import command
import json

def validate_receive_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = ExpectedTaskStructure(**parsed_data)  
        return True 
    except ValidationError as e:
        return False 
def validate_move_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = command.ExpectedMoveActivity(**parsed_data)  
        return True 
    except ValidationError as e:
        return False 
def validate_docking_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = command.ExpectedDockingActivity(**parsed_data)  
        return True 
    except ValidationError as e:
        return False 
def validate_kivaturn_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = command.ExpectedKivaTurnActivity(**parsed_data)  
        return True 
    except ValidationError as e:
        return False 
def validate_cancel_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = command.ExpectedCancelActivity(**parsed_data)  
        return True 
    except ValidationError as e:
        return False 
def validate_pause_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = command.ExpectedPause(**parsed_data)  
        return True 
    except ValidationError as e:
        return False 
def validate_resume_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = command.ExpectedResume(**parsed_data)  
        return True 
    except ValidationError as e:
        return False 
def validate_speedcontrol_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = command.ExpectedSpeedControl(**parsed_data)  
        return True 
    except ValidationError as e:
        return False 
def validate_drivejog_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = command.ExpectedDriveJog(**parsed_data)  
        return True 
    except ValidationError as e:
        return False 
def validate_alarmclear_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = command.ExpectedAlarmClear(**parsed_data)  
        return True 
    except ValidationError as e:
        return False 
def validate_setmap_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = command.ExpectedSetMap(**parsed_data)  
        return True 
    except ValidationError as e:
        return False 
def validate_initpose_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = command.ExpectedInitPose(**parsed_data)  
        return True 
    except ValidationError as e:
        return False 
