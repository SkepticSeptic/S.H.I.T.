import time as t
import pyautogui as pg

def nbrute():
    while True:
        # Gather variables:
        min_val = input("Enter minimum value: ")
        if exit(min_val):
            break
        max_val = input("Enter maximum value: ")
        if exit(max_val):
            break
        entr = input("Press enter after each number? (y/n): ")
        if exit(entr):
            break
        delay = input("Delay after each number: ")
        if exit(delay):
            break

        # Wait then start
        print("Starting in 3 seconds")
        t.sleep(3)

        # Main loop
        for i in range(int(max_val)):
            pg.write(str(i + int(min_val)))
            if entr.lower() == "y":  # If enters are true, enter after each num
                pg.press("enter")
            t.sleep(float(delay))  # Wait delay amount of seconds



def exit(dot):
    if dot == "..":
        return True
    else:
        return False