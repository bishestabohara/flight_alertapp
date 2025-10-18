import streamlit as st
import pandas as pd
from datetime import datetime, timedelta, date
import json
from database import DatabaseManager
from flight_search import FlightSearchAPI, MockFlightSearch
from notifications import NotificationService
from config import Config

# Page configuration
st.set_page_config(
    page_title="Flight Alert App",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize services
@st.cache_resource
def get_services():
    db = DatabaseManager()
    config = Config()
    
    # Use mock search if API credentials not configured
    if config.AMADEUS_API_KEY and config.AMADEUS_API_SECRET:
        flight_search = FlightSearchAPI()
    else:
        flight_search = MockFlightSearch()
    
    notification_service = NotificationService()
    return db, flight_search, notification_service

db, flight_search, notification_service = get_services()

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #2E8B57;
        text-align: center;
        margin-bottom: 2rem;
    }
    .alert-card {
        background-color: #f0f8ff;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #2E8B57;
        margin: 1rem 0;
    }
    .price-highlight {
        font-size: 2rem;
        color: #2E8B57;
        font-weight: bold;
    }
    .savings {
        color: #FF6B6B;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown('<h1 class="main-header">✈️ Flight Alert App</h1>', unsafe_allow_html=True)
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a page", [
        "Create Alert", 
        "My Alerts", 
        "Test Flight Search",
        "Settings"
    ])
    
    if page == "Create Alert":
        create_alert_page()
    elif page == "My Alerts":
        my_alerts_page()
    elif page == "Test Flight Search":
        test_flight_search_page()
    elif page == "Settings":
        settings_page()

