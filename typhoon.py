import requests
from bs4 import BeautifulSoup
import os

# URL to fetch
typhoon_url = "https://typhoon.yahoo.co.jp/weather/jp/typhoon/2515.html"

# Fetch the page
response = requests.get(typhoon_url)
response.raise_for_status()  # Raise an error for bad status codes

# Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Find all img tags with src starting with the specified URL
images = soup.find_all('img', attrs={'src': lambda s: s and s.startswith('https://weather-pctr.c.yimg.jp')})

if images:
    first_image_url = images[0]['src']
    print(f"Found first image: {first_image_url}")
    
    # Telegram bot details (replace with your actual values)
    bot_token = "YOUR_BOT_TOKEN_HERE"  # e.g., "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
    channel_id = "YOUR_CHANNEL_ID_HERE"  # e.g., "@yourchannel" or "-1001234567890"
    
    TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
    TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

    # Telegram API URL for sending photo
    telegram_api_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
    
    # Parameters for the request
    params = {
        'chat_id': TELEGRAM_CHAT_ID,
        'photo': first_image_url
    }
    
    # Send the request
    response = requests.get(telegram_api_url, params=params)
    
    if response.status_code == 200:
        print("Image sent successfully to Telegram channel.")
    else:
        print(f"Failed to send image. Error: {response.text}")
else:
    print("No images found starting with 'https://weather-pctr.c.yimg.jp'.")