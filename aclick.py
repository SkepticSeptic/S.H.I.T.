import os    
import time as t
import pyautogui as pg
import threading
def aclick():
    while True:
        pcCores = int(os.cpu_count())
        intensity = int(input("PC Contains " + str(pcCores) + " cores. Set intensity to: (1 to 5 recommended, dangerous going above that.)"))

        pcStrength = pcCores * intensity
        totalClicks = 0
        main_time = t.time()

        def increment_total_clicks():
            global totalClicks
            pg.doubleClick() 
            totalClicks += 1

        rnge = int((50 * intensity) / 2)
        for j in range(rnge):
            start_time = t.time()
            threads = []
            for i in range(pcStrength):
                th = threading.Thread(target=lambda: increment_total_clicks())
                th.start()
                threads.append(th)
            for th in threads:
                th.join()
            end_time = t.time()
            elapsed_time = end_time - start_time
            print("(" + str(j+1) + "/" + str(rnge) + ") " + "iteration done in " + str(elapsed_time) + " seconds.")
        #print("Total clicks:", totalClicks)

        main_endTime = t.time()
        main_elapsedTime = main_endTime - main_time
        print("full thing completed in: " + str(main_elapsedTime) + " seconds.")
