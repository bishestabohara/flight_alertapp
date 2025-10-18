import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Flight API Configuration
    AMADEUS_API_KEY = os.getenv('AMADEUS_API_KEY')
    AMADEUS_API_SECRET = os.getenv('AMADEUS_API_SECRET')
    
    # Twilio SMS Configuration
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
    
    # SendGrid Email Configuration
    SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
    FROM_EMAIL = os.getenv('FROM_EMAIL')
    
    # App Configuration
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///flight_alerts.db')
    
    # Flight API Base URLs
    AMADEUS_BASE_URL = "https://api.amadeus.com/v2"
    AMADEUS_TOKEN_URL = "https://api.amadeus.com/v1/security/oauth2/token"
