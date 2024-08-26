import requests
import time
import sys
import signal
import json

def logo():
    """Print the ASCII logo."""
    logo_text = """
  ____        _      _    _____       _               
 / __ \      (_)    | |  |_   _|     | |              
| |  | |_   _ _  ___| | __ | |  _ __ | |__   _____  __
| |  | | | | | |/ __| |/ / | | | '_ \| '_ \ / _ \ \/ /
| |__| | |_| | | (__|   < _| |_| | | | |_) | (_) >  < 
  \___\_\\__,_|_|\___|_|\_\_____|_| |_|_.__/ \___/_/\_\ 


|--------------------------------------------------------------------|
| Created By: Krishna Gopal Jha                                      |
| Checkout my LinkedIn: https://www.linkedin.com/in/krishnagopaljha/ |
| Lookup at my insta: https://instagram.com/theindianpsych           |
|--------------------------------------------------------------------|
 """
    print(logo_text)

def generate_email(name):
    """Generate a personalized email address."""
    sanitized_name = name.strip().lower().replace(' ', '.')
    domain = '1secmail.com'
    email = f"{sanitized_name}@{domain}"
    return email

def check_inbox(email):
    """Check the inbox of the generated email."""
    username, domain = email.split('@')
    url = f'https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        messages = response.json()
        return messages
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return []

def get_email_content(email, message_id):
    """Retrieve the content of a specific email."""
    username, domain = email.split('@')
    url = f'https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain}&id={message_id}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        message_content = response.json()
        return message_content
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return {}

def dispose_email(email):
    """Dispose of the email address."""
    username, domain = email.split('@')
    url = f'https://www.1secmail.com/api/v1/?action=deleteMailbox&login={username}&domain={domain}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        if response.status_code == 200:
            print(f"Email address {email} has been successfully disposed of.")
        else:
            print(f"Failed to dispose of email address {email}.")
    except requests.RequestException as e:
        print(f"Request error: {e}")

def print_progress_indicator():
    """Print a progress indicator with dots."""
    for i in range(3):
        sys.stdout.write(f'\rChecking inbox {"." * (i + 1)}')
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write('\r' + ' ' * 20 + '\r')  # Clear the line

def signal_handler(sig, frame):
    """Handle termination signals."""
    print("\nWe will miss you later but first let me dispose this email...")
    dispose_email(email)
    sys.exit(0)

def save_email_content(sender_name, content):
    """Save email content to a file named after the sender."""
    filename = f"{sender_name}.txt"
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Email from {sender_name} saved to {filename}")

def main():
    logo()  # Print the ASCII logo at the top
    global email
    name = input("What's your secret name?")
    print(f"Hello, {name}! Getting an exclusive email just for you...")
    
    email = generate_email(name)
    print(f"Your temporary email address is: {email}")

    # Register signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    processed_messages = set()
    
    while True:
        print_progress_indicator()
        messages = check_inbox(email)
        for message in messages:
            message_id = message['id']
            sender_name = message['from']
            if message_id not in processed_messages:
                print(f"New email from: {sender_name}")
                content = get_email_content(email, message_id)
                email_content = content.get('textBody', 'No content available')
                
                save_email_content(sender_name, email_content)
                processed_messages.add(message_id)
        time.sleep(1)  # Check every second

if __name__ == "__main__":
    main()
