 #!/usr/bin/env python3
"""
Script to fetch data from Golf Genius API
"""

import requests
import json
import sys
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

def get_golf_genius_data():
    url = f"https://www.golfgenius.com/api_v2/{api_key}/events/11616205264390239025/roster"
    
    try:
        print(f"Sending GET request to: {url}")
        response = requests.get(url)
        
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print("\nResponse Body:")
        
        # Try to parse as JSON for better formatting
        try:
            json_data = response.json()
            print(json.dumps(json_data, indent=2))
        except json.JSONDecodeError:
            # If not JSON, print raw text
            print(response.text)
            
        return response
        
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None

if __name__ == "__main__":
    get_golf_genius_data()