import webbrowser
import time
import os
import pyautogui

count = 0
limit = 20 # number of times to visit the site
url = 'http://10.0.2.169:3000/' # the url you want to visit

while(count != limit):
    webbrowser.open_new_tab(url) # open in a new browser page
    print(count)
    # os.system("taskkill /im chrome.exe /f")
    time.sleep(3) # wait x seconds
    pyautogui.moveTo(1910,5)
    pyautogui.click()
    count = count + 1 