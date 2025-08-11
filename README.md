# 📧 Email Automation Tool

A Python script to send bulk personalized emails via Gmail's SMTP server.

## 🚀 Features
- Send personalized emails in bulk
- HTML email support
- Secure authentication using App Passwords

## ⚙️ Setup
1. **Enable Gmail App Password**:
   - Go to [Google Account Security](https://myaccount.google.com/security)
   - Enable 2FA and generate an App Password (select "Mail" as the app)

2. **Configure Environment Variables**:
   ```bash
   export GMAIL_EMAIL="your@gmail.com"
   export GMAIL_PASSWORD="your-app-password"
