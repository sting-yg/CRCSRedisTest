import redis
import time
import logging
from validation import validate_receive_data

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def subscribe(channel='file_content', host='localhost', port=6379):
    try:
        r = redis.Redis(host=host, port=port, db=0, socket_connect_timeout=5)
        pubsub = r.pubsub()
        pubsub.subscribe(channel)

        logging.info(f"Successfully connected to Redis. Listening to channel: {channel}...")
        
        for message in pubsub.listen():
            if message['type'] == 'message':
                data = message['data'].decode('utf-8')
                logging.info(f"Received message: {data}")

                if validate_receive_data(data):
                    logging.info("Data is valid and can be processed.")
                else:
                    logging.warning("Data validation failed.")
                    
    except (redis.exceptions.ConnectionError, redis.exceptions.TimeoutError) as e:
        logging.error(f"Connection error: {e}. Reconnecting in 5 seconds...")
        time.sleep(5)
        subscribe(channel, host, port) 
    
    except KeyboardInterrupt:
        logging.info("Manually stopped listening.")
    
    except Exception as e:
        logging.error(f"Unexpected error: {e}. Reconnecting in 2 seconds...")
        time.sleep(2)
        subscribe(channel, host, port) 

if __name__ == "__main__":
    subscribe()
