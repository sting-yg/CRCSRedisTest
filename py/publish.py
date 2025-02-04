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
    # 'HeartBeat.txt': 'broadcast.heartbeat.navigation',
    # 'AlarmOccurred.txt': 'event.navigation-alarm-occurred	',
    # 'NavigationStatus.txt': 'status.navigation',
    # 'NavigationMileage.txt': 'status.navigation-mileage',
    # 'LidarStatus.txt': 'status.lidar',
    # 'CameraStatus.txt': 'status.camera'
}

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, redis_conn):
        self.r = redis_conn
        self.last_content = {}  # Records the last content of each file to avoid sending the same content

        # Initialize last_content and send initial file contents
        for file_name in file_channel_map:
            file_path = os.path.join('com', file_name)  # Ensure correct path
            self.last_content[file_name] = None
            self.send_initial_content(file_path)

    def send_initial_content(self, file_path):
        """ First time send message to Redis channel """
        if not os.path.exists(file_path):
            print(f"Warning: {file_path} does not exist. Skipping initial content.")
            return

        try:
            file_name = os.path.basename(file_path)
            with open(file_path, 'r', encoding='utf-8') as f:
                initial_content = f.read()
                if initial_content != self.last_content.get(file_name):  # Avoid resending the same content
                    channel = file_channel_map[file_name]
                    self.r.publish(channel, initial_content)
                    print(f"Initial content of {file_name} sent to channel: {channel}")
                    self.last_content[file_name] = initial_content
        except Exception as e:
            print(f"Failed to send initial content for {file_path}: {e}")

    def on_modified(self, event):
        """ Listen for file modifications and send to the corresponding Redis channel """
        if event.is_directory:
            return  # Skip directory events

        file_name = os.path.basename(event.src_path)
        if file_name in file_channel_map:
            self.send_file_content(file_name)

    def send_file_content(self, file_name):
        """ Read file content and send to Redis channel """
        file_path = os.path.join('com', file_name)  # Read files from 'com/' directory
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                new_content = f.read()
                if new_content != self.last_content.get(file_name):  # Avoid resending identical content
                    channel = file_channel_map[file_name]
                    self.r.publish(channel, new_content)
                    print(f"Detected file change in {file_name}. Sent new content to channel: {channel}")
                    self.last_content[file_name] = new_content
        except Exception as e:
            print(f"Failed to send updated content for {file_name}: {e}")

def main():
    r = redis.Redis(host='localhost', port=6379, db=0)
    observer = Observer()

    # Monitor all files in the 'com' directory
    event_handler = FileChangeHandler(r)
    observer.schedule(event_handler, path='com', recursive=False)

    observer.start()
    print(f"Started monitoring: {list(file_channel_map.keys())} in 'com/' directory...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
