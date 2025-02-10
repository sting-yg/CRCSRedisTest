import redis
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Mapping of file names to Redis channels
file_channel_map = {
    'Task.txt': 'task',
    'Move.txt': 'cmd.move',
    'Docking.txt': 'cmd.docking',
    'KivaTurn.txt': 'cmd.kiva-turn',
    'Cancel.txt': 'cmd.cancel-activity',
    'Pause.txt': 'cmd.pause',
    'Resume.txt': 'cmd.resume',
    'SpeedControl.txt': 'cmd.control-speed',
    'DriveJog.txt': 'cmd.drive-jog',
    'AlarmClear.txt': 'cmd.clear-alarm',
    'SetMap.txt': 'cmd.set-map',
    'InitPose.txt': 'cmd.init-pose',
    'Conveyor.txt' : 'cmd.conveyor',
    'Lift.txt' : 'cmd.lift',
    'ChargeStart.txt' : 'cmd.start-charge',
    'ChargeStop.txt' : 'cmd.stop-charge',
    'TableTurn.txt' : 'cmd.tableturn',
    'ControlPtz.txt' : 'cmd.control-ptz',
    'GetPicture' : 'cmd.get-picture',
    'UploadRequest.txt' : 'cmd.upload-request',
    'SetSound.txt' : 'cmd.set-sound',
    'SetLed.txt' : 'cmd.set-led'
}

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, redis_conn):
        self.r = redis_conn

    def send_file_content(self, file_name):
        """ Read file content and send to Redis channel """
        file_path = os.path.join('com', file_name)  # Read files from 'com/' directory
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                new_content = f.read()
                channel = file_channel_map[file_name]
                self.r.publish(channel, new_content)
                print(f"Sent content of {file_name} to channel: {channel}")
        except Exception as e:
            print(f"Failed to send updated content for {file_name}: {e}")

def list_channels():
    """ List all available channels with their corresponding numbers """
    print("Available channels:")
    for i, (file_name, channel) in enumerate(file_channel_map.items(), start=1):
        print(f"{i}. {channel} (File: {file_name})")

def main():
    r = redis.Redis(host='localhost', port=6379, db=0)
    observer = Observer()

    event_handler = FileChangeHandler(r)

    while True:
        # Display all available channels with numbers
        print("=" * 150)
        list_channels()

        # Get user input for channel selection
        try:
            channel_number = int(input("\nEnter the number corresponding to the channel you want to send content from (or 0 to exit): "))
            if channel_number == 0:
                print("Exiting the program...")
                break  # Exit the loop if the user enters 0

            if 1 <= channel_number <= len(file_channel_map):
                selected_file = list(file_channel_map.keys())[channel_number - 1]
                print(f"Selected file: {selected_file}")
                
                # Send content of selected file to Redis channel
                event_handler.send_file_content(selected_file)
            else:
                print("Invalid input, please enter a valid number from the list.")
                continue
        except ValueError:
            print("Invalid input, please enter a valid number.")
            continue

    observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
