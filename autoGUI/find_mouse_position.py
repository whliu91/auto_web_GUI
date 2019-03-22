import pyautogui

screenWidth, screenHeight = pyautogui.size()

print("screen width is {width}, screen height is {height}".format(width=screenWidth, height=screenHeight))
currentMouseX, currentMouseY = pyautogui.position()
print("currentMouseX is {x}, currentMouseY is {y}".format(x=currentMouseX, y=currentMouseY))