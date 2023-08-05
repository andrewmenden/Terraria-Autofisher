from numpy import False_
from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con
import os

#user inputted info
hpPixel = [2477, 77]
settingsPixel = [2397, 1403]

def clear():
    os.system("cls")
def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

position = pyautogui.position()
size = pyautogui.size()

def setPosition():
    global position
    position = pyautogui.position()
    print(str(position.x)+", "+str(position.y))

def autoFish():
    clear()
    sleep(1)
    print("auto fishing...")
    global position
    global hpPixel
    hpColor = pyautogui.pixel(hpPixel[0],hpPixel[1])

    numberOfCatches = 0

    pyautogui.moveTo(size.width/2,position.y+50)
    click()
    sleep(0.5)

    pause = False
    while not pause:
        color = pyautogui.pixel(position.x,position.y)
        while True:
            sleep(0.1) #trying not to destroy my computer, shorter is probably more accurate
            if keyboard.is_pressed('alt+p'):
                print("paused")
                pause = True
                break
            if pyautogui.pixel(position.x,position.y) != color:
                click()

                clear()
                numberOfCatches+=1
                print(f"caught {numberOfCatches}")
                
                sleep(0.2)
                pyautogui.moveTo(size.width/2,position.y+50)
                click()
                sleep(1)
            if pyautogui.pixel(hpPixel[0],hpPixel[1]) != hpColor:
                print("damage taken")
                print("sleeping")
                pyautogui.moveTo(settingsPixel[0],settingsPixel[1])
                click()
                pyautogui.keyDown('esc')
                sleep(0.2)
                pyautogui.keyUp('esc')
                sleep(0.2)
                click()
                pause = True
                break



def testPosition():
    pyautogui.moveTo(size.width/2,position.y+50)
    print("in position")

keyboard.add_hotkey('alt+l', setPosition)
keyboard.add_hotkey('alt+j', autoFish) # start autofishing
keyboard.add_hotkey("alt+c", testPosition)
keyboard.wait('alt+e')