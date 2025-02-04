import redis
import time
import logging
# from validation import validate_receive_data
import validation

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def handle_message(channel, data):
    if channel == 'file_content':
        if validation.validate_receive_data(data):
            logging.info("File content data is valid and can be processed.")
        else:
            logging.warning("File content data validation failed.")
    elif channel == 'move':
        if validation.validate_move_data(data):
            logging.info("File content data is valid and can be processed.")
        else:
            logging.warning("File content data validation failed.")
    elif channel == 'docking':
        if validation.validate_docking_data(data):
            logging.info("File content data is valid and can be processed.")
        else:
            logging.warning("File content data validation failed.")
    elif channel == 'kivaturn':
        if validation.validate_kivaturn_data(data):
            logging.info("File content data is valid and can be processed.")
        else:
            logging.warning("File content data validation failed.")
    elif channel == 'cancel':
        if validation.validate_cancel_data(data):
            logging.info("File content data is valid and can be processed.")
        else:
            logging.warning("File content data validation failed.")
    elif channel == 'pause':
        if validation.validate_pause_data(data):
            logging.info("File content data is valid and can be processed.")
        else:
            logging.warning("File content data validation failed.")
    elif channel == 'resume':
        if validation.validate_resume_data(data):
            logging.info("File content data is valid and can be processed.")
        else:
            logging.warning("File content data validation failed.")
    elif channel == 'speedcontrol':
        if validation.validate_speedcontrol_data(data):
            logging.info("File content data is valid and can be processed.")
        else:
            logging.warning("File content data validation failed.")
    elif channel == 'drivejog':
        if validation.validate_drivejog_data(data):
            logging.info("File content data is valid and can be processed.")
        else:
            logging.warning("File content data validation failed.")
    elif channel == 'alarmclear':
        if validation.validate_alarmclear_data(data):
            logging.info("File content data is valid and can be processed.")
        else:
            logging.warning("File content data validation failed.")
    elif channel == 'setmap':
        if validation.validate_setmap_data(data):
            logging.info("File content data is valid and can be processed.")
        else:
            logging.warning("File content data validation failed.")
    elif channel == 'initpose':
        if validation.validate_initpose_data(data):
            logging.info("File content data is valid and can be processed.")
        else:
            logging.warning("File content data validation failed.")
            
    else:
        logging.warning(f"Unknown channel: {channel}, skipping...")

def subscribe(channels=None, host='localhost', port=6379):
    if channels is None:
        channels = ['file_content', 'move', 'docking', 'kivaturn', 'cancel', 'pause', 'resume', 'speedcontrol', 'drivejog', 'alarmclear', 'setmap', 'initpose' ]  
    
    try:
        r = redis.Redis(host=host, port=port, db=0, socket_connect_timeout=5)
        pubsub = r.pubsub()
        pubsub.subscribe(*channels) 

        logging.info(f"Successfully connected to Redis. Listening to channels: {', '.join(channels)}...")
        
        for message in pubsub.listen():
            if message['type'] == 'message':
                data = message['data'].decode('utf-8')
                channel = message['channel'].decode('utf-8') 
                logging.info(f"Received message on channel {channel}: {data}")

                
                handle_message(channel, data)
                    
    except (redis.exceptions.ConnectionError, redis.exceptions.TimeoutError) as e:
        logging.error(f"Connection error: {e}. Reconnecting in 5 seconds...")
        time.sleep(5)
        subscribe(channels, host, port) 
    
    except KeyboardInterrupt:
        logging.info("Manually stopped listening.")
    
    except Exception as e:
        logging.error(f"Unexpected error: {e}. Reconnecting in 2 seconds...")
        time.sleep(2)
        subscribe(channels, host, port) 

if __name__ == "__main__":
    subscribe(channels=['file_content', 'user_data', 'order_data']) 
