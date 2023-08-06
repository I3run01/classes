import pyautogui
import time

pyautogui.press('winleft') 
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('https://web.whatsapp.com/')
pyautogui.press('enter')
time.sleep(4)
pyautogui.press('F11')
time.sleep(2)
pyautogui.click(x = 400, y = 98)
pyautogui.write('Gil Amor')
time.sleep(2)
pyautogui.click(x = 400, y = 220)
time.sleep(1)
pyautogui.write('Eu sou um robo, mas eu ainda continuo te amando S2 S2 S2')
pyautogui.press('enter')
