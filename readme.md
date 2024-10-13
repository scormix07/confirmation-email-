# SOC Automation Project

## Overview
This project automates the process of sending a confirmation to a client after a new case is created in TheHive. The confirmation can be sent via email or SMS.

### Files:
- `main.py`: Main script that retrieves the latest case from TheHive and triggers notifications.
- `config.py`: Configuration file holding all API keys, email settings, and URLs.
- `notifications.py`: Contains functions to send email or SMS notifications.

### How to Run:
1. Set the required environment variables:
   - `HIVE_API_KEY`
   - `SMTP_USER`
   - `SMTP_PASS`
   - `CLIENT_EMAIL`
   - (If using SMS) `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER`

2. Install dependencies:
