# Webhook Checker

This is a simple Python script to check if a Discord webhook URL is valid or not. It sends a GET request to the provided URL and checks if the response contains specific strings indicating an invalid or unknown webhook. If the URL is valid, it prints a message saying so, and if it is invalid, it prints an error message.

## Prerequisites
- Python 3
- requests library

## Usage
1. Clone the repository or download the `main.py` file.
2. Install the requests library by running `pip install requests` in your command line.
3. Run `python main.py` in your command line.
4. Enter the webhook URL you want to check when prompted.
5. The script will output whether the webhook URL is valid or not.

## Disclaimer
This script is not foolproof and may not catch all invalid webhook URLs. It is simply a quick way to check if a webhook URL is likely to work or not.
