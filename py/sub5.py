import redis
import json
import time

# 目标数据结构（用于数据验证）
EXPECTED_STRUCTURE = {
    "activityType": int,
    "index": int,
    "id": str,
    "isAsync": bool,
    "isTaskOverridable": bool,
    "palletSize": (type(None), int),
    "palletHeight": int,
    "moveParameter": dict,  # moveParameter 
    "dockingInParameter": dict,  # dockingInParameter 
    "dockingOutParameter": dict,  # dockingOutParameter 
    "conveyorParameter": dict,  # conveyorParameter 
    "standbyParameter": dict,  # standbyParameter 
    "chargeStartParameter": dict,  # chargeStartParameter 
    "tableTurnParameter": dict,  # tableTurnParameter 
    "kivaTurnParameter": dict,  # kivaTurnParameter 
    "liftParameter": dict,  # liftParameter 
    "controlPtzParameter": dict,  # controlPtzParameter 
    "getPictureParameter": dict,  # getPictureParameter 
    "uploadRequestParameter": dict,  # uploadRequestParameter 
    "visible": bool
}

# pathList 子项的预期结构
EXPECTED_PATH_STRUCTURE = {
    "index": int,
    "node": str,
    "x": float,
    "y": float,
    "angle": float,
    "actionType": int,
    "isArc": bool,
    "arcRadius": float,
    "arcControlPointX": float,
    "arcControlPointY": float,
    "speed": float,
    "obstacleDetectionDistance": list,  
    "obstacleDetectionAreaAtTarget": list  
}

# moveParameter 
EXPECTED_MOVE_PARAMETER = {
    "driveType": int,
    "pathList": list,  
    "doAlign": (bool, type(None)),  
    "alignAngle": (float, type(None))  
}

# dockingInParameter 子项的预期结构
EXPECTED_DOCKING_IN_PARAMETER = {
    "driveType": int,
    "pathList": list
}

# dockingOutParameter 子项的预期结构
EXPECTED_DOCKING_OUT_PARAMETER = {
    "driveType": int,
    "pathList": list
}

# conveyorParameter 子项的预期结构
EXPECTED_CONVEYOR_PARAMETER = {
    "actionType": int,
    "productInOutType": int,
    "speed": int,
    "productCount": int,
    "useProductCheck": bool,
    "pioSideType": int,
    "pioComType": int,
    "pioId": str,
    "pioChannel": int
}

# standbyParameter 子项的预期结构
EXPECTED_STANDBY_PARAMETER = {
    "seconds": int,
    "useBatterySaving": bool
}

# chargeStartParameter 子项的预期结构
EXPECTED_CHARGE_START_PARAMETER = {
    "pioSideType": int,
    "pioComType": int,
    "pioId": str,
    "pioChannel": int,
    "ignoreFail": bool
}

# tableTurnParameter 子项的预期结构
EXPECTED_TABLE_TURN_PARAMETER = {
    "targetAngle": float,
    "speed": float
}

# kivaTurnParameter 子项的预期结构
EXPECTED_KIVA_TURN_PARAMETER = {
    "targetAngle": float,
    "speed": float
}

# liftParameter 子项的预期结构
EXPECTED_LIFT_PARAMETER = {
    "actionType": int,
    "height": float,
    "speed": float,
    "useProductCheck": bool
}

# controlPtzParameter 子项的预期结构
EXPECTED_CONTROL_PTZ_PARAMETER = {
    "pan": float,
    "tilt": float,
    "zoom": float
}

# getPictureParameter 子项的预期结构
EXPECTED_GET_PICTURE_PARAMETER = {
    "camId": int,
    "photoNum": int,
    "interval": int,
    "saveLocal": bool,
    "description": str,
    "uploadServer": bool,
    "directoryName": str,
    "nodeName": str
}

# uploadRequestParameter 子项的预期结构
EXPECTED_UPLOAD_REQUEST_PARAMETER = {
    "url": str,
    "directoryName": str
}