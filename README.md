# QuickInbox

This Python script generates a temporary email address, checks for new emails, and saves the content of each email to a file named after the sender. The script also includes a progress indicator and handles termination signals to clean up the email address.

## Features

- Generates a temporary email address.
- Checks the inbox for new messages.
- Saves email content to a file named after the sender.
- Have in built email disposal feature triggered by CTRL+C.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/krishnagopaljha/quickinbox.git
    cd quickinbox
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```sh
    python quickinbox.py
    ```

2. Enter your secret name when prompted to generate a temporary email address.

3. The script will periodically check the inbox for new messages and save the content to files.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