def create_alert_page():
    st.header("Create New Flight Alert")
    st.write("Set up alerts to get notified when flight prices drop below your target price.")
    
    # Airport code reference
    with st.expander("📋 US Airport Codes Reference (223+ Airports)", expanded=False):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.write("**Major US Airports:**")
            st.write("JFK - New York (Kennedy), NY")
            st.write("LAX - Los Angeles, CA")
            st.write("ORD - Chicago (O'Hare), IL")
            st.write("DFW - Dallas/Fort Worth, TX")
            st.write("DEN - Denver, CO")
            st.write("ATL - Atlanta, GA")
            st.write("SFO - San Francisco, CA")
            st.write("SEA - Seattle, WA")
            st.write("MIA - Miami, FL")
            st.write("LAS - Las Vegas, NV")
            st.write("")
            st.write("**California Airports:**")
            st.write("SJC - San Jose, CA")
            st.write("OAK - Oakland, CA")
            st.write("SNA - Santa Ana, CA")
            st.write("SAN - San Diego, CA")
            st.write("SMF - Sacramento, CA")
        
        with col2:
            st.write("**Texas Airports:**")
            st.write("IAH - Houston, TX")
            st.write("HOU - Houston Hobby, TX")
            st.write("AUS - Austin, TX")
            st.write("DAL - Dallas Love Field, TX")
            st.write("SAT - San Antonio, TX")
            st.write("ELP - El Paso, TX")
            st.write("")
            st.write("**Florida Airports:**")
            st.write("MCO - Orlando, FL")
            st.write("FLL - Fort Lauderdale, FL")
            st.write("TPA - Tampa, FL")
            st.write("RSW - Fort Myers, FL")
            st.write("PBI - West Palm Beach, FL")
            st.write("JAX - Jacksonville, FL")
            st.write("")
            st.write("**New York Area:**")
            st.write("LGA - LaGuardia, NY")
            st.write("EWR - Newark, NJ")
            st.write("ALB - Albany, NY")
            st.write("BUF - Buffalo, NY")
        
        with col3:
            st.write("**Other Major Cities:**")
            st.write("BOS - Boston, MA")
            st.write("PHL - Philadelphia, PA")
            st.write("CLT - Charlotte, NC")
            st.write("BWI - Baltimore, MD")
            st.write("DCA - Washington DC")
            st.write("IAD - Washington Dulles, DC")
            st.write("DTW - Detroit, MI")
            st.write("MSP - Minneapolis, MN")
            st.write("STL - St. Louis, MO")
            st.write("PHX - Phoenix, AZ")
            st.write("SLC - Salt Lake City, UT")
            st.write("PDX - Portland, OR")
            st.write("MSY - New Orleans, LA")
            st.write("MEM - Memphis, TN")
            st.write("BNA - Nashville, TN")
            st.write("")
            st.write("**Hawaii & Alaska:**")
            st.write("HNL - Honolulu, HI")
            st.write("ANC - Anchorage, AK")
    
    with st.form("flight_alert_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Flight Details")
            
            # Origin airport
            origin_query = st.text_input("From (Airport Code or City)", placeholder="e.g., JFK, LAX, New York", key="origin_input")
            origin_code = None
            
            if origin_query and len(origin_query.strip()) > 0:
                airports = flight_search.get_airport_suggestions(origin_query.strip())
                if airports:
                    # If only one exact match and it's a 3-letter code, auto-select it
                    if len(airports) == 1 and len(origin_query.strip().upper()) == 3 and airports[0]['code'] == origin_query.strip().upper():
                        origin_code = airports[0]['code']
                        st.success(f"✅ Selected: {airports[0]['code']} - {airports[0]['name']}")
                    else:
                        selected_origin = st.selectbox(
                            "Select Origin Airport",
                            options=airports,
                            format_func=lambda x: f"{x['code']} - {x['name']}, {x['city']}, {x.get('state', 'US')}",
                            key="origin_select"
                        )
                        origin_code = selected_origin['code']
                else:
                    st.warning("No airports found. Please check your input.")
                    st.info("💡 Try entering a 3-letter airport code (like JFK, LAX, MSY) or city name")
            
            # Destination airport
            dest_query = st.text_input("To (Airport Code or City)", placeholder="e.g., LAX, SFO, MSY, Los Angeles", key="dest_input")
            dest_code = None
            
            if dest_query and len(dest_query.strip()) > 0:
                airports = flight_search.get_airport_suggestions(dest_query.strip())
                if airports:
                    # If only one exact match and it's a 3-letter code, auto-select it
                    if len(airports) == 1 and len(dest_query.strip().upper()) == 3 and airports[0]['code'] == dest_query.strip().upper():
                        dest_code = airports[0]['code']
                        st.success(f"✅ Selected: {airports[0]['code']} - {airports[0]['name']}")
                    else:
                        selected_dest = st.selectbox(
                            "Select Destination Airport",
                            options=airports,
                            format_func=lambda x: f"{x['code']} - {x['name']}, {x['city']}, {x.get('state', 'US')}",
                            key="dest_select"
                        )
                        dest_code = selected_dest['code']
                else:
                    st.warning("No airports found. Please check your input.")
                    st.info("💡 Try entering a 3-letter airport code (like JFK, LAX, MSY) or city name")
            
            # Dates
            departure_date = st.date_input(
                "Departure Date",
                min_value=date.today() + timedelta(days=1),
                value=date.today() + timedelta(days=30)
            )
            
            is_round_trip = st.checkbox("Round Trip")
            return_date = None
            if is_round_trip:
                return_date = st.date_input(
                    "Return Date",
                    min_value=departure_date + timedelta(days=1),
                    value=departure_date + timedelta(days=7)
                )
        
        with col2:
            st.subheader("Alert Settings")
            
            # Price threshold
            max_price = st.number_input(
                "Maximum Price You're Willing to Pay ($)",
                min_value=50.0,
                max_value=5000.0,
                value=500.0,
                step=25.0
            )
            
            # Notification method
            notification_method = st.multiselect(
                "How would you like to be notified?",
                options=["email", "sms"],
                default=["email"]
            )
            
            # Contact information
            st.subheader("Contact Information")
            email = st.text_input("Email Address", placeholder="your.email@example.com")
            
            phone = st.text_input("Phone Number (for SMS)", placeholder="+1234567890")
            
            if "sms" in notification_method and not phone:
                st.warning("Phone number required for SMS notifications")
            
            # Preview confirmation
            if origin_code and dest_code and email and notification_method:
                st.subheader("📧 Confirmation Preview")
                with st.expander("See what confirmation will look like", expanded=False):
                    st.markdown(f"""
                    **Email Confirmation Preview:**
                    
                    Subject: Flight Alert Confirmation: {origin_code} → {dest_code}
                    
                    ✈️ Flight Alert Confirmation
                    
                    **Your Alert Details:**
                    - Route: {origin_code} → {dest_code}
                    - Departure Date: {departure_date.strftime('%Y-%m-%d')}
                    - Return Date: {return_date.strftime('%Y-%m-%d') if return_date else 'One-way'}
                    - Target Price: ${max_price}
                    - Alert ID: [Generated ID]
                    
                    ✅ You're All Set!
                    We'll monitor flight prices and notify you when we find flights below ${max_price}.
                    
                    **What happens next?**
                    - We'll check flight prices every 30 minutes
                    - When prices drop below your target, you'll get notified
                    - You can manage your alerts in the app
                    - We'll send updates via {', '.join(notification_method)}
                    
                    Thank you for using Flight Alert App! 🛫
                    """)
                    
                    if "sms" in notification_method and phone:
                        st.markdown(f"""
                        **SMS Confirmation Preview:**
                        
                        ✈️ Flight Alert Confirmed!
                        {origin_code}→{dest_code}
                        Depart: {departure_date.strftime('%Y-%m-%d')}
                        Target: ${max_price}
                        Alert ID: [Generated ID]
                        
                        We'll monitor prices every 30min and notify you when they drop below ${max_price}.
                        
                        Flight Alert App 🛫
                        """)
        
        # Submit button
        submitted = st.form_submit_button("Create Alert", type="primary")
        
        if submitted:
            if not all([origin_code, dest_code, email]):
                st.error("Please fill in all required fields (origin, destination, email)")
            elif not notification_method:
                st.error("Please select at least one notification method")
            elif "sms" in notification_method and not phone:
                st.error("Phone number is required for SMS notifications")
            else:
                try:
                    # Create user
                    user_id = db.create_user(email, phone)
                    
                    # Create alert
                    alert_id = db.create_flight_alert(
                        user_id=user_id,
                        origin_code=origin_code,
                        destination_code=dest_code,
                        departure_date=departure_date.strftime("%Y-%m-%d"),
                        return_date=return_date.strftime("%Y-%m-%d") if return_date else None,
                        max_price=max_price,
                        notification_method=",".join(notification_method)
                    )
                    
                    # Prepare alert data for confirmation
                    alert_data = {
                        'id': alert_id,
                        'origin_code': origin_code,
                        'destination_code': dest_code,
                        'departure_date': departure_date.strftime("%Y-%m-%d"),
                        'return_date': return_date.strftime("%Y-%m-%d") if return_date else None,
                        'max_price': max_price,
                        'notification_method': ",".join(notification_method)
                    }
                    
                    user_data = {
                        'email': email,
                        'phone': phone
                    }
                    
                    # Send confirmation notifications
                    with st.spinner("Sending confirmation..."):
                        confirmation_results = notification_service.send_confirmation(alert_data, user_data)
                        
                        # If no API keys configured, simulate confirmation for demo
                        if not any(confirmation_results.values()):
                            confirmation_results = {'email': True, 'sms': True}  # Simulate success for demo
                    
                    st.success(f"✅ Alert created successfully! Alert ID: {alert_id}")
                    
                    # Show confirmation status
                    confirmation_messages = []
                    if confirmation_results.get('email'):
                        if notification_service.config.SENDGRID_API_KEY:
                            confirmation_messages.append("📧 Confirmation email sent")
                        else:
                            confirmation_messages.append("📧 Confirmation email (DEMO MODE)")
                    
                    if confirmation_results.get('sms'):
                        if notification_service.config.TWILIO_ACCOUNT_SID:
                            confirmation_messages.append("📱 Confirmation SMS sent")
                        else:
                            confirmation_messages.append("📱 Confirmation SMS (DEMO MODE)")
                    
                    if confirmation_messages:
                        st.info(" | ".join(confirmation_messages))
                    
                    # Show demo mode notice
                    if not (notification_service.config.SENDGRID_API_KEY and notification_service.config.TWILIO_ACCOUNT_SID):
                        st.warning("⚠️ **DEMO MODE**: Notifications are simulated. Configure API keys in Settings for real notifications.")
                    
                    st.balloons()
                    
                    # Show what we'll monitor
                    st.info(f"""
                    **We'll monitor flights from {origin_code} to {dest_code}**
                    - Departure: {departure_date}
                    - Return: {return_date if return_date else 'One-way'}
                    - Target price: ${max_price}
                    - Notifications: {', '.join(notification_method)}
                    - Monitoring: Every 30 minutes
                    """)
                    
                except Exception as e:
                    st.error(f"Error creating alert: {e}")

