import random
import pyautogui as pg
import time
from datetime import datetime, timedelta

# List of animals and messages
animals = ['monkey', 'donkey', 'dog', 'cat']
messages = ['you are a ', 'you are a brave ', 'you are a funny ', 'you are STRONG ']

# Define the target time
target_hour = 11 # 6 PM in 24-hour format
target_minute =4
# Get the current time
now = datetime.now()
print(f"Current time: {now}")

# Calculate the target time for today or tomorrow
target_time = now.replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)
if now > target_time:
    target_time += timedelta(days=1)

print(f"Target time: {target_time}")

# Calculate the time to wait
time_to_wait = (target_time - now).total_seconds()
print(f"Waiting for {time_to_wait} seconds until {target_hour}:{target_minute} IST.")

# Wait until the target time
time.sleep(max(0, time_to_wait))

# Send messages
for i in range(50):
    animal = random.choice(animals)
    message = random.choice(messages) + animal
    print(f"Sending message: {message}")  # Debugging line to verify message content
    pg.write(message)
    pg.press('enter')
    time.sleep(1)
print("Script finished.")
