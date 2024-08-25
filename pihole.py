#!/usr/bin/env python

import time
import fourletterphat
import requests

print("""
Four Letter pHAT: pihole.py

This example will display your Pi-hole
percentage blocked queries on the
Four Letter pHat.

Press Ctrl+C to exit.
""")

# Replace this with your Pi-hole IP address or domain name and API key
PIHOLE_URL = 'http://xxx/admin/api.php'
API_KEY = '1234'

while True:
    params = { 
        'summaryRaw': '',  # This returns a more detailed set of data
        'auth': API_KEY
    }
    try:
        response = requests.get(PIHOLE_URL, params=params)
        response.raise_for_status  # Raises an error for bad HTTP status codes
        data = response.json()
        blocked_percentage = data['ads_percentage_today']
    except Exception as e:
        print(f"Error querying Pi-hole API: {e}")
        time.sleep(60)
        continue

    # Update phat display
    fourletterphat.clear()
    fourletterphat.print_float(blocked_percentage, decimal_digits=2, justify_right=True)
    fourletterphat.show()

    time.sleep(60)

