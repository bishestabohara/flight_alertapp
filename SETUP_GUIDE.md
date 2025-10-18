# Flight Alert App - API Setup Guide

## 🔧 Getting Real Notifications Working

To enable real email and SMS notifications, you need to configure API keys from external services.

### 📧 Email Notifications (SendGrid)

1. **Sign up for SendGrid:**
   - Go to: https://sendgrid.com/
   - Click "Start for Free"
   - Create an account (free tier available)

2. **Create API Key:**
   - Go to Settings → API Keys
   - Click "Create API Key"
   - Choose "Restricted Access"
   - Give it "Mail Send" permissions
   - Copy the API key

3. **Verify Sender Email:**
   - Go to Settings → Sender Authentication
   - Verify a single sender email address
   - This will be your FROM_EMAIL

### 📱 SMS Notifications (Twilio)

1. **Sign up for Twilio:**
   - Go to: https://console.twilio.com/
   - Click "Sign up for free"
   - Create an account

2. **Get Account Credentials:**
   - Account SID: Found on dashboard
   - Auth Token: Found on dashboard (click to reveal)

3. **Buy a Phone Number:**
   - Go to Phone Numbers → Manage → Buy a number
   - Choose a US number (costs ~$1/month)
   - This will be your TWILIO_PHONE_NUMBER

### 🔑 Configuration

1. **Create .env file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit .env file with your credentials:**
   ```env
   # Email Configuration
   SENDGRID_API_KEY=your_sendgrid_api_key_here
   FROM_EMAIL=your_verified_email@example.com
   
   # SMS Configuration  
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_PHONE_NUMBER=+1234567890
   ```

3. **Restart the app:**
   ```bash
   python start_app.py
   ```

### 💰 Costs

- **SendGrid**: Free tier = 100 emails/day
- **Twilio**: ~$1/month for phone number + $0.0075 per SMS

### ✅ Testing

After configuration:
1. Go to Settings → Test Notifications
2. Enter your email and phone
3. Click "Test Email" and "Test SMS"
4. You should receive real notifications!

### 🆘 Troubleshooting

- **Email not working**: Check SendGrid API key and verified sender
- **SMS not working**: Check Twilio credentials and phone number format (+1XXXXXXXXXX)
- **Still in demo mode**: Restart the app after adding .env file
