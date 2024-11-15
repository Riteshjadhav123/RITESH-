import random
import pyautogui as pg
import time
from datetime import datetime, timedelta

# List of animals and messages
animals = ['monkey', 'donkey', 'dog', 'cat']
messages = ['you are a ', 'you are a brave ', 'you are a funny ', 'you are STRONG ']

# Define the target time
target_hour = 10  # 12 AM is 0 hours in 24-hour format
target_minute = 53

# Get the current time
now = datetime.now()

# Calculate the target time for today or tomorrow
target_time = now.replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)
if now > target_time:
    target_time += timedelta(days=1)

# Calculate the time to wait
time_to_wait = (target_time - now).total_seconds()
print(f"Waiting for {time_to_wait} seconds until 12:30 AM IST.")

# Wait until the target time
time.sleep(time_to_wait)

# Send messages
for i in range(50):
    animal = random.choice(animals)
    message = random.choice(messages) + animal
    pg.write(message)
    pg.press('enter')
    time.sleep(0.1)
