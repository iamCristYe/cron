import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# URL to fetch
typhoon_url = "https://typhoon.yahoo.co.jp/weather/jp/typhoon/2515.html"

# Set up headless Chrome browser to render JavaScript
options = Options()
options.headless = True  # Run in headless mode (no GUI)
driver = webdriver.Chrome(options=options)  # Requires ChromeDriver installed and in PATH

# Fetch the rendered page
driver.get(typhoon_url)
html = driver.page_source
driver.quit()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find all img tags with src starting with the specified URL
images = soup.find_all('img', attrs={'src': lambda s: s and s.startswith('https://weather-pctr.c.yimg.jp')})

if images:
    first_image_url = images[0]['src']
    print(f"Found first image: {first_image_url}")
    
    # Telegram bot details (replace with your actual values)
    bot_token = "YOUR_BOT_TOKEN_HERE"  # e.g., "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
    channel_id = "YOUR_CHANNEL_ID_HERE"  # e.g., "@yourchannel" or "-1001234567890"
    
    # Telegram API URL for sending photo
    telegram_api_url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    
    # Parameters for the request
    params = {
        'chat_id': channel_id,
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