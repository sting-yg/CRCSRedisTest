import redis
import time
import logging
import signal
import sys
import validation

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def handle_message(channel, data):
    print("=" * 150)
    try:
        if channel == 'task':
            validation.validate_task_data(data)
        elif channel == 'cmd.move':
            validation.validate_move_data(data)
        elif channel == 'cmd.docking':
            validation.validate_docking_data(data)
        elif channel == 'cmd.kiva-turn':
            validation.validate_kivaturn_data(data)
        elif channel == 'cmd.cancel-activity':
            validation.validate_cancel_data(data)
        elif channel == 'cmd.pause':
            validation.validate_pause_data(data)
        elif channel == 'cmd.resume':
            validation.validate_resume_data(data)
        elif channel == 'cmd.control-speed':
            validation.validate_speedcontrol_data(data)
        elif channel == 'cmd.drive-jog':
            validation.validate_drivejog_data(data)
        elif channel == 'cmd.clear-alarm':
            validation.validate_alarmclear_data(data)
        elif channel == 'cmd.set-map':
            validation.validate_setmap_data(data)
        elif channel == 'cmd.init-pose':
            validation.validate_initpose_data(data)
        # elif channel == 'broadcast.heartbeat.navigation':
        #     validation.validate_initpose_data(data)
        # elif channel == 'event.navigation-alarm-occurred	':
        #     validation.validate_initpose_data(data)
        # elif channel == 'status.navigation':
        #     validation.validate_initpose_data(data)
        # elif channel == 'status.navigation-mileage':
        #     validation.validate_initpose_data(data)
        # elif channel == 'status.lidar':
        #     validation.validate_initpose_data(data)
        # elif channel == 'status.camera':
        #     validation.validate_initpose_data(data)
        else:
            logging.warning(f"Unknown channel: {channel}, skipping...")
    except Exception as e:
        print("=" * 150)
        logging.error(f"Error handling data for channel {channel}: {e}")

def subscribe(channels=None, host='localhost', port=6379):
    if channels is None:
        channels = [
                    'task', 
                    'cmd.move', 
                    'cmd.docking', 
                    'cmd.kiva-turn', 
                    'cmd.cancel-activity', 
                    'cmd.pause', 
                    'cmd.resume', 
                    'cmd.control-speed', 
                    'cmd.drive-jog', 
                    'cmd.clear-alarm', 
                    'cmd.set-map', 
                    'cmd.init-pose'
                    # 'broadcast.heartbeat.navigation',
                    # 'event.navigation-alarm-occurred	',
                    # 'status.navigation',
                    # 'status.navigation-mileage',
                    # 'status.lidar',
                    # 'status.camera'
                    ]

    try:
        r = redis.Redis(host=host, port=port, db=0, socket_connect_timeout=5)
        pubsub = r.pubsub()
        pubsub.subscribe(*channels) 

        logging.info(f"Successfully connected to Redis. Listening to channels: {', '.join(channels)}...")

        while True:  # Change to while loop to continuously check for messages
            message = pubsub.get_message()  # Non-blocking method to get a message
            if message:
                if message['type'] == 'message':
                    data = message['data'].decode('utf-8')
                    channel = message['channel'].decode('utf-8')
                    handle_message(channel, data)
            time.sleep(0.01)  # Wait for a while to avoid high CPU usage

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

def signal_handler(sig, frame):
    logging.info('Exiting gracefully...')
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)  # Handle Ctrl+C
    subscribe(channels=['task', 
                        'cmd.move', 
                        'cmd.docking', 
                        'cmd.kiva-turn', 
                        'cmd.cancel-activity', 
                        'cmd.pause', 
                        'cmd.resume', 
                        'cmd.control-speed', 
                        'cmd.drive-jog', 
                        'cmd.clear-alarm', 
                        'cmd.set-map', 
                        'cmd.init-pose']) 
