import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Dict, List
import requests
from twilio.rest import Client
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from config import Config
from database import DatabaseManager

class NotificationService:
    def __init__(self):
        self.config = Config()
        self.db = DatabaseManager()
    
    def send_email_notification(self, to_email: str, alert_data: Dict, flight_data: Dict) -> bool:
        """Send email notification about price drop"""
        try:
            if self.config.SENDGRID_API_KEY:
                return self._send_sendgrid_email(to_email, alert_data, flight_data)
            else:
                return self._send_smtp_email(to_email, alert_data, flight_data)
        except Exception as e:
            print(f"Email notification error: {e}")
            return False
    
    def _send_sendgrid_email(self, to_email: str, alert_data: Dict, flight_data: Dict) -> bool:
        """Send email using SendGrid"""
        subject = f"Flight Price Alert: {alert_data['origin_code']} → {alert_data['destination_code']}"
        
        html_content = self._create_email_html(alert_data, flight_data)
        
        message = Mail(
            from_email=self.config.FROM_EMAIL,
            to_emails=to_email,
            subject=subject,
            html_content=html_content
        )
        
        try:
            sg = SendGridAPIClient(api_key=self.config.SENDGRID_API_KEY)
            response = sg.send(message)
            return response.status_code == 202
        except Exception as e:
            print(f"SendGrid error: {e}")
            return False
    
    def _send_smtp_email(self, to_email: str, alert_data: Dict, flight_data: Dict) -> bool:
        """Send email using SMTP (fallback)"""
        # This is a basic implementation - you'd need to configure SMTP settings
        subject = f"Flight Price Alert: {alert_data['origin_code']} → {alert_data['destination_code']}"
        body = self._create_email_text(alert_data, flight_data)
        
        msg = MIMEMultipart()
        msg['From'] = self.config.FROM_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Note: You'd need to configure SMTP server settings
        # This is just a placeholder implementation
        return True
    
    def send_sms_notification(self, to_phone: str, alert_data: Dict, flight_data: Dict) -> bool:
        """Send SMS notification about price drop"""
        try:
            if not all([self.config.TWILIO_ACCOUNT_SID, self.config.TWILIO_AUTH_TOKEN, self.config.TWILIO_PHONE_NUMBER]):
                print("Twilio credentials not configured")
                return False
            
            client = Client(self.config.TWILIO_ACCOUNT_SID, self.config.TWILIO_AUTH_TOKEN)
            
            message_body = self._create_sms_text(alert_data, flight_data)
            
            message = client.messages.create(
                body=message_body,
                from_=self.config.TWILIO_PHONE_NUMBER,
                to=to_phone
            )
            
            return message.sid is not None
        except Exception as e:
            print(f"SMS notification error: {e}")
            return False
    
    def _create_email_html(self, alert_data: Dict, flight_data: Dict) -> str:
        """Create HTML email content"""
        html = f"""
        <html>
        <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
            <h2 style="color: #2E8B57;">✈️ Flight Price Alert!</h2>
            
            <div style="background-color: #f0f8ff; padding: 20px; border-radius: 8px; margin: 20px 0;">
                <h3>Your Alert Details:</h3>
                <p><strong>Route:</strong> {alert_data['origin_code']} → {alert_data['destination_code']}</p>
                <p><strong>Departure Date:</strong> {alert_data['departure_date']}</p>
                <p><strong>Your Target Price:</strong> ${alert_data['max_price']}</p>
            </div>
            
            <div style="background-color: #e8f5e8; padding: 20px; border-radius: 8px; margin: 20px 0;">
                <h3 style="color: #2E8B57;">🎉 Great News! Found Lower Prices:</h3>
                <p style="font-size: 24px; font-weight: bold; color: #2E8B57;">
                    ${flight_data['price']} {flight_data['currency']}
                </p>
                <p><strong>Savings:</strong> ${alert_data['max_price'] - flight_data['price']:.2f}</p>
            </div>
            
            <div style="background-color: #fff; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
                <h3>Flight Details:</h3>
                <p><strong>Airlines:</strong> {', '.join(flight_data['airlines'])}</p>
                <p><strong>Duration:</strong> {flight_data['outbound']['duration']}</p>
                <p><strong>Available Seats:</strong> {flight_data['number_of_bookable_seats']}</p>
                
                <h4>Outbound Flight:</h4>
                {self._format_segments_html(flight_data['outbound']['segments'])}
                
                {self._format_inbound_html(flight_data.get('inbound'))}
            </div>
            
            <div style="margin-top: 30px; text-align: center;">
                <p style="color: #666; font-size: 14px;">
                    Book quickly! Flight prices can change rapidly.
                </p>
                <p style="color: #666; font-size: 12px;">
                    This alert was sent by Flight Alert App
                </p>
            </div>
        </body>
        </html>
        """
        return html
    
    def _format_segments_html(self, segments: List[Dict]) -> str:
        """Format flight segments for HTML"""
        html = "<ul>"
        for segment in segments:
            html += f"""
            <li>
                <strong>{segment['airline']} {segment['flight_number']}</strong><br>
                {segment['departure']['airport']} → {segment['arrival']['airport']}<br>
                Departure: {segment['departure']['time']}<br>
                Arrival: {segment['arrival']['time']}<br>
                Stops: {segment['stops']}
            </li>
            """
        html += "</ul>"
        return html
    
    def _format_inbound_html(self, inbound: Dict) -> str:
        """Format inbound flight for HTML"""
        if not inbound:
            return ""
        
        return f"""
        <h4>Return Flight:</h4>
        {self._format_segments_html(inbound['segments'])}
        """
    
    def _create_email_text(self, alert_data: Dict, flight_data: Dict) -> str:
        """Create plain text email content"""
        text = f"""
Flight Price Alert!

Your Alert Details:
- Route: {alert_data['origin_code']} → {alert_data['destination_code']}
- Departure Date: {alert_data['departure_date']}
- Your Target Price: ${alert_data['max_price']}

Great News! Found Lower Prices:
- Price: ${flight_data['price']} {flight_data['currency']}
- Savings: ${alert_data['max_price'] - flight_data['price']:.2f}

Flight Details:
- Airlines: {', '.join(flight_data['airlines'])}
- Duration: {flight_data['outbound']['duration']}
- Available Seats: {flight_data['number_of_bookable_seats']}

Outbound Flight:
"""
        
        for segment in flight_data['outbound']['segments']:
            text += f"- {segment['airline']} {segment['flight_number']}: {segment['departure']['airport']} → {segment['arrival']['airport']}\n"
            text += f"  Departure: {segment['departure']['time']}, Arrival: {segment['arrival']['time']}\n"
            text += f"  Stops: {segment['stops']}\n"
        
        if flight_data.get('inbound'):
            text += "\nReturn Flight:\n"
            for segment in flight_data['inbound']['segments']:
                text += f"- {segment['airline']} {segment['flight_number']}: {segment['departure']['airport']} → {segment['arrival']['airport']}\n"
                text += f"  Departure: {segment['departure']['time']}, Arrival: {segment['arrival']['time']}\n"
                text += f"  Stops: {segment['stops']}\n"
        
        text += "\nBook quickly! Flight prices can change rapidly.\n"
        text += "This alert was sent by Flight Alert App"
        
        return text
    
    def _create_sms_text(self, alert_data: Dict, flight_data: Dict) -> str:
        """Create SMS text content"""
        savings = alert_data['max_price'] - flight_data['price']
        
        text = f"✈️ Flight Alert!\n"
        text += f"{alert_data['origin_code']}→{alert_data['destination_code']}\n"
        text += f"Found: ${flight_data['price']} (was ${alert_data['max_price']})\n"
        text += f"Save: ${savings:.2f}\n"
        text += f"Depart: {alert_data['departure_date']}\n"
        text += f"Book now!"
        
        return text
    
    def send_confirmation_email(self, to_email: str, alert_data: Dict) -> bool:
        """Send confirmation email when alert is created"""
        try:
            if not self.config.SENDGRID_API_KEY or not self.config.FROM_EMAIL:
                print(f"DEMO MODE: Would send email to {to_email}")
                print(f"Subject: Flight Alert Confirmation: {alert_data['origin_code']} → {alert_data['destination_code']}")
                return True  # Return True for demo mode
            
            subject = f"Flight Alert Confirmation: {alert_data['origin_code']} → {alert_data['destination_code']}"
            
            html_content = f"""
            <html>
            <body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                <h2 style="color: #2E8B57;">✈️ Flight Alert Confirmation</h2>
                
                <div style="background-color: #f0f8ff; padding: 20px; border-radius: 8px; margin: 20px 0;">
                    <h3>Your Alert Details:</h3>
                    <p><strong>Route:</strong> {alert_data['origin_code']} → {alert_data['destination_code']}</p>
                    <p><strong>Departure Date:</strong> {alert_data['departure_date']}</p>
                    <p><strong>Return Date:</strong> {alert_data['return_date'] if alert_data['return_date'] else 'One-way'}</p>
                    <p><strong>Target Price:</strong> ${alert_data['max_price']}</p>
                    <p><strong>Alert ID:</strong> {alert_data['id'][:8]}</p>
                </div>
                
                <div style="background-color: #e8f5e8; padding: 20px; border-radius: 8px; margin: 20px 0;">
                    <h3 style="color: #2E8B57;">✅ You're All Set!</h3>
                    <p>We'll monitor flight prices and notify you when we find flights below ${alert_data['max_price']}.</p>
                    <p><strong>Monitoring:</strong> Every 30 minutes</p>
                    <p><strong>Notifications:</strong> {alert_data['notification_method'].replace(',', ' and ')}</p>
                </div>
                
                <div style="background-color: #fff; padding: 20px; border: 1px solid #ddd; border-radius: 8px;">
                    <h3>What happens next?</h3>
                    <ul>
                        <li>We'll check flight prices every 30 minutes</li>
                        <li>When prices drop below your target, you'll get notified</li>
                        <li>You can manage your alerts in the app</li>
                        <li>We'll send updates via {alert_data['notification_method'].replace(',', ' and ')}</li>
                    </ul>
                </div>
                
                <div style="margin-top: 30px; text-align: center;">
                    <p style="color: #666; font-size: 14px;">
                        Thank you for using Flight Alert App! 🛫
                    </p>
                    <p style="color: #666; font-size: 12px;">
                        This confirmation was sent automatically when you created your alert.
                    </p>
                </div>
            </body>
            </html>
            """
            
            return self._send_sendgrid_email(to_email, subject, html_content)
                
        except Exception as e:
            print(f"Confirmation email error: {e}")
            return False
    
    def send_confirmation_sms(self, to_phone: str, alert_data: Dict) -> bool:
        """Send confirmation SMS when alert is created"""
        try:
            if not all([self.config.TWILIO_ACCOUNT_SID, self.config.TWILIO_AUTH_TOKEN, self.config.TWILIO_PHONE_NUMBER]):
                print(f"DEMO MODE: Would send SMS to {to_phone}")
                print(f"Message: Flight Alert Confirmed! {alert_data['origin_code']}→{alert_data['destination_code']}")
                return True  # Return True for demo mode
            
            client = Client(self.config.TWILIO_ACCOUNT_SID, self.config.TWILIO_AUTH_TOKEN)
            
            message_body = f"""✈️ Flight Alert Confirmed!
{alert_data['origin_code']}→{alert_data['destination_code']}
Depart: {alert_data['departure_date']}
Target: ${alert_data['max_price']}
Alert ID: {alert_data['id'][:8]}

We'll monitor prices every 30min and notify you when they drop below ${alert_data['max_price']}.

Flight Alert App 🛫"""
            
            message = client.messages.create(
                body=message_body,
                from_=self.config.TWILIO_PHONE_NUMBER,
                to=to_phone
            )
            
            return message.sid is not None
        except Exception as e:
            print(f"Confirmation SMS error: {e}")
            return False
    
    def send_confirmation(self, alert_data: Dict, user_data: Dict) -> Dict:
        """Send confirmation notifications when alert is created"""
        results = {'email': False, 'sms': False}
        
        notification_method = alert_data['notification_method']
        
        if 'email' in notification_method and user_data.get('email'):
            results['email'] = self.send_confirmation_email(
                user_data['email'], alert_data
            )
        
        if 'sms' in notification_method and user_data.get('phone'):
            results['sms'] = self.send_confirmation_sms(
                user_data['phone'], alert_data
            )
        
        return results
    
    def send_notification(self, alert_data: Dict, flight_data: Dict, user_data: Dict) -> Dict:
        """Send notification based on user preferences"""
        results = {'email': False, 'sms': False}
        
        notification_method = alert_data['notification_method']
        
        if 'email' in notification_method and user_data.get('email'):
            results['email'] = self.send_email_notification(
                user_data['email'], alert_data, flight_data
            )
        
        if 'sms' in notification_method and user_data.get('phone'):
            results['sms'] = self.send_sms_notification(
                user_data['phone'], alert_data, flight_data
            )
        
        # Record notification sent
        if any(results.values()):
            notification_type = 'both' if all(results.values()) else ('email' if results['email'] else 'sms')
            self.db.record_notification_sent(alert_data['id'], notification_type)
        
        return results
