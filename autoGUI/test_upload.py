import pyautogui
import time

# this is for 1920*1080
# on Ambari UI, click upload
pyautogui.moveTo(1797, 183)
pyautogui.click()
time.sleep(2)
# click to browse file
pyautogui.moveTo(947, 351)
pyautogui.click()
time.sleep(3)

'''
pyautogui.doubleClick()

pyautogui.moveRel(None, 10)
pyautogui.moveTo(1800, 500, duration=2, tween=pyautogui.easeInOutQuad)
pyautogui.typewrite('Hello world!', interval=0.25)
pyautogui.press('esc')
pyautogui.keyDown('shift')
pyautogui.press(['left', 'left', 'left', 'left', 'left', 'left'])
pyautogui.keyUp('shift')
pyautogui.hotkey('ctrl', 'c')
'''