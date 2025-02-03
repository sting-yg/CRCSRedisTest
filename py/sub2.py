import redis
import json
import time

# 目标数据结构（用于数据验证）
EXPECTED_STRUCTURE = {
    "topicId": str,
    "activityId": str,
    "driveType": int,
    "doAlign": (bool, type(None)),  # 可选字段 (bool or None)
    "alignAngle": (float, type(None)),  # 可选字段 (float or None)
    "pathList": list  # 这里是列表，内部检查结构
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

def is_valid_path_item(item):
    """ 验证 pathList 中的每个元素是否符合要求 """
    if not isinstance(item, dict):
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
        if not isinstance(data[key], expected_type):
            print(f"Invalid type for {key}: Expected {expected_type}, got {type(data[key])}")
            return False

    # 进一步检查 pathList
    if isinstance(data["pathList"], list):
        for item in data["pathList"]:
            if not is_valid_path_item(item):
                print("Invalid pathList item")
                return False
    else:
        print("pathList is not a list")
        return False

    print("Valid move data received")
    return True


def subscribe_forever(channel='move', host='localhost', port=6379):
    """ 监听 Redis 频道，并校验 move 频道的数据 """
    while True:
        try:
            # 创建 Redis 连接
            r = redis.Redis(host=host, port=port, db=0, socket_connect_timeout=5)
            pubsub = r.pubsub()
            pubsub.subscribe(channel)

            print(f"Successfully connected to Redis. Listening to channel: {channel}...")

            # 持续监听消息
            for message in pubsub.listen():
                if message['type'] == 'message':
                    data = message['data'].decode('utf-8')  # 解码 Redis 消息
                    print(f"Received message: {data}")
                    
                    # 校验数据
                    if validate_move_data(data):
                        print("✔ Data is valid and can be processed.")
                    else:
                        print("❌ Data validation failed.")

        except (redis.exceptions.ConnectionError, redis.exceptions.TimeoutError) as e:
            print(f"Connection error: {e}. Reconnecting in 5 seconds...")
            time.sleep(5)
        except KeyboardInterrupt:
            print("Manually stopped listening")
            break
        except Exception as e:
            print(f"Unknown error: {e}. Reconnecting in 10 seconds...")
            time.sleep(10)


if __name__ == "__main__":
    subscribe_forever()
