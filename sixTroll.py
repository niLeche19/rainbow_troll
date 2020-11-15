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

import string
import subprocess
import sys
import time

sys.path.append("D:\Python stuff\Lib\site-packages")
import pyautogui as pag
from pynput.mouse import Listener

cmd = 'WMIC PROCESS get Caption'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)


IS_RUNNING = "chrome"

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

curTime = 0
clicklist = []
def on_click(x, y, button, pressed):
    global curTime, clicklist
    if(pressed):
        curTime = int(time.time() * 1000)
    else:
        print(int(time.time() * 1000) - curTime)
        clicklist.append(int(time.time() * 1000) - curTime)
        #print(curtime % 1000)
    #print ("Mouse clicked")

listener = Listener(on_click=on_click)
listener.start()

# check if IS_RUNNING is running. Will print true or false
checkFor(IS_RUNNING)

time.sleep(10)
print(sum(clicklist) / len(clicklist))
