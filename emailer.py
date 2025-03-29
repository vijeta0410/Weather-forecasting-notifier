
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables

# Email credentials
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
SENDER_EMAIL ="weatherreporter4u@gmail.com"  # Ensure the .env file has the correct `EMAIL`
EMAIL_PASSWORD = "zcmqyasvkwxulwjo"  # Ensure the .env file has the correct `PASSWORD`

def send_email(subject, receiver_email, body):
    """
    Sends an email with the given subject and body to the receiver's email address.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = receiver_email
        msg["Subject"] = subject

        # Attach the email body
        msg.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server using SSL
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(SENDER_EMAIL, EMAIL_PASSWORD)
            server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
        print(f"Email sent successfully to {receiver_email}")
    
    except Exception as e:
        print(f"Failed to send email to {receiver_email}. Error: {e}")
