import os
import sys
import time
import string
import random

global username
global starterWeapon

def main():
    # read info using sql
    def explore():
        while True:
            try:
                stopSearching = str(input("Currently exploring!\n\n[Press X to stop exploring]")).lower()
            except:
                continue
            else:
                if stopSearching == 'x':
                    break
                else:
                    continue

        time = random.randrange(5, 15)
        print(time)

        for i in time:
            time.sleep(1)
            sys.clear()
            print(f"Time elapsed: {i}")



def starterWeaponChoice():
    while True:
        try:
            starterWeapon = int(input("Choose your starter weapon\n\n(1) AK47 | (2) AR-15 | (3) M1911\n\nChoice: "))
            if starterWeapon == 1:
                print("sql")
                break
            elif starterWeapon == 2:
                print("sql")
                break
            elif starterWeapon == 3:
                print("sql")
                break
            else:
                continue
        except:
            continue

    while True:
        try:
            confirmWeapon = int(input(f"Is this the weapon you want? {starterWeapon}\n\n (1) Yes | (2) No\n\nChoice: "))
        except:
            continue
        else:
            if confirmWeapon == 1:
                intro()
                break
            elif confirmWeapon == 2:
                starterWeaponChoice()
            else:
                continue

def intro():
    global starterWeapon 

    if starterWeapon == 'N/A':
        input("Universal Studios Production")
        input("Made by WolvTMG\n\n[Enter] to continue")

        input(f"Welcome to Rainfare, {username}, choose your starter weapon")
        starterWeaponChoice()
    else:
        input(f"Character Info:\n\nUsername: {username}\nHP: 100\nMain weapon: {starterWeapon}\nBag: {starterWeapon}")
        main()


def newSave():
    while True:
        try:
            username = str(input("Username: "))
            break
        except:
            continue

    input(f"Welcome, {username}")
    while True:
        try:
            confirmUsername = int(input(f"Would you like to keep this name?\n\n (1) Yes | (2) No\n\nChoice: "))
        except:
            continue
        else:
            if confirmUsername == 1:
                intro()
                break
            elif confirmUsername == 2:
                newSave()
                break
            else:
                continue

def loadSave():
    print("WIP")


newSave()
