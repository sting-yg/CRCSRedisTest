import redis
import time
import logging
import signal
import sys
import validation

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def subscribe(channels=None, host='localhost', port=6379):
    r = redis.Redis(host=host, port=port, db=0, socket_connect_timeout=5)
    pubsub = r.pubsub()
    pubsub.subscribe(*channels)

    logging.info(f"Successfully connected to Redis. Listening to channels: {', '.join(channels)}...")

    while True:
        try:
            message = pubsub.get_message()  # Non-blocking method to get a message
            if message:
                if message['type'] == 'message':
                    data = message['data'].decode('utf-8')
                    channel = message['channel'].decode('utf-8')
                    validation.validate_data(channel, data)
            time.sleep(0.01)  # Wait for a while to avoid high CPU usage

        except (redis.exceptions.ConnectionError, redis.exceptions.TimeoutError) as e:
            logging.error(f"Connection error: {e}. Reconnecting in 5 seconds...")
            time.sleep(5)
            continue  # Keep looping, try reconnecting

        except KeyboardInterrupt:
            logging.info("Manually stopped listening.")
            break  # Exit the loop gracefully

        except Exception as e:
            logging.error(f"Unexpected error: {e}. Reconnecting in 2 seconds...")
            time.sleep(2)
            continue  # Keep looping, try reconnecting

def signal_handler(sig, frame):
    logging.info('Exiting gracefully...')
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)  # Handle Ctrl+C
    subscribe(channels=['frontMoveStop',
                        'backMoveStop',
                        'frontMoveArcStop',
                        'backMoveArcStop',
                        # 'cmd.move',
                        # 'cmd.docking',
                        # 'cmd.kiva-turn',
                        # 'cmd.cancel-activity',
                        # 'cmd.pause',
                        # 'cmd.resume',
                        # 'cmd.control-speed',
                        # 'cmd.drive-jog',
                        # 'cmd.clear-alarm',
                        # 'cmd.set-map',
                        # 'cmd.init-pose',
                        # 'cmd.conveyor',
                        # 'cmd.lift',
                        # 'cmd.start-charge',
                        # 'cmd.stop-charge',
                        # 'cmd.tableturn',
                        # 'cmd.control-ptz',
                        # 'cmd.get-picture',
                        # 'cmd.upload-request',
                        # 'cmd.set-sound',
                        # 'cmd.set-led'
                        ])
