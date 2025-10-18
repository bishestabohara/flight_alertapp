import sqlite3
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import uuid

class DatabaseManager:
    def __init__(self, db_path: str = "flight_alerts.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize the database with required tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                email TEXT UNIQUE NOT NULL,
                phone TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Flight alerts table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS flight_alerts (
                id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                origin_code TEXT NOT NULL,
                destination_code TEXT NOT NULL,
                departure_date DATE NOT NULL,
                return_date DATE,
                max_price DECIMAL(10,2) NOT NULL,
                notification_method TEXT NOT NULL,
                is_active BOOLEAN DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        
        # Flight prices table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS flight_prices (
                id TEXT PRIMARY KEY,
                alert_id TEXT NOT NULL,
                airline TEXT,
                price DECIMAL(10,2) NOT NULL,
                currency TEXT DEFAULT 'USD',
                flight_details TEXT,
                checked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (alert_id) REFERENCES flight_alerts (id)
            )
        ''')
        
        # Notifications sent table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notifications_sent (
                id TEXT PRIMARY KEY,
                alert_id TEXT NOT NULL,
                notification_type TEXT NOT NULL,
                sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (alert_id) REFERENCES flight_alerts (id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def create_user(self, email: str, phone: str = None) -> str:
        """Create a new user and return user ID"""
        user_id = str(uuid.uuid4())
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO users (id, email, phone) VALUES (?, ?, ?)",
                (user_id, email, phone)
            )
            conn.commit()
            return user_id
        except sqlite3.IntegrityError:
            # User already exists, get their ID
            cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
            result = cursor.fetchone()
            return result[0] if result else None
        finally:
            conn.close()
    
    def create_flight_alert(self, user_id: str, origin_code: str, destination_code: str,
                          departure_date: str, max_price: float, notification_method: str,
                          return_date: str = None) -> str:
        """Create a new flight alert and return alert ID"""
        alert_id = str(uuid.uuid4())
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO flight_alerts 
            (id, user_id, origin_code, destination_code, departure_date, return_date, 
             max_price, notification_method)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (alert_id, user_id, origin_code, destination_code, departure_date, 
              return_date, max_price, notification_method))
        
        conn.commit()
        conn.close()
        return alert_id
    
    def get_active_alerts(self) -> List[Dict]:
        """Get all active flight alerts"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT fa.*, u.email, u.phone
            FROM flight_alerts fa
            JOIN users u ON fa.user_id = u.id
            WHERE fa.is_active = 1
        ''')
        
        columns = [description[0] for description in cursor.description]
        alerts = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        conn.close()
        return alerts
    
    def save_flight_price(self, alert_id: str, airline: str, price: float, 
                         currency: str = 'USD', flight_details: str = None):
        """Save a flight price check result"""
        price_id = str(uuid.uuid4())
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO flight_prices 
            (id, alert_id, airline, price, currency, flight_details)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (price_id, alert_id, airline, price, currency, flight_details))
        
        conn.commit()
        conn.close()
    
    def record_notification_sent(self, alert_id: str, notification_type: str):
        """Record that a notification was sent"""
        notification_id = str(uuid.uuid4())
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO notifications_sent (id, alert_id, notification_type)
            VALUES (?, ?, ?)
        ''', (notification_id, alert_id, notification_type))
        
        conn.commit()
        conn.close()
    
    def get_user_alerts(self, user_id: str) -> List[Dict]:
        """Get all alerts for a specific user"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM flight_alerts WHERE user_id = ? ORDER BY created_at DESC
        ''', (user_id,))
        
        columns = [description[0] for description in cursor.description]
        alerts = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        conn.close()
        return alerts
    
    def deactivate_alert(self, alert_id: str):
        """Deactivate a flight alert"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE flight_alerts SET is_active = 0 WHERE id = ?
        ''', (alert_id,))
        
        conn.commit()
        conn.close()
