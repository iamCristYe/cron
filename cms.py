import requests

import json
import time
import os
from telegram import Bot
from github import Github
from github import Auth
import base64

# af10450 b1029b6


# 发送压缩文件到Telegram
async def send_file_to_telegram():
    with open("cms.json") as f:
        data = json.load(f)
        start = int(data["last"] / 1000) * 1000 - 1
    telegram_token = os.environ["bot_token"]  # 替换为你的Telegram bot token
    telegram_chat_id = os.environ["chat_id"]  # 替换为你的频道或群组ID
    bot = Bot(token=telegram_token)
    archive_path = os.path.join(".", f"cms-{start}.txt")
    await bot.send_document(chat_id=telegram_chat_id, document=open(archive_path, "rb"))


def send_telegram_image(token, channel_id, url_img, message):
    while True:
        try:
            url = f"https://api.telegram.org/bot{token}/sendPhoto"
            payload = {
                "chat_id": channel_id,  # Channel ID with "@" (e.g., "@your_channel_id")
                "photo": url_img,
                "caption": message,
            }
            response = requests.post(url, data=payload)
            return response.json()
        except:
            time.sleep(10)


def hex_to_dec(hex_value):
    """
    Convert a hexadecimal string to a decimal integer.
    """
    try:
        decimal_value = int(hex_value, 16)
        return decimal_value
    except ValueError:
        return "Invalid hexadecimal value!"


def dec_to_hex(decimal_value):
    """
    Convert a decimal integer to a hexadecimal string.
    """
    try:
        decimal_value = int(decimal_value)  # Ensure input is an integer
        hex_value = hex(decimal_value).replace("0x", "").lower()
        return hex_value
    except ValueError:
        return "Invalid decimal value!"


async def main():
    data = {}
    need_update = False
    with open("cms.json") as f:
        data = json.load(f)
        if data["running"]:
            return
        start = int(data["last"])-10
        data["running"] = True
        with open("cms.json", "w") as f:
            json.dump(data, f)

        # using an access token
        auth = Auth.Token(os.environ["github_token"])

        # First create a Github instance:
        # Public Web Github
        g = Github(auth=auth)

        # Then play with your Github objects:
        repo = g.get_user().get_repo("cron")
        contents = repo.get_contents("cms.json")

        with open("cms.json", "r") as f:
            repo.update_file("cms.json", f"cms s {start}", f.read(), contents.sha)

        # To close connections after use
        g.close()

    for code in range(start, start+5000):  # (start, start + 500, 1):
        print(code)
        # Define the URL of the image
        hex_value = dec_to_hex(code)
        url = f"https://img.lemino.docomo.ne.jp/cms/{hex_value}/{hex_value}_w1.jpg"
        # crid = "crid://plala.iptvf.jp/group/" + hex_value
        # json_url = "https://if.lemino.docomo.ne.jp/v1/meta/contents?crid" + crid
        # lemino_url = (
        #     "https://lemino.docomo.ne.jp/contents/"
        #     + base64.b64encode(crid.encode()).decode()
        # )
        # res_str = url  # + "\n" + json_url + "\n" + lemino_url + "\n" + str(code) + "\n"
        # url = f"https://img.lemino.docomo.ne.jp/livecms/{hex_value}/thumbnail/w_0.png?width=128&auto=webp&quality=75"
        # url = f"https://img.lemino.docomo.ne.jp/livecms/live_s_000{code:05d}/thumbnail/thumbnail.png?width=256&auto=webp&quality=75"
        res_str = url
        print(res_str)
        # Send a GET request to the URL

        # Retry mechanism in case of connection issues
        while True:
            try:
                response = requests.get(url)
                # last_modified = response.headers.get("last-modified")

                # time.sleep(1)
                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    if len(response.content) > 6 * 1024:

                        # Save the content to a file
                        # with open(f"img/{code}.jpg", "wb") as file:
                        #     file.write(response.content)
                        with open(f"cms-{start}.txt", "a") as f:
                            f.write(res_str)
                        send_telegram_image(
                            os.environ["bot_token"],
                            os.environ["chat_id"],
                            url,
                            str(code) + "\n" + res_str,
                        )
                        need_update = True
                        print("Image saved successfully.")
                    else:
                        with open(f"cms-{start}.txt", "a") as f:
                            f.write(res_str + "\n" + " File < 6KB\n")
                        print("File < 6KB")
                    break
                else:
                    with open(f"cms-{start}.txt", "a") as f:
                        f.write(res_str + "\n" + " 404\n")
                    print(
                        "Failed to retrieve the image. Status code:",
                        response.status_code,
                    )
                    break

            except Exception as e:
                print(e)
                print("Connection lost. Retrying in 10 seconds...")
                time.sleep(10)  # Wait 10 seconds before retrying

        if code % 1000 == 0:
            while True:
                
                try:
                    break
                    await send_file_to_telegram()
                    break
                except:
                    print("send_file_to_telegram failed. Retrying in 10 seconds...")
                    time.sleep(10)  # Wait 10 seconds before retrying

    if need_update:
        # using an access token
        auth = Auth.Token(os.environ["github_token"])

        # First create a Github instance:
        # Public Web Github
        g = Github(auth=auth)

        # Then play with your Github objects:
        repo = g.get_user().get_repo("cron")
        contents = repo.get_contents("cms.json")

        data["last"] = start + 5000
        data["running"] = False
        with open("cms.json", "w") as f:
            json.dump(data, f)

        with open("cms.json", "r") as f:
            repo.update_file("cms.json", f"cms e {start}", f.read(), contents.sha)

        # To close connections after use
        g.close()


import asyncio

if __name__ == "__main__":
    asyncio.run(main())
