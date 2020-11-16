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
IS_RUNNING = "VALORANT"

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
    # check each line in the running program output
    for line in proc.stdout:
        # check for a match with the case name
        if(getName(line) == progName):
            print("True")
            return True

    # if the loop finishes then there were no matches
    print("False")
    return False

def on_click(x, y, button, pressed):
    global curTime, mouseDown
    if(pressed):
        curTime = int(time.time() * 1000)
    else:
        #clicklist.append(int(time.time() * 1000) - curTime)
        print(int(time.time() * 1000) - curTime)

listener = Listener(on_click=on_click)
listener.start()
listener.stop()
# check if IS_RUNNING is running. Will print true or false
checkFor(IS_RUNNING)

while True:
    time.sleep(10)
    running = checkFor(IS_RUNNING)
    """
    if(checkFor(IS_RUNNING) and not(running)):
        running = True
    else:
        running = False
    """

time.sleep(10)
