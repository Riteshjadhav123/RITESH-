import pyautogui
import time

# Give yourself enough time to open WhatsApp Web and position the window
time.sleep(0.1)

s = "hi"
for i in range(20):
    pyautogui.typewrite(s)
    pyautogui.press("enter")
    time.sleep(0.1)
    