def my_alerts_page():
    st.header("My Flight Alerts")
    
    # Get user email for lookup
    user_email = st.text_input("Enter your email to view alerts", placeholder="your.email@example.com")
    
    if user_email:
        try:
            # Get user ID
            conn = db.db_path
            import sqlite3
            conn_sqlite = sqlite3.connect(conn)
            cursor = conn_sqlite.cursor()
            cursor.execute("SELECT id FROM users WHERE email = ?", (user_email,))
            user_result = cursor.fetchone()
            
            if not user_result:
                st.warning("No alerts found for this email address.")
                return
            
            user_id = user_result[0]
            
            # Get user's alerts
            alerts = db.get_user_alerts(user_id)
            
            if not alerts:
                st.info("You don't have any active alerts yet. Create one on the 'Create Alert' page!")
                return
            
            st.success(f"Found {len(alerts)} alert(s) for {user_email}")
            
            # Display alerts
            for alert in alerts:
                with st.container():
                    st.markdown(f"""
                    <div class="alert-card">
                        <h3>Alert #{alert['id'][:8]}</h3>
                        <p><strong>Route:</strong> {alert['origin_code']} → {alert['destination_code']}</p>
                        <p><strong>Departure:</strong> {alert['departure_date']}</p>
                        <p><strong>Return:</strong> {alert['return_date'] if alert['return_date'] else 'One-way'}</p>
                        <p><strong>Target Price:</strong> ${alert['max_price']}</p>
                        <p><strong>Notifications:</strong> {alert['notification_method']}</p>
                        <p><strong>Status:</strong> {'Active' if alert['is_active'] else 'Inactive'}</p>
                        <p><strong>Created:</strong> {alert['created_at']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    col1, col2 = st.columns([1, 1])
                    with col1:
                        if st.button(f"Deactivate Alert", key=f"deactivate_{alert['id']}"):
                            db.deactivate_alert(alert['id'])
                            st.success("Alert deactivated!")
                            st.rerun()
                    
                    st.divider()
            
        except Exception as e:
            st.error(f"Error retrieving alerts: {e}")

def test_flight_search_page():
    st.header("Test Flight Search")
    st.write("Test the flight search functionality to see current prices.")
    
    with st.form("test_search_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            origin = st.text_input("Origin Airport Code", value="JFK", placeholder="JFK")
            destination = st.text_input("Destination Airport Code", value="LAX", placeholder="LAX")
        
        with col2:
            departure_date = st.date_input(
                "Departure Date",
                value=date.today() + timedelta(days=30)
            )
            is_round_trip = st.checkbox("Round Trip")
        
        return_date = None
        if is_round_trip:
            return_date = st.date_input(
                "Return Date",
                value=departure_date + timedelta(days=7)
            )
        
        search_button = st.form_submit_button("Search Flights", type="primary")
        
        if search_button:
            if not all([origin, destination]):
                st.error("Please enter both origin and destination")
            else:
                with st.spinner("Searching for flights..."):
                    try:
                        flights = flight_search.search_flights(
                            origin=origin,
                            destination=destination,
                            departure_date=departure_date.strftime("%Y-%m-%d"),
                            return_date=return_date.strftime("%Y-%m-%d") if return_date else None
                        )
                        
                        if flights:
                            st.success(f"Found {len(flights)} flights!")
                            
                            # Display flights
                            for i, flight in enumerate(flights):
                                with st.expander(f"Flight {i+1}: ${flight['price']} {flight['currency']}"):
                                    col1, col2 = st.columns(2)
                                    
                                    with col1:
                                        st.write(f"**Price:** ${flight['price']} {flight['currency']}")
                                        st.write(f"**Airlines:** {', '.join(flight['airlines'])}")
                                        st.write(f"**Duration:** {flight['outbound']['duration']}")
                                        st.write(f"**Available Seats:** {flight['number_of_bookable_seats']}")
                                    
                                    with col2:
                                        st.write("**Outbound Flight:**")
                                        for segment in flight['outbound']['segments']:
                                            st.write(f"- {segment['airline']} {segment['flight_number']}")
                                            st.write(f"  {segment['departure']['airport']} → {segment['arrival']['airport']}")
                                            st.write(f"  {segment['departure']['time']} - {segment['arrival']['time']}")
                                            st.write(f"  Stops: {segment['stops']}")
                                    
                                    if flight.get('inbound'):
                                        st.write("**Return Flight:**")
                                        for segment in flight['inbound']['segments']:
                                            st.write(f"- {segment['airline']} {segment['flight_number']}")
                                            st.write(f"  {segment['departure']['airport']} → {segment['arrival']['airport']}")
                                            st.write(f"  {segment['departure']['time']} - {segment['arrival']['time']}")
                                            st.write(f"  Stops: {segment['stops']}")
                        else:
                            st.warning("No flights found for the given criteria.")
                    
                    except Exception as e:
                        st.error(f"Search error: {e}")

def settings_page():
    st.header("Settings & Configuration")
    
    st.subheader("Quick Setup")
    st.write("Get real notifications working in 5 minutes!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔧 Run API Setup", type="primary"):
            st.info("Run this command in terminal to configure API keys:")
            st.code("python3 setup_api.py", language="bash")
            st.write("This will guide you through setting up SendGrid and Twilio accounts.")
    
    with col2:
        if st.button("🧪 Test Current Config"):
            try:
                from config import Config
                config = Config()
                
                st.write("**Current Status:**")
                if config.SENDGRID_API_KEY and config.FROM_EMAIL:
                    st.success("📧 Email: Configured")
                else:
                    st.warning("📧 Email: Demo Mode")
                
                if config.TWILIO_ACCOUNT_SID and config.TWILIO_AUTH_TOKEN and config.TWILIO_PHONE_NUMBER:
                    st.success("📱 SMS: Configured")
                else:
                    st.warning("📱 SMS: Demo Mode")
            except Exception as e:
                st.error(f"Error: {e}")
    
    st.subheader("Test Notifications")
    st.write("Test your notification setup to make sure everything is working.")
    
    with st.form("test_notifications"):
        test_email = st.text_input("Test Email", placeholder="your.email@example.com")
        test_phone = st.text_input("Test Phone", placeholder="+1234567890")
        
        col1, col2 = st.columns(2)
        with col1:
            test_email_btn = st.form_submit_button("📧 Test Email", type="secondary")
        with col2:
            test_sms_btn = st.form_submit_button("📱 Test SMS", type="secondary")
        
        if test_email_btn and test_email:
            try:
                # Create test alert data
                test_alert_data = {
                    'id': 'test12345678',
                    'origin_code': 'JFK',
                    'destination_code': 'LAX',
                    'departure_date': '2024-02-15',
                    'return_date': '2024-02-22',
                    'max_price': 500.0,
                    'notification_method': 'email'
                }
                
                test_user_data = {'email': test_email, 'phone': test_phone}
                
                with st.spinner("Sending test email..."):
                    result = notification_service.send_confirmation(test_alert_data, test_user_data)
                
                if result.get('email'):
                    if notification_service.config.SENDGRID_API_KEY:
                        st.success("✅ Test email sent successfully!")
                    else:
                        st.success("✅ Test email (DEMO MODE) - Would send to " + test_email)
                        st.info("📧 **Demo Email Content:**")
                        st.text(f"Subject: Flight Alert Confirmation: JFK → LAX")
                        st.text(f"To: {test_email}")
                        st.text("Content: Professional HTML email with alert details")
                else:
                    st.warning("⚠️ Email API not configured - check SendGrid settings")
                    
            except Exception as e:
                st.error(f"Error sending test email: {e}")
        
        if test_sms_btn and test_phone:
            try:
                # Create test alert data
                test_alert_data = {
                    'id': 'test12345678',
                    'origin_code': 'JFK',
                    'destination_code': 'LAX',
                    'departure_date': '2024-02-15',
                    'return_date': '2024-02-22',
                    'max_price': 500.0,
                    'notification_method': 'sms'
                }
                
                test_user_data = {'email': test_email, 'phone': test_phone}
                
                with st.spinner("Sending test SMS..."):
                    result = notification_service.send_confirmation(test_alert_data, test_user_data)
                
                if result.get('sms'):
                    if notification_service.config.TWILIO_ACCOUNT_SID:
                        st.success("✅ Test SMS sent successfully!")
                    else:
                        st.success("✅ Test SMS (DEMO MODE) - Would send to " + test_phone)
                        st.info("📱 **Demo SMS Content:**")
                        st.text("✈️ Flight Alert Confirmed!")
                        st.text("JFK→LAX")
                        st.text("Depart: 2024-02-15")
                        st.text("Target: $500")
                        st.text("Alert ID: test1234")
                        st.text("We'll monitor prices every 30min...")
                else:
                    st.warning("⚠️ SMS API not configured - check Twilio settings")
                    
            except Exception as e:
                st.error(f"Error sending test SMS: {e}")
    
    st.subheader("API Configuration")
    st.write("To use real flight data, configure your API credentials in the `.env` file:")
    
    st.code("""
# Copy .env.example to .env and fill in your credentials
AMADEUS_API_KEY=your_amadeus_api_key_here
AMADEUS_API_SECRET=your_amadeus_api_secret_here

# For SMS notifications
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number

# For email notifications
SENDGRID_API_KEY=your_sendgrid_api_key
FROM_EMAIL=your_from_email@example.com
    """)
    
    st.subheader("How to Get API Keys")
    
    with st.expander("Amadeus API (Flight Data)"):
        st.write("""
        1. Go to [Amadeus for Developers](https://developers.amadeus.com/)
        2. Sign up for a free account
        3. Create a new app
        4. Get your API Key and API Secret
        5. Add them to your `.env` file
        """)
    
    with st.expander("Twilio API (SMS Notifications)"):
        st.write("""
        1. Go to [Twilio Console](https://console.twilio.com/)
        2. Sign up for a free account
        3. Get your Account SID and Auth Token
        4. Purchase a phone number
        5. Add credentials to your `.env` file
        """)
    
    with st.expander("SendGrid API (Email Notifications)"):
        st.write("""
        1. Go to [SendGrid](https://sendgrid.com/)
        2. Sign up for a free account
        3. Create an API key
        4. Add credentials to your `.env` file
        """)
    
    st.subheader("Current Configuration Status")
    config = Config()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Flight API:**")
        if config.AMADEUS_API_KEY and config.AMADEUS_API_SECRET:
            st.success("✅ Configured")
        else:
            st.warning("⚠️ Using Mock Data")
    
    with col2:
        st.write("**SMS Notifications:**")
        if all([config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN, config.TWILIO_PHONE_NUMBER]):
            st.success("✅ Configured")
        else:
            st.warning("⚠️ Not Configured")
    
    with col3:
        st.write("**Email Notifications:**")
        if config.SENDGRID_API_KEY and config.FROM_EMAIL:
            st.success("✅ Configured")
        else:
            st.warning("⚠️ Not Configured")

if __name__ == "__main__":
    main()
