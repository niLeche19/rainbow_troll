import subprocess
import sys
from time import sleep
cmd = 'WMIC PROCESS get Caption'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)

for line in proc.stdout:
    print(line)

sleep(2)

def getName(linee):
    for i in linee:
        
"""
for line in proc.stdout:
    print (line)

import sys
from time import sleep
from os import system

sys.path.append("D:\Python stuff\Lib\site-packages")
import pyautogui as PAG

PAG.sleep = 0.1

print(sys.argv[0])


system('cmd /k "tasklist > D:\Downloads\task_list.txt"')
#os.system('cmd /k "Your Command Prompt Command"')
"""



