"""
Author: Nick Lee
Date created: 11.12.2020
Date last modified: 11.13.2020

project:
This program will make spray patterns in valorent intollerable

Citations: 
https://stackoverflow.com/questions/3429250/determining-running-programs-in-python
https://pyautogui.readthedocs.io/en/latest/
https://nitratine.net/blog/post/how-to-get-mouse-clicks-with-python/ #not used
https://pypi.org/project/pynput/ #i used this instead
"""

#imports
import string
import subprocess
import sys
import time
sys.path.append("D:\Python stuff\Lib\site-packages")
import pyautogui as pag
from pynput.mouse import Listener, Controller
from random import randint

#for task getting
cmd = 'WMIC PROCESS get Caption'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

#variables
timeDown = 0 # how long the mouse mas ben depressed
mouseDown = False # true if the mouse is down
mouseDownTwo = False # for resetting timeDown
running = False # true if IS_RUNNING is running
curTime = 0 # for checking when to check if isRunning
DEPRESSO = 90
SLEEP_TIME = 2 # the loop delay, this reduces when the program is running
IS_RUNNING = "slack" # this is the program you want to check for
CHECK_DELAY = 1 # how long the program waits before checking if running again

# this is the velocity of the mouse when depressed
XVEL = 10
YVEL = -10

def getName(linee):
    # this is the output string
    strOut = ""

    # check each char in the input string
    for i in linee:
        # if the char is alphabetical then add it to the output string
        if(chr(i).isalpha()):
            strOut += chr(i)
        else:
            # if the char is not alphabetical then end the loop and output the string
            return(strOut)

def checkFor(progName):
    global running
    # check each line in the running program output
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for line in proc.stdout:
        # check for a match with the case name
        if(getName(line) == progName):
            return True

    # if the loop finishes then there were no matches
    return False


#this is a little multi-threaded bastard but it works
def on_click(x, y, button, pressed):
    global mouseDown
    #this will constantly update mouseDown to True or False
    if(pressed):
        mouseDown = True
    else:
        mouseDown = False

listener = Listener(on_click=on_click)
listener.start()

# check if IS_RUNNING is running. Will print true or false. This only runs once
print(checkFor(IS_RUNNING))

curTime = int(time.time())
while True:
    # small delay as to not overload the CPU
    time.sleep(SLEEP_TIME)
    
    # this will check every second if the specified program is running or not. It will update running accordingly
    if(int(time.time()) - curTime > CHECK_DELAY):
        #print(running, mouseDown) #debugging
        print("checking")

        if(checkFor(IS_RUNNING) and not(running)):
            running = True
            print("running")
            SLEEP_TIME = 0.02
            CHECK_DELAY = 20

        elif(not(checkFor(IS_RUNNING)) and running):
            running = False
            print("not running")
            SLEEP_TIME = 10
            CHECK_DELAY = 5

        curTime = int(time.time())

    # if the mouse is released and mouseDownTwo is True
    if(not(mouseDown)):
        #print("mouse up")
        mouseDownTwo = False
        timeDown = 0

    # if the mouse if pressed and the program is running
    if(mouseDown and running):
        # check if mouseDownTwo to reset the timeDown
        if(not(mouseDownTwo)):
            timeDown = int(time.time() * 1000)
            #print("mouse down")
            mouseDownTwo = True
        
        #print(int(time.time() * 100) - timeDown)

        # if the mouse has been depressed for over 90ms then move it
        if(int(int(time.time() * 1000) - timeDown) > DEPRESSO):
            Controller().move(randint(-(XVEL),XVEL), YVEL)

        #print(mouseDown, timeDown, int((time.time()-timeDown) * 100)) # debugging
    
