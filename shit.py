#imports
import threading
import os
import time as t
import subprocess as sp
import getpass as pswd
import aclick
import sabotage
try:
    import pyautogui as pg
except:
    print("[ WARN ] PyAutoGUI is not installed.")

#TODO- research locateOnWindow

#welcome the user with a cringey screen:
def welcomeUser(listOfCommands):
    print("________________________________________________________________\n")
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
    print("Welcome to Skeptic's Hacking Interface Tool! (S.H.I.T.)\n\n")
    print("note: this was built on and for linux/unix systems.")
    print("List of commands:\n")
    for i in range(len(listOfCommands)):
        print(" - " + listOfCommands[i])




#numberbrute: spam numbers every "delay" seconds starting from min and ending at max, and pressing enter after every number if user requests so
def numberbrute():
    #gather variables:
    min = input("Enter minimum value: ")
    max = input("Enter maximum value: ")
    entr = input("Press enter after each number? (y/n): ")
    delay = input("Delay after each number: ")
    #wait then start
    print("Starting in 3 seconds")
    t.sleep(3)
    #main
    for i in range(int(max)):
        pg.write(str(i + int(min)))
        if entr.lower() == "y": #if enters are true, enter after each num
            pg.press("enter")
        
        t.sleep(float(delay)) #wait delay amount of seconds

def autoclickutil():
    aclick.aclick()
def sabotageutil():
    sabotage.sabotage()