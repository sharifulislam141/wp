import os
import time
import requests

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '6960679877:AAHJ4ZHofh1J4suiWXyrMCda1q0-DTiq7dM'

def read_last_line(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return lines[-1] if lines else ''

def send_to_telegram(message):
    # Replace 'YOUR_CHAT_ID' with your actual chat ID
    chat_id = '6015288409'
    
    # Telegram Bot API endpoint for sending messages
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    
    # Message payload
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'Markdown'
    }
    
    # Send the message using the requests library
    response = requests.post(url, json=payload)
    
    # Check the response status
    if response.status_code != 200:
        print(f"Failed to send message. Status code: {response.status_code}")
        print(response.text)

def main(file_path):
    # Initial read to get the last processed line
    last_line = read_last_line(file_path)
    
    while True:
        # Get the current size of the file
        current_size = os.path.getsize(file_path)
        
        if current_size > os.path.getsize(file_path):
            # File has been modified
            new_last_line = read_last_line(file_path)
            
            if new_last_line != last_line:
                # New lines detected, send them to Telegram
                send_to_telegram(f'New Line: {new_last_line}')
                
                # Update the last processed line
                last_line = new_last_line

        # Sleep for a while before checking again
        time.sleep(5)

if __name__ == "__main__":
    file_path =  'result.txt'
    main(file_path)
