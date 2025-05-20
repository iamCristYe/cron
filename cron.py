import time
from datetime import datetime
import os
import subprocess

data = {}
data["environ"] = str(os.environ)
for code in range(1, 11, 1):
    data[f"CMD_{code}"] = [os.environ[f"CMD_{code}"]]

# First loop: check every 10 seconds if current hour is 0 mod 4
while True:
    current_hour = datetime.now().hour
    if current_hour % 4 == 0:
        break
    time.sleep(50)

# Second loop: check if (minute - 5) mod 15 is 0
count = 0  # run 4 hr * 4 times per hour = 16 times
while True:
    current_minute = datetime.now().minute
    if (current_minute - 3) % 15 == 0:
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("Condition met! Doing something...")
        count += 1
        subprocess.run(data["CMD_3"], shell=True)
        subprocess.run(data["CMD_5"], shell=True)
        subprocess.run(data["CMD_7"], shell=True)
        subprocess.run(data["CMD_9"], shell=True)
        subprocess.run(data["CMD_10"], shell=True)
    else:
        time.sleep(40)

    if count >= 16:
        subprocess.run(data["CMD_1"], shell=True)
        subprocess.run(data["CMD_2"], shell=True)
        subprocess.run(data["CMD_4"], shell=True)
        subprocess.run(data["CMD_6"], shell=True)
        subprocess.run(data["CMD_8"], shell=True)
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        break
