import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client
from config import SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASS, CLIENT_EMAIL, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER


# Function to send confirmation email to the client
def send_confirmation_email(case_details):
    msg = MIMEText(f"Case {case_details['title']} has been created.\nDescription: {case_details['description']}")
    msg['Subject'] = f"Case {case_details['id']} Created"
    msg['From'] = SMTP_USER
    msg['To'] = CLIENT_EMAIL

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(SMTP_USER, CLIENT_EMAIL, msg.as_string())
        server.quit()
        print('Confirmation email sent.')
    except Exception as e:
        print(f"Error sending email: {e}")


# Function to send SMS confirmation using Twilio
def send_confirmation_sms(case_details, client_phone_number):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        to=client_phone_number,
        from_=TWILIO_PHONE_NUMBER,
        body=f"Case {case_details['title']} has been created.\nDescription: {case_details['description']}"
    )
    print('Confirmation SMS sent.')
