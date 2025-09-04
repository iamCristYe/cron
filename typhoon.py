import requests
from bs4 import BeautifulSoup
import os

import time
from datetime import datetime
import os
import subprocess

# First loop: check every 10 seconds if current hour is 0 mod 4
while True:
    current_hour = datetime.now().hour
    if current_hour % 4 == 0:
        break
    time.sleep(50)

count = 0
while True:
    current_minute = datetime.now().minute
    if (current_minute - 3) % 60 == 0:
        count += 1
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("Condition met! Doing something...")

        # URL to fetch
        typhoon_url = "https://typhoon.yahoo.co.jp/weather/jp/typhoon/2515.html"

        # Directory to save the image
        save_dir = "images"
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

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
            
            # Download and save the image
            image_response = requests.get(first_image_url)
            image_response.raise_for_status()
            
            # Extract filename from URL or use a default
            image_filename = os.path.join(save_dir, first_image_url.split('/')[-1] or "typhoon_image.jpg")
            
            with open(image_filename, 'wb') as f:
                f.write(image_response.content)
            print(f"Image saved to {image_filename}")
            
            # Telegram bot details (use environment variables if available, else fallback to placeholders)
            bot_token = os.environ.get("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
            channel_id = os.environ.get("TELEGRAM_CHAT_ID", "YOUR_CHANNEL_ID_HERE")
            
            # Telegram API URL for sending photo
            telegram_api_url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
            
            # Send the image as a file
            with open(image_filename, 'rb') as photo:
                files = {'photo': photo}
                params = {'chat_id': channel_id}
                response = requests.post(telegram_api_url, params=params, files=files)
            
            if response.status_code == 200:
                print("Image sent successfully to Telegram channel.")
            else:
                print(f"Failed to send image. Error: {response.text}")
        else:
            print("No images found starting with 'https://weather-pctr.c.yimg.jp'.")

    if count >= 4:



        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        break