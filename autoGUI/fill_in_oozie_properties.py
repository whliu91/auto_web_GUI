##############################################################
# This script is for testing auto typing all properties fields
# for a rce oozie workflow, it is tested on a screen of
# 1920*1080
# Usage: on Ambari import workflow from local and click submit
# Then, run this script directly.
# To stop execution, move mouse to top left of screen
# Currently work only on primary screen
##############################################################

import pyautogui
import time
import os

properties_file = os.path.join("resource", "mem.properties")
properties = []
with open(properties_file) as f:
    for line in f:
        properties.append(line.replace("\n", ""))

pyautogui.moveTo(790, 294)
pyautogui.click()
time.sleep(1)
pyautogui.typewrite(properties[0], interval=0.1)
pyautogui.moveTo(695, 320)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(695, 358)
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(726, 504)
pyautogui.click()
time.sleep(1)

for i in range(len(properties)-1):
    pyautogui.typewrite(properties[i+1], interval=0.1)
    pyautogui.hotkey('tab')
    time.sleep(0.5)

time.sleep(1)
pyautogui.moveTo(1467, 834)
pyautogui.click()
