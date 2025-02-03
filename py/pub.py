import redis
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, channel, redis_conn, file_path):
        self.channel = channel
        self.r = redis_conn
        self.last_content = None
        self.last_modified_time = 0
        self.debounce_time = 0.5
        self.file_path = file_path
        self.send_initial_content()

    def send_initial_content(self):

        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                initial_content = f.read().strip() 
                if initial_content: 
                    self.r.publish(self.channel, initial_content)
                    print(f'Initial content sent to channel: {self.channel}')
                    self.last_content = initial_content
        except Exception as e: 
            print(f'Failed to send initial content: {e}')

    def on_modified(self, event):
        if not event.is_directory and event.src_path == self.file_path:
            current_time  = time.time()
            if current_time - self.last_modified_time > self.debounce_time:
                if self.send_file_content(event.src_path):
                    self.last_modified_time = time.time()

    def send_file_content(self, file_path):

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                new_content = f.read()
                if new_content != self.last_content: #Avoid duplicate content
                    self.r.publish(self.channel, new_content)
                    print(f'Detected file change. sent new content to channel: {self.channel}')
                    self.last_content = new_content
                    return True # Send Success
        except Exception as e:
            print(f'Failed to send: {e}')
        
def main(): 
    r = redis.Redis(host="localhost", port=6379, db=0)
    channel = 'move'
    file_path = 'input.txt' # Target file to monitor

    event_handler = FileChangeHandler(channel, r, file_path)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    print(f'Started monitoring file changes: {file_path}...')

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
