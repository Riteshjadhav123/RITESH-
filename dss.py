import random

import pyautogui as pg

import time

animal=('monkey','donkey','dog','cat')
messages = ['you are a ', 'you are a brave ', 'you are a funny ', 'you are STRONG ']
time.sleep(0.1) 

for i in range(50):
    a=random.choice(animal)
    m=random.choice(messages)+a
    pg.write(m)
    pg.press('enter')
    time.sleep(0.1)
    