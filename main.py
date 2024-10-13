import requests
from config import HIVE_URL, HIVE_API_KEY
from notifications import send_confirmation_email, send_confirmation_sms

# Set headers for TheHive API
HEADERS = {
    'Authorization': f'Bearer {HIVE_API_KEY}',
    'Content-Type': 'application/json'
}

# Function to get the latest case from TheHive
def get_latest_case():
    try:
        response = requests.get(HIVE_URL, headers=HEADERS)
        response.raise_for_status()  # Raises error if status code is not 200
        cases = response.json()
        return cases[0]  # Return the latest case
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    return None

# Main Logic
if __name__ == "__main__":
    latest_case = get_latest_case()
    if latest_case:
        # Send both email and SMS (choose depending on your preference)
        send_confirmation_email(latest_case)
        send_confirmation_sms(latest_case, '+1234567890')  # Replace with client phone number
