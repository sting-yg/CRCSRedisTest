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
    "moveParameter": dict,  # moveParameter 是字典，需要进一步验证内部结构
    "dockingInParameter": dict,  # dockingInParameter 是字典，需要进一步验证内部结构
    "dockingOutParameter": dict,  # dockingOutParameter 是字典，需要进一步验证内部结构
    "conveyorParameter": dict,  # conveyorParameter 是字典，需要进一步验证内部结构
    "standbyParameter": dict,  # standbyParameter 是字典，需要进一步验证内部结构
    "chargeStartParameter": dict,  # chargeStartParameter 是字典，需要进一步验证内部结构
    "tableTurnParameter": dict,  # tableTurnParameter 是字典，需要进一步验证内部结构
    "kivaTurnParameter": dict,  # kivaTurnParameter 是字典，需要进一步验证内部结构
    "liftParameter": dict,  # liftParameter 是字典，需要进一步验证内部结构
    "controlPtzParameter": dict,  # controlPtzParameter 是字典，需要进一步验证内部结构
    "getPictureParameter": dict,  # getPictureParameter 是字典，需要进一步验证内部结构
    "uploadRequestParameter": dict,  # uploadRequestParameter 是字典，需要进一步验证内部结构
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
    "obstacleDetectionDistance": list,  # 应该是浮点数列表
    "obstacleDetectionAreaAtTarget": list  # 应该是浮点数列表
}

# moveParameter 子项的预期结构
EXPECTED_MOVE_PARAMETER = {
    "driveType": int,
    "pathList": list,  # 这项是列表，需要进一步检查列表内部的结构
    "doAlign": (bool, type(None)),  # 可选字段 (bool or None)
    "alignAngle": (float, type(None))  # 可选字段 (float or None)
}

# dockingInParameter 子项的预期结构
EXPECTED_DOCKING_IN_PARAMETER = {
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

# 校验 pathList 子项
def is_valid_path_item(item):
    """ 验证 pathList 中的每个元素是否符合要求 """
    if not isinstance(item, dict):
        print("Item is not a dictionary:", item)
        return False

    for key, expected_type in EXPECTED_PATH_STRUCTURE.items():
        if key not in item:
            print(f"Missing key in pathList item: {key}")
            return False

        # 特殊处理 obstacleDetectionDistance 和 obstacleDetectionAreaAtTarget
        if key in ["obstacleDetectionDistance", "obstacleDetectionAreaAtTarget"]:
            if not isinstance(item[key], list) or not all(isinstance(i, float) for i in item[key]):
                print(f"Invalid type for {key}: Expected list of float, got {item[key]}")
                return False
        else:
            if not isinstance(item[key], expected_type):
                print(f"Invalid type for {key}: Expected {expected_type}, got {type(item[key])}")
                return False

    return True

# 校验主数据结构
def validate_move_data(data):
    """ 验证 move 频道接收的数据格式 """
    try:
        data = json.loads(data)  # 解析 JSON 数据
    except json.JSONDecodeError:
        print("Invalid JSON format")
        return False

    # 检查主结构
    for key, expected_type in EXPECTED_STRUCTURE.items():
        if key not in data:
            print(f"Missing key: {key}")
            return False
        if isinstance(expected_type, tuple):
            if None in expected_type:
                if data[key] is None:
                    continue  # 跳过类型验证
            if not isinstance(data[key], expected_type[0]):
                print(f"Invalid type for {key}: Expected {expected_type[0]}, got {type(data[key])}")
                return False
        else:
            if not isinstance(data[key], expected_type):
                print(f"Invalid type for {key}: Expected {expected_type}, got {type(data[key])}")
                return False

    # 进一步检查 moveParameter
    if isinstance(data.get("moveParameter"), dict):
        for key, expected_type in EXPECTED_MOVE_PARAMETER.items():
            if key not in data["moveParameter"]:
                print(f"Missing key in moveParameter: {key}")
                return False
            if isinstance(expected_type, tuple):
                if not isinstance(data["moveParameter"][key], expected_type[0]) and data["moveParameter"][key] is not None:
                    print(f"Invalid type for {key} in moveParameter: Expected {expected_type[0]}, got {type(data['moveParameter'][key])}")
                    return False
            else:
                if not isinstance(data["moveParameter"][key], expected_type):
                    print(f"Invalid type for {key} in moveParameter: Expected {expected_type}, got {type(data['moveParameter'][key])}")
                    return False

        # 验证 pathList 内部元素
        if isinstance(data["moveParameter"]["pathList"], list):
            for item in data["moveParameter"]["pathList"]:
                if not is_valid_path_item(item):
                    print("Invalid pathList item")
                    return False
        else:
            print("moveParameter.pathList is not a valid list")
            return False
    else:
        print("moveParameter is not a valid dictionary")
        return False

    # 验证每个字典字段
    def validate_substructure(key, structure, sub_data):
        """ 验证字典字段的内部结构 """
        if isinstance(sub_data, dict):
            for sub_key, expected_type in structure.items():
                if sub_key not in sub_data:
                    print(f"Missing key in {key}: {sub_key}")
                    return False
                if isinstance(expected_type, tuple):
                    if not isinstance(sub_data[sub_key], expected_type[0]) and sub_data[sub_key] is not None:
                        print(f"Invalid type for {sub_key} in {key}: Expected {expected_type[0]}, got {type(sub_data[sub_key])}")
                        return False
                else:
                    if not isinstance(sub_data[sub_key], expected_type):
                        print(f"Invalid type for {sub_key} in {key}: Expected {expected_type}, got {type(sub_data[sub_key])}")
                        return False
        else:
            print(f"{key} is not a valid dictionary")
            return False

    # 验证每个子字典字段
    validate_substructure("dockingInParameter", EXPECTED_DOCKING_IN_PARAMETER, data.get("dockingInParameter"))
    validate_substructure("dockingOutParameter", EXPECTED_DOCKING_IN_PARAMETER, data.get("dockingOutParameter"))
    validate_substructure("conveyorParameter", EXPECTED_CONVEYOR_PARAMETER, data.get("conveyorParameter"))
    validate_substructure("standbyParameter", EXPECTED_STANDBY_PARAMETER, data.get("standbyParameter"))
    validate_substructure("chargeStartParameter", EXPECTED_CHARGE_START_PARAMETER, data.get("chargeStartParameter"))
    validate_substructure("tableTurnParameter", EXPECTED_TABLE_TURN_PARAMETER, data.get("tableTurnParameter"))
    validate_substructure("kivaTurnParameter", EXPECTED_KIVA_TURN_PARAMETER, data.get("kivaTurnParameter"))
    validate_substructure("liftParameter", EXPECTED_LIFT_PARAMETER, data.get("liftParameter"))
    validate_substructure("controlPtzParameter", EXPECTED_CONTROL_PTZ_PARAMETER, data.get("controlPtzParameter"))
    validate_substructure("getPictureParameter", EXPECTED_GET_PICTURE_PARAMETER, data.get("getPictureParameter"))
    validate_substructure("uploadRequestParameter", EXPECTED_UPLOAD_REQUEST_PARAMETER, data.get("uploadRequestParameter"))

    return True

# 示例：从 Redis 获取数据并验证
def fetch_and_validate_from_redis(redis_key):
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    data = r.get(redis_key)
    if data:
        data = data.decode('utf-8')  # 解码字节串为字符串
        is_valid = validate_move_data(data)
        return is_valid
    return False
