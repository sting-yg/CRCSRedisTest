import redis
import os

# List of channels (no longer associated with a file)
channel_list = [
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
    'cmd.init-pose',
]

class FileSender:
    def __init__(self, redis_conn, input_file='input.txt'):
        self.r = redis_conn
        self.input_file = input_file

    def send_to_channel(self, channel):
        """ Read content from input.txt and send to the specified Redis channel """
        try:
            with open(self.input_file, 'r', encoding='utf-8') as f:
                content = f.read()
                self.r.publish(channel, content)
                print(f"Sent content of {self.input_file} to channel: {channel}")
        except Exception as e:
            print(f"Failed to send updated content: {e}")

def list_channels():
    """ List all available channels """
    print("Available channels:")
    for i, channel in enumerate(channel_list, start=1):
        print(f"{i}. {channel}")

def main():
    r = redis.Redis(host='localhost', port=6379, db=0)
    file_sender = FileSender(r)

    while True:
        print("=" * 150)
        list_channels()

        # Get the channel number selected by the user
        try:
            channel_number = int(input("\nEnter the number of the channel you want to send content to (or 0 to exit): "))
            if channel_number == 0:
                print("Exiting the program...")
                break

            if 1 <= channel_number <= len(channel_list):
                selected_channel = channel_list[channel_number - 1]
                print(f"Selected channel: {selected_channel}")
                
                # Send content from input.txt to the selected channel
                file_sender.send_to_channel(selected_channel)
            else:
                print("Invalid input, please enter a valid number from the list.")
        except ValueError:
            print("Invalid input, please enter a number.")

if __name__ == "__main__":
    main()
