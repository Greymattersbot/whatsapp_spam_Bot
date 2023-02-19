import pyautogui as pg
import webbrowser as wb
import time

wb.open("https://web.whatsapp.com")
time.sleep(30)

for i in range(100):
    pg.typewrite("Hello its GreyMatters here")
    pg.press("enter")
