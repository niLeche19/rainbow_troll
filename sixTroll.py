import string
import subprocess
import sys
from time import sleep
import pyautogui as pag

cmd = 'WMIC PROCESS get Caption'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

recurse = 0

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

# check if IS_RUNNING is running. Will print true or false
checkFor(IS_RUNNING)


