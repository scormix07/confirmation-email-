import os

# Configuration for TheHive API
HIVE_URL = 'https://your-hive-instance.com/api/case'
HIVE_API_KEY = os.getenv('HIVE_API_KEY')  # Store API key in environment variables

# Email Configuration
SMTP_SERVER = 'smtp.your-email-provider.com'
SMTP_PORT = 587
SMTP_USER = os.getenv('SMTP_USER')
SMTP_PASS = os.getenv('SMTP_PASS')
CLIENT_EMAIL = os.getenv('CLIENT_EMAIL')

# SMS Configuration (if using Twilio)
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
