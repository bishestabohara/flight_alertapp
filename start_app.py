#!/usr/bin/env python3
"""
Flight Alert App Startup Script
Run this script to start both the web interface and background monitoring
"""

import subprocess
import sys
import os
import time
import signal
from threading import Thread

def run_streamlit():
    """Run the Streamlit web interface"""
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py", "--server.port", "8501"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Streamlit: {e}")
    except KeyboardInterrupt:
        print("Streamlit stopped")

def run_monitor():
    """Run the background monitor"""
    try:
        subprocess.run([sys.executable, "monitor.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running monitor: {e}")
    except KeyboardInterrupt:
        print("Monitor stopped")

def main():
    print("🚀 Starting Flight Alert App...")
    print("=" * 50)
    
    # Check if required files exist
    required_files = ["app.py", "monitor.py", "database.py", "flight_search.py", "notifications.py", "config.py"]
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return
    
    print("✅ All required files found")
    
    # Start background monitor in a separate thread
    monitor_thread = Thread(target=run_monitor, daemon=True)
    monitor_thread.start()
    
    print("📊 Background monitor started")
    print("🌐 Starting web interface...")
    print("=" * 50)
    print("📱 Web interface will be available at: http://localhost:8501")
    print("🔄 Background monitoring is running")
    print("=" * 50)
    print("Press Ctrl+C to stop the application")
    
    try:
        # Start Streamlit (this will block)
        run_streamlit()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down Flight Alert App...")
        print("✅ Application stopped successfully")

if __name__ == "__main__":
    main()
