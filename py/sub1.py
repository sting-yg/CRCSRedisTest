import redis
import time

def subscribe_forever(channel='file_channel', host='localhost', port=6379):
    while True:
        try:
            # Create new connection
            r = redis.Redis(host=host, port=port, db=0, socket_connect_timeout=5)
            pubsub = r.pubsub()
            pubsub.subscribe(channel)

            print(f"Successfully connected to Redis. Listening to channel: {channel}...")

            # Continuous message listening
            for message in pubsub.listen():
                if message['type'] == 'message':
                    data = message['data'].decode('utf-8')
                    print(f"Received message: {data}")
            for channel in pubsub.channels:
                channel == ''
                    
                channel == ''

        except (redis.exceptions.ConnectionError, 
                redis.exceptions.TimeoutError) as e:
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