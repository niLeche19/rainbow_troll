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
from pynput.mouse import Listener

#for task getting
cmd = 'WMIC PROCESS get Caption'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

#variables
mouseDown = False
running = False
curTime = 0
avgClick = 70
sleepTime = 10
IS_RUNNING = "slack"

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
    global curTime, mouseDown
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
    time.sleep(sleepTime)

    # this will check every second if the specified program is running or not. It will update running accordingly
    if(int(time.time()) - curTime > 10):
        #print(running, mouseDown) #debugging

        if(checkFor(IS_RUNNING) and not(running)):
            running = True
            print("running")
            sleepTime = 0.02

        elif(not(checkFor(IS_RUNNING)) and running):
            running = False
            print("not running")
            sleepTime = 10
        curTime = int(time.time())

    elif(mouseDown and running): 
        print(mouseDown)
    
