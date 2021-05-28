import pyautogui


pyautogui.moveTo(10,10 duration=1.5)

#slm upper left corner if stuck in loop with pyautogui

#cmd python.exe import pyautogui pyautogui.displayMousePosition()
# show x,y (coordinates)  r,g,b (colors)
# Ctrl-C to quit,
###Doesn't work in IDLE
#separating by semicolon (;) causes both commands to occur at once

pyautogui.typewrite('Hello world!' interval = 0.2)
pyautpgui.press('')
pyautoqui.screenshot()  #brings up a pil.Image.Image
pyautogui.screenshot('c\\myfiles\\screenshot_example.png') # saves file
pyautogui.locateOnScreen("cropped image filename")   #image on screen
#tuple of location X, Y, W,H (top left of region)
pyautogui.locateCenterOnScreen('filename')
