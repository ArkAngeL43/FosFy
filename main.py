import os 
import sys 
import time 
import datetime 
from datetime import datetime
import random
import requests
from time import sleep
from rich.console import Console
import socket


def clear():
    print("\x1b[H\x1b[2J\x1b[3J") 
#
#
# user data
def token():
    tok = open("token.txt", 'r')
    tok1 = tok.readlines()
    for line in tok1:
        print("[+] Token In Use -> {}".format(line.strip()))
#
#animation for sleep 
#
#
def animation():
    console = Console()
    tasks = [f"task {n}" for n in range(0,1)]
    with console.status("[bold green]Sleeping......") as status:
        while tasks:
            task = tasks.pop(0)
            sleep(43200)
            console.log(f"{task} Sleep finished ")
#
# testing connection
def testcon():
    console = Console()
    tasks = [f"task {n}" for n in range(0,1)]
    with console.status("[bold green]Working on tests....") as status:
        while tasks:
            task = tasks.pop(0)
            sleep(1)
            console.log(f"Done")
    r = requests.get("https://www.discord.com")
    if r.status_code == 200:
        console.log("[ + ] Status:  Server responded with code 200")
        console.log("[ + ] Status:  Connection is stable")
        console.log("[ + ] Status:  Status Server code -> ", r.status_code)
    else:
        console.log("[ + ] Status:  Server responded with a code out of range")
        console.log("[ + ] Status:  Connection is stable")
        console.log("[ + ] Status:  Status Server code -> ", r.status_code)
    sock2 = socket.gethostbyname('www.discord.com')
    console.log("[ + ] Data: Connection on  > ", sock2)
    print("\n")
#
#banner 
#
#
def banner():
    print("""
 _____         ___     
|   __|___ ___|  _|_ _ 
|   __| . |_ -|  _| | |
|__|  |___|___|_| |_  |
                  |___|
______________________________________
Discord Message Automation made simple    
    """)
#
# basic/entry level messaging
def basicmes():
    #
    #
    #
    # token
    tok = open("token.txt", 'r')
    tok1 = tok.readlines()
    for line in tok1:
        print("[ + ] Read current token")
    ### token and message formating
    mylist = ["Hello! goodmorning/goodnight", "Hope everyone has a good night/day!", "Good evening/night, hope everyones chill :D "]
    random.shuffle(mylist)
    header = {
    'authorization': '{}'.format(line.strip())
    }
    payload = {
        'content': mylist
    }
    # id's to send the message to
    #
    #
    #
    with open(r"IDlist.txt", 'r') as fp:
        num_lines = sum(1 for line in fp)
    print('[ + ] Total IDS in file ~~> ', num_lines) # 8
    i = open("IDlist.txt", 'r')
    ii = i.readlines()
    for line in ii:
        print("[ + ] ID's parsed ~~> ", line)
    r = requests.post("https://discord.com/api/v9/channels/{}/messages".format(line.strip()), data=payload, headers=header)



def main():
    pa = str(input(" Password > "))
    os.system(f"cd login ; go run main.go -p {pa} ; clear ")
    clear()
    banner()
    while True:
        try:
            testcon()
            print("[ + ] Status: Sleeping")
            print("[ + ] Status: Sleeping for : 43200 seconds 12 hours")
            animation()
            basicmes()
            print("[ + ] Status: Message sent, process completed, sleeping till the next")
        except SyntaxError:
            print("[ - ] Syntax error detected [ ? ] ")
        except KeyboardInterrupt:
            print("[ - ] Shutting down....")
            sys.exit()

if __name__ == "__main__":
    main()