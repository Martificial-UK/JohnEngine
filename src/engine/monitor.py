# monitor.py
# Simple monitoring and alerting example
import time

def monitor_health(health_check, interval=10):
    while True:
        results = health_check.run()
        print(f"Health: {results}")
        # Add alerting logic here (e.g., send email/webhook if error)
        time.sleep(interval)
