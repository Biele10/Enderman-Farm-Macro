import pyautogui
import time

# to end this program the user needs to swing their mouse button to the bottom right of the screen
# pyautogui recognises this and will stop the program

a=10        # basic variables to keep the loop going
b=0
food_count=0     # counter used to track when player needs to eat

time.sleep(4)

while a > b:                    # this section of code is what moves the player from left to right by the enderman farm
    pyautogui.click()           # this ensures that the player hits all the enderman that have spawned
    pyautogui.keyDown("A")
    time.sleep(0.45)
    pyautogui.click()
    pyautogui.keyUp("A")
    pyautogui.keyDown("D")
    time.sleep(0.45)
    pyautogui.click()
    pyautogui.keyUp("D")

    food_count+=1       # food_count increments by 1

    if food_count > 50:
        pyautogui.press("4")            # player must hold food in slot 4 so that food can be eaten
        pyautogui.mouseDown(button="right")
        time.sleep(10)
        pyautogui.mouseUp(button="right")
        pyautogui.press("1")
        food_count = 0       # player will only eat again once c reaches 50 again
    else:
        print(":)")
