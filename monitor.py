import schedule
import time
import threading
from datetime import datetime, timedelta
from typing import List, Dict
import logging
from database import DatabaseManager
from flight_search import FlightSearchAPI, MockFlightSearch
from notifications import NotificationService
from config import Config

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('flight_monitor.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class FlightMonitor:
    def __init__(self):
        self.db = DatabaseManager()
        self.config = Config()
        
        # Use mock search if API credentials not configured
        if self.config.AMADEUS_API_KEY and self.config.AMADEUS_API_SECRET:
            self.flight_search = FlightSearchAPI()
        else:
            self.flight_search = MockFlightSearch()
            logger.warning("Using mock flight search - configure Amadeus API for real data")
        
        self.notification_service = NotificationService()
        self.is_running = False
        self.monitor_thread = None
    
    def start_monitoring(self):
        """Start the background monitoring process"""
        if self.is_running:
            logger.warning("Monitoring is already running")
            return
        
        self.is_running = True
        self.monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self.monitor_thread.start()
        logger.info("Flight monitoring started")
    
    def stop_monitoring(self):
        """Stop the background monitoring process"""
        self.is_running = False
        if self.monitor_thread:
            self.monitor_thread.join()
        logger.info("Flight monitoring stopped")
    
    def _monitor_loop(self):
        """Main monitoring loop"""
        while self.is_running:
            try:
                self.check_all_alerts()
                # Wait 30 minutes before next check
                time.sleep(30 * 60)
            except Exception as e:
                logger.error(f"Error in monitoring loop: {e}")
                time.sleep(5 * 60)  # Wait 5 minutes on error
    
    def check_all_alerts(self):
        """Check all active flight alerts"""
        logger.info("Checking all active alerts...")
        
        try:
            alerts = self.db.get_active_alerts()
            logger.info(f"Found {len(alerts)} active alerts")
            
            for alert in alerts:
                try:
                    self.check_single_alert(alert)
                except Exception as e:
                    logger.error(f"Error checking alert {alert['id']}: {e}")
                    continue
            
            logger.info("Finished checking all alerts")
        except Exception as e:
            logger.error(f"Error getting active alerts: {e}")
    
    def check_single_alert(self, alert: Dict):
        """Check a single flight alert"""
        alert_id = alert['id']
        logger.info(f"Checking alert {alert_id}: {alert['origin_code']} → {alert['destination_code']}")
        
        try:
            # Search for flights
            flights = self.flight_search.search_flights(
                origin=alert['origin_code'],
                destination=alert['destination_code'],
                departure_date=alert['departure_date'],
                return_date=alert['return_date']
            )
            
            if not flights:
                logger.warning(f"No flights found for alert {alert_id}")
                return
            
            # Find flights below the target price
            affordable_flights = [
                flight for flight in flights 
                if flight['price'] <= alert['max_price']
            ]
            
            if affordable_flights:
                logger.info(f"Found {len(affordable_flights)} affordable flights for alert {alert_id}")
                
                # Get the cheapest flight
                cheapest_flight = min(affordable_flights, key=lambda x: x['price'])
                
                # Check if we've already sent a notification for this price
                if self._should_send_notification(alert_id, cheapest_flight['price']):
                    self._send_price_alert(alert, cheapest_flight)
                else:
                    logger.info(f"Notification already sent for this price range for alert {alert_id}")
            else:
                logger.info(f"No affordable flights found for alert {alert_id}")
            
            # Save the flight search results
            for flight in flights[:3]:  # Save top 3 results
                self.db.save_flight_price(
                    alert_id=alert_id,
                    airline=','.join(flight['airlines']),
                    price=flight['price'],
                    currency=flight['currency'],
                    flight_details=str(flight)
                )
            
        except Exception as e:
            logger.error(f"Error checking alert {alert_id}: {e}")
    
    def _should_send_notification(self, alert_id: str, price: float) -> bool:
        """Check if we should send a notification for this price"""
        try:
            # Get recent notifications for this alert
            import sqlite3
            conn = sqlite3.connect(self.db.db_path)
            cursor = conn.cursor()
            
            # Check notifications sent in the last 24 hours
            yesterday = datetime.now() - timedelta(days=1)
            cursor.execute('''
                SELECT COUNT(*) FROM notifications_sent 
                WHERE alert_id = ? AND sent_at > ?
            ''', (alert_id, yesterday.strftime('%Y-%m-%d %H:%M:%S')))
            
            recent_notifications = cursor.fetchone()[0]
            conn.close()
            
            # Don't send more than 2 notifications per day per alert
            return recent_notifications < 2
            
        except Exception as e:
            logger.error(f"Error checking notification history: {e}")
            return True  # Default to sending notification
    
    def _send_price_alert(self, alert: Dict, flight: Dict):
        """Send price alert notification"""
        alert_id = alert['id']
        logger.info(f"Sending price alert for alert {alert_id}")
        
        try:
            # Prepare user data
            user_data = {
                'email': alert['email'],
                'phone': alert['phone']
            }
            
            # Send notification
            results = self.notification_service.send_notification(
                alert_data=alert,
                flight_data=flight,
                user_data=user_data
            )
            
            if any(results.values()):
                logger.info(f"Price alert sent successfully for alert {alert_id}: {results}")
            else:
                logger.warning(f"Failed to send price alert for alert {alert_id}")
                
        except Exception as e:
            logger.error(f"Error sending price alert for alert {alert_id}: {e}")
    
    def run_manual_check(self, alert_id: str = None):
        """Run a manual check for specific alert or all alerts"""
        if alert_id:
            # Check specific alert
            alerts = self.db.get_active_alerts()
            alert = next((a for a in alerts if a['id'] == alert_id), None)
            if alert:
                self.check_single_alert(alert)
            else:
                logger.error(f"Alert {alert_id} not found")
        else:
            # Check all alerts
            self.check_all_alerts()

def run_monitor():
    """Function to run the monitor (for standalone execution)"""
    monitor = FlightMonitor()
    
    try:
        logger.info("Starting Flight Alert Monitor...")
        monitor.start_monitoring()
        
        # Keep the main thread alive
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        logger.info("Received interrupt signal, stopping monitor...")
        monitor.stop_monitoring()
    except Exception as e:
        logger.error(f"Monitor error: {e}")
        monitor.stop_monitoring()

if __name__ == "__main__":
    run_monitor()
