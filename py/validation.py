import logging
import json
from pydantic import ValidationError
from Task import ExpectedTaskStructure
import command

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_validation_result(channel: str, success: bool):
    if success:
        logging.info(f"Channel :[{channel}] ---- data validation Success.")
    else:
        logging.warning(f"Channel :[{channel}] ---- data validation Failure.")

def validate_task_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = ExpectedTaskStructure(**parsed_data)  
        log_validation_result('task', True)  
        return True
    except ValidationError as e:
        log_validation_result('task', False)  
        return False
def validate_move_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = command.ExpectedMoveActivity(**parsed_data)  
        log_validation_result('cmd.move', True)  
        return True
    except ValidationError as e:
        log_validation_result('cmd.move', False)  
        return False
def validate_docking_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = command.ExpectedDockingActivity(**parsed_data)  
        log_validation_result('cmd.docking', True)  
        return True
    except ValidationError as e:
        log_validation_result('cmd.docking', False)  
        return False
def validate_kivaturn_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = command.ExpectedKivaTurnActivity(**parsed_data)  
        log_validation_result('cmd.kiva-turn', True)  
        return True
    except ValidationError as e:
        log_validation_result('cmd.kiva-turn', False)  
        return False
def validate_cancel_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = command.ExpectedCancelActivity(**parsed_data)  
        log_validation_result('cmd.cancel-activity', True)  
        return True
    except ValidationError as e:
        log_validation_result('cmd.cancel-activity', False)  
        return False
def validate_pause_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = command.ExpectedPause(**parsed_data)  
        log_validation_result('cmd.pause', True)  
        return True
    except ValidationError as e:
        log_validation_result('cmd.pause', False)  
        return False 
def validate_resume_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = command.ExpectedResume(**parsed_data)  
        log_validation_result('cmd.resume', True)  
        return True
    except ValidationError as e:
        log_validation_result('cmd.resume', False)  
        return False 
def validate_speedcontrol_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = command.ExpectedSpeedControl(**parsed_data)  
        log_validation_result('cmd.control-speed', True)  
        return True
    except ValidationError as e:
        log_validation_result('cmd.control-speed', False)  
        return False 
def validate_drivejog_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = command.ExpectedDriveJog(**parsed_data)  
        log_validation_result('cmd.drive-jog', True)  
        return True
    except ValidationError as e:
        log_validation_result('cmd.drive-jog', False)  
        return False 
def validate_alarmclear_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = command.ExpectedAlarmClear(**parsed_data)  
        log_validation_result('cmd.clear-alarm', True)  
        return True
    except ValidationError as e:
        log_validation_result('cmd.clear-alarm', False)  
        return False
def validate_setmap_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = command.ExpectedSetMap(**parsed_data)  
        log_validation_result('cmd.set-map', True)  
        return True
    except ValidationError as e:
        log_validation_result('cmd.set-map', False)  
        return False
def validate_initpose_data(data: str) -> bool:
    try:
        parsed_data = json.loads(data)  
        task = command.ExpectedInitPose(**parsed_data)  
        log_validation_result('cmd.init-pose', True)  
        return True
    except ValidationError as e:
        log_validation_result('cmd.init-pose', False)  
        return False
