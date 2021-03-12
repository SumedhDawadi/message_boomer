import pyfiglet

ascii_banner = pyfiglet.figlet_format(\
'''
Message Boomer: 

   ''')
   

print(ascii_banner)
import pyautogui
import time
while True:
    pyautogui.typewrite("I Love you!")                                 #@AUTHOR: SUMEDH DAWADI
    time.sleep(1)
    pyautogui.press('enter')



