
import os
import time
import requests
from datetime import datetime

count = 0
while True:
    current_second = datetime.now().second
    if current_second == 0:
        count += 1
        time_str=datetime.now().strftime("%Y%m%d%H%M%S")
        print(time_str)
        print("Condition met! Doing something...")

        # URL to fetch
        url = "https://img.lemino.docomo.ne.jp/cms/a140561/a140561_w1.jpg"+"?="+time_str

           
        # Telegram bot details (use environment variables if available, else fallback to placeholders)
        bot_token = os.environ.get("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
        channel_id = os.environ.get("TELEGRAM_CHAT_ID", "YOUR_CHANNEL_ID_HERE")
            
        # Telegram API URL for sending photo
        telegram_api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
            
        params = {'chat_id': channel_id, 'text': url}
        response = requests.post(telegram_api_url, params=params)
            
        if response.status_code == 200:
                print("Image sent successfully to Telegram channel.")
        else:
                print(f"Failed to send image. Error: {response.text}")


        time.sleep(1)

        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    if count >= 30:
        break