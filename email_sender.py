#!/usr/bin/env python3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials (use an App Password for security!)
EMAIL = "your@gmail.com""  # 🚨 Update this!
PASSWORD = "your-app-password"  # 🚨 See Step 3!

def send_email(to_email, subject, body):
    """Send an email via Gmail SMTP."""
    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject

    # Attach the body (supports HTML)
    msg.attach(MIMEText(body, "html"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Encrypt connection
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, to_email, msg.as_string())
        print(f"✅ Email sent to: {to_email}")
    except Exception as e:
        print(f"❌ Failed to send to {to_email}: {e}")

if __name__ == "__main__":
    # Example: Send to a list of emails
    emails = ["client1@gmail.com", "client2@gmail.com"]  # 🚨 Replace these!
    subject = "Hello from Python!"
    body = """
    <h1>Hi there!</h1>
    <p>This is a <b>test email</b> sent via Python.</p>
    """

    for email in emails:
        send_email(email, subject, body)
