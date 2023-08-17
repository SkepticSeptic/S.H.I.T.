#imports
import threading
import os
import time as t
import subprocess as sp
import getpass as pswd
import color

# tools
import aclick
import sabotage
import nbrute
import sshmaster
import shodanSearch
import agressiveScanner

try:
    import pyautogui as pg
except:
    print("[ WARN ] PyAutoGUI is not installed.")

#TODO- research locateOnWindow


#welcome the user with a cringey screen:
def welcomeUser(listOfCommands):
    print("________________________________________________________________\n")
    print(color.success("Welcome to Skeptic's Hacking Interface Tool! (S.H.I.T.)\n\n"))
    print(color.warning("note: this was built on and for linux/unix systems."))
    print("List of commands:\n")
    for i in range(len(listOfCommands)):
        print(color.progress(" - " + listOfCommands[i]))
def skull():
        print("""
                 ___-----------___
           __--~~                 ~~--__
       _-~~                             ~~-_
    _-~                                     ~-_
   /                                           \\
  |                                             |
 |                                               |
 |                                               |
|                                                 |
|                                                 |
|                                                 |
 |                                               |
 |  |    _-------_               _-------_    |  |
 |  |  /~         ~\           /~         ~\  |  |
  ||  | 0          |         | 0          |  ||
  || |               |       |               | ||
  || |              |         |              | ||
  |   \_           /           \           _/   |
 |      ~~--_____-~    /~V~\    ~-_____--~~      |
 |                    |     |                    |
|                    |       |                    |
|                    |  /^\  |                    |
 |                    ~~   ~~                    |
  \_         _                       _         _/
    ~--____-~ ~\                   /~ ~-____--~
         \     /\                 /\     /
          \    | ( ,           , ) |    /    __________________________
           |   | (~(__(  |  )__)~) |   |    / W e L c O m E !           \\
            |   \/ (  (~~|~~)  ) \/   |    < Ye be warned and only use   |
             |   |  [ [  |  ] ]  /   |      \   this on yer own devices! |
              |                     |        \__________________________/
               \                   /
                ~-_             _-~
                   ~--___-___--~"""
                   )



#numberbrute: spam numbers every "delay" seconds starting from min and ending at max, and pressing enter after every number if user requests so
def numberbrute():
    nbrute.nbrute()

def autoclickutil():
    aclick.aclick()

def sabotageutil():
    sabotage.sabotage()

def sshmastercli():
    sshmaster.sshmastercli()
def sshmastergui():
    sshmaster.sshmastergui()

def shodanSearcher():
    shodanSearch.shodanSearch()

def scannerutil():
    agressiveScanner.aggressiveScan()
