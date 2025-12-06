import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Flask config
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-change-this')
    
    # Email config (using Gmail as example)
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
    SMTP_USERNAME = os.getenv('SMTP_USERNAME', 'your-email@gmail.com')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD', 'your-app-password')
    EMAIL_FROM = os.getenv('EMAIL_FROM', 'your-email@gmail.com')
    
    # Admin email for notifications
    ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', 'info@artmountacademy.com')