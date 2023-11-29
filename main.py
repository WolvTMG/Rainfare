import os
import sys
import time
import string
import random
import sqlite3
from threading import Thread

global username

eql = sqlite3.connect('data.db')

eq = eql.cursor()

# eq.execute("""CREATE TABLE users (
# user text,
# hp int,
# cash int,
# level int, 
# xp int,
# gun1 text,
# gun2 text,
# gun3 text,
# gun4 text,
# potion1 text,
# potion2 text,
# potion3 text,
# potion4 text
# )""")

# eql.commit()
# eql.close()

def main():
    # read info using sql
    def explore():
        global searching

        eq.execute(""" SELECT gun1, gun2, gun3, gun4 FROM users WHERE user = ?; """, (username))
        result = eq.fetchall()
        x = 0
        print(result)
        for i in result:
            x = x + 1
        input(x)
        if x == 0:
            input("You have no guns!")
            menu()
        else:
            while True:
                try:
                    choice = int(input("Choose gun\n\nChoice: "))
                except:
                    continue
                else:
                    if choice == 1:
                        print(result[0][0])
                        if result[0][0] != 'N/A':
                            
                            timex = random.randrange(5, 15)
                            print(timex)

                            searching = False

                            def search():
                                print("search started")
                                while searching:
                                    # try:
                                        stopSearching = str(input("Currently exploring!\n\n[Press X to stop exploring]")).lower()
                                    # except:
                                        # continue
                                    # else:
                                        if stopSearching == 'x':
                                            break
                                        else:
                                            continue
                            
                            def loop():
                                global searching
                                searching = True    
                                for i in range(timex):
                                    time.sleep(1)
                                    # os.system('clear')
                                    # print(f"Time elapsed: {i}")
                                searching = False

                            loo = Thread(target=loop, daemon=True)
                            sea = Thread(target=search, daemon=True)

                            loo.start()
                            sea.start()


    def lootCrates():
        print("WIP")

    def menu():
        while True:
            try:
                choice = int(input("(1) Explore | (2) View Bag | (3) Loot Crates | (4) Leave\n\nChoice: "))
            except:
                continue
            else:
                if choice == 1:
                    explore()
                    break
                elif choice == 2:
                    print("WIP")
                    continue
                elif choice == 3:
                    lootCrates()
                elif choice == 4:
                    sys.exit()
                else:
                    continue

    menu()
                     



def starterWeaponChoice():
    while True:
        try:
            starterWeapon = int(input("Choose your starter weapon\n\n(1) AK47 | (2) AR-15 | (3) M1911\n\nChoice: "))
        except:
            continue
        else:
            if starterWeapon == 1:
                print("sql")
                break
            elif starterWeapon == 2:
                print("sql")
                break
            elif starterWeapon == 3:
                eq.execute("UPDATE users SET gun1 = 'M1911' WHERE user = ?;""", (username))
                eql.commit()
                break
            else:
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
    global username

    eq.execute(""" SELECT gun1 FROM users WHERE user = ?;""", (username))
    result = eq.fetchone()

    input(result)

    if result[0] == 'N/A':
        input("Universal Studios Production")
        input("Made by WolvTMG\n\n[Enter] to continue")

        input(f"Welcome to Rainfare, {username[0]}, choose your starter weapon")
        starterWeaponChoice()
    else:
        eq.execute(""" SELECT hp FROM users WHERE user = ?;""", (username))
        hp = eq.fetchone()

        input(f"Character Info:\n\nUsername: {username[0]}\nHP: {hp[0]}")
        main()




def newSave():
    eq.execute(""" SELECT user from users; """)
    result = eq.fetchall()
    x = 0
    for i in result:
        x = x + 1

    if x == 3:
        input("Too many saves!")
        startUp()
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
                eq.execute(""" INSERT INTO users (user, hp, cash, level, xp, gun1, gun2, gun3, gun4, potion1, potion2, potion3, potion4) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?); """, (username, 100, 0, 0, 0, "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"))
                eql.commit()
                intro()
                break
            elif confirmUsername == 2:
                newSave()
                break
            else:
                continue

def loadSave():
    global username
    eq.execute(""" SELECT user from users; """)
    result = eq.fetchall()
    x = 0

    for i in result:
        x = x + 1

    if x == 0:
        input("There are no saves!")
        startUp()
    else:
        while True:
            try:
                choice = int(input(f"{result}\n\n(1) Load Save 1 | (2) Load Save 2 | (3) Load Save 3 | (4) Go Back\n\nChoice: "))
            except:
                continue
            else:
                if choice == 1:
                    username = result[choice-1]
                    input(username)
                    break
                elif choice == 2 and x > 1:
                    username = result[choice-1]
                    input(username)
                    break
                elif choice == 2 and x < 2:
                    input("No data found")
                    continue
                elif choice == 3 and x > 2:
                    username = result[choice-1]
                    input(username)
                    break
                elif choice == 3 and x < 3:
                    input("No data found")
                else:
                    startUp()

        while True:
            try: 
                confirmChoice = int(input(f"Confirm choice: {username[0]} (1) Yes | (2) No\n\nChoice: "))
            except:
                continue
            else:
                if confirmChoice == 1:
                    intro()
                    break
                elif confirmChoice ==2:
                    loadSave()
                    break
                else:
                    continue

def deleteSave():
    input("| WARNING !!! | Entering dangeroust territory !!! | Proceed with caution |")


def startUp():
    while True:
        try:
            choice = int(input("(1) New Save | (2) Load Save | (3) Delete Save | (4) Exit\n\nChoice: "))
        except:
            continue
        else:
            if choice == 1:
                newSave()
                break
            elif choice == 2:
                loadSave()
                break
            elif choice ==3:
                deleteSave()
                break
            else:
                sys.exit()

startUp()
