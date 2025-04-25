import pyautogui as pg
import time
import random
import webbrowser


webbrowser.open('https://www.youtube.com/@syscursos')
while True:
    print(pg.position())
    x = 1726
    y = 460

    pg.moveTo(x, y, duration=0.5)
    time.sleep(4)
    pg.click()