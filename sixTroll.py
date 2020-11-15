import string
import subprocess
import sys
from time import sleep
cmd = 'WMIC PROCESS get Caption'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

strTest = ""
recurse = 0

def getName(linee):
    strOut = ""

    for i in linee:
        if(chr(i).isalpha()):
            strOut += chr(i)
        else:
            print(strOut)
            break


for line in proc.stdout:
    strTest = line
    if (recurse > 2):
        break
    recurse += 1
    getName(strTest)
    print(strTest)


