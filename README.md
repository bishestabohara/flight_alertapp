# Flight Alert App

A comprehensive flight price monitoring application that alerts users when flight prices drop below their target price.

## ✈️ Features

- **Flight Price Monitoring**: Monitor flights from any airline for specific routes and dates
- **Smart Alerts**: Get notified via SMS or email when prices drop below your threshold
- **User-Friendly Interface**: Clean Streamlit web interface for easy alert management
- **Background Monitoring**: Continuous price checking every 30 minutes
- **Multiple Airlines**: Support for all major airlines through Amadeus API
- **Flexible Notifications**: Choose between email, SMS, or both notification methods

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Keys (Optional)

Copy the example environment file and add your API credentials:

```bash
cp .env.example .env
```

Edit `.env` with your API keys:
- **Amadeus API**: For real flight data (free tier available)
- **Twilio**: For SMS notifications
- **SendGrid**: For email notifications

*Note: The app works with mock data if no API keys are configured*

### 3. Run the Application

```bash
python start_app.py
```

Or run components separately:

```bash
# Web interface only
streamlit run app.py

# Background monitor only
python monitor.py
```

### 4. Access the App

Open your browser and go to: `http://localhost:8501`

## 📱 How to Use

### Creating an Alert

1. **Flight Details**: Enter origin and destination airports (e.g., JFK, LAX)
2. **Dates**: Select departure date and optionally return date
3. **Price Threshold**: Set your maximum willing price
4. **Notifications**: Choose email, SMS, or both
5. **Contact Info**: Provide your email and phone number

### Managing Alerts

- View all your active alerts
- Deactivate alerts you no longer need
- Check alert status and creation date

### Testing Flight Search

- Test the flight search functionality
- See current prices for any route
- Verify the system is working correctly

## 🔧 Configuration

### API Setup

#### Amadeus API (Flight Data)
1. Go to [Amadeus for Developers](https://developers.amadeus.com/)
2. Sign up for a free account
3. Create a new app
4. Get your API Key and API Secret

#### Twilio API (SMS)
1. Go to [Twilio Console](https://console.twilio.com/)
2. Sign up for a free account
3. Get your Account SID and Auth Token
4. Purchase a phone number

#### SendGrid API (Email)
1. Go to [SendGrid](https://sendgrid.com/)
2. Sign up for a free account
3. Create an API key

### Environment Variables

```env
# Flight API Configuration
AMADEUS_API_KEY=your_amadeus_api_key_here
AMADEUS_API_SECRET=your_amadeus_api_secret_here

# Twilio SMS Configuration
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number

# SendGrid Email Configuration
SENDGRID_API_KEY=your_sendgrid_api_key
FROM_EMAIL=your_from_email@example.com

# App Configuration
DATABASE_URL=sqlite:///flight_alerts.db
```

## 📊 Database Schema

The app uses SQLite with the following tables:

- **users**: User information and contact details
- **flight_alerts**: Active flight price alerts
- **flight_prices**: Historical flight price data
- **notifications_sent**: Notification history

## 🔄 Monitoring System

The background monitor:

- Checks all active alerts every 30 minutes
- Searches for flights using the Amadeus API
- Sends notifications when prices drop below thresholds
- Prevents spam by limiting notifications to 2 per day per alert
- Logs all activities for debugging

## 📁 Project Structure

```
flight_alertapp/
├── app.py                 # Main Streamlit application
├── monitor.py             # Background monitoring system
├── database.py            # Database management
├── flight_search.py       # Flight search API integration
├── notifications.py       # SMS and email notifications
├── config.py             # Configuration management
├── start_app.py          # Application startup script
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
└── README.md            # This file
```

## 🛠️ Development

### Running in Development Mode

```bash
# Install development dependencies
pip install -r requirements.txt

# Run with auto-reload
streamlit run app.py --server.runOnSave true

# Run monitor separately
python monitor.py
```

### Testing

The app includes mock flight data for testing without API keys. Use the "Test Flight Search" page to verify functionality.

## 📝 Logs

The monitoring system creates detailed logs in `flight_monitor.log`:

- Alert checking activities
- Price changes detected
- Notification sending status
- Error handling and debugging

## 🔒 Security Notes

- Store API keys securely in environment variables
- Never commit `.env` files to version control
- Use HTTPS in production
- Implement rate limiting for production use

## 🚀 Deployment

### Local Production

```bash
# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your API keys

# Start the application
python start_app.py
```

### Cloud Deployment

The app can be deployed to:
- **Heroku**: Use Procfile for web and worker processes
- **AWS**: EC2 with RDS for database
- **Google Cloud**: App Engine with Cloud SQL
- **DigitalOcean**: Droplet with managed database

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

For issues and questions:
1. Check the logs in `flight_monitor.log`
2. Verify API key configuration
3. Test with the "Test Flight Search" feature
4. Check the Settings page for configuration status

## 🔮 Future Enhancements

- [ ] Support for multiple passengers
- [ ] Flexible date ranges
- [ ] Price trend analysis
- [ ] Mobile app
- [ ] Integration with more airlines
- [ ] Advanced filtering options
- [ ] Price prediction algorithms
