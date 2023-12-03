import os
import sys
import time
import random
import sqlite3

global username

eql = sqlite3.connect('data.db')
eq = eql.cursor()


def clear():
    system = os.name
    if system == 'nt':
        clear()
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return

# [[Rifles], [SMG], [Snipers], [HandGuns]]
starterWeapons = [["AK-47", "AR-15"], ["M1911"]]

weaponsI = [["M16"], ["UZI"], ["G17"]]
weaponsII = [["Beretta M9"]]
weaponsIII = [["AUG-A3"], ["Barrett"]]

def main():

    def explore():

        eq.execute(""" SELECT gun1, gun2, gun3, gun4 FROM users WHERE user = ?; """, (username))
        result = eq.fetchall()
        x = 0
        print(result)
        for i in result:
            x = x + 1

        if x == 0:
            input("You have no guns!")
            menu()
        else:
            while True:
                try:
                    choice = int(input("Choose gun\n\nChoice: "))
                except:
                    clear()
                    continue
                else:
                    if choice == 1:
                        
                        print(result[0][0])
                        if result[0][0] != 'N/A':
                            
                            timex = random.randrange(5, 15)
                            print(timex)

                            for i in range(timex):
                                time.sleep(1)
                                clear()
                                print(f"Currently Exploring\n\nTime elapsed: {i}")

                            cash, xp = rewards(1)

                            eq.execute("SELECT cash FROM users WHERE user = ?;", (username))
                            eq.execute("SeLECT xp FROM users WHERE user = ?;", (username))

                            result = eq.fetchone()
                            result2 = eq.fetchone()

                            print(result[0])
                            print(result[0])

                            cashReward = result[0] + cash 
                            input(cashReward)

                            eq.execute("UPDATE users SET gun1 = 'M1911' WHERE user = ?;""", (username))

                            input(f"You have gained {cash} cash and {xp} xp")
                            break

    def rewards(x):
        if x == 1:
            cash = random.randrange(50, 80)
            xp = random.randrange(10, 20)

        return cash, xp
        

    def lootCrates():
        print("WIP")

    def menu():
        while True:
            try:
                choice = int(input("(1) Explore | (2) View Bag | (3) Loot Crates | (4) Leave\n\nChoice: "))
            except:
                clear()
                continue
            else:
                if choice == 1:
                    clear()
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
                    clear()
                    continue

    menu()
                     



def starterWeaponChoice():
    while True:
        try:
            starterWeapon = int(input("Choose your starter weapon\n\n(1) AK47 | (2) AR-15 | (3) M1911\n\nChoice: "))
        except:
            clear()
            continue
        else:
            if starterWeapon == 1:
                eq.execute("UPDATE users SET gun1 = 'AK-47' WHERE user = ?;""", (username))
                eql.commit()
                break
            elif starterWeapon == 2:
                eq.execute("UPDATE users SET gun1 = 'AR-15' WHERE user = ?;""", (username))
                eql.commit()
                break
            elif starterWeapon == 3:
                eq.execute("UPDATE users SET gun1 = 'M1911' WHERE user = ?;""", (username))
                eql.commit()
                break
            else:
                clear()
                continue

    while True:
        try:
            confirmWeapon = int(input(f"Is this the weapon you want? {starterWeapon}\n\n (1) Yes | (2) No\n\nChoice: "))
        except:
            clear()
            continue
        else:
            if confirmWeapon == 1:
                clear()
                intro()
                break
            elif confirmWeapon == 2:
                clear()
                starterWeaponChoice()
            else:
                clear()
                continue

def intro():
    global username

    eq.execute(""" SELECT gun1 FROM users WHERE user = ?;""", (username))
    result = eq.fetchone()

    if result[0] == 'N/A':
        input("Universal Studios Production")
        input("Made by WolvTMG\n\n[Enter] to continue")

        input(f"Welcome to Rainfare, {username[0]}, choose your starter weapon")
        clear()
        starterWeaponChoice()
    else:
        eq.execute(""" SELECT hp FROM users WHERE user = ?;""", (username))
        hp = eq.fetchone()

        input(f"Character Info:\n\nUsername: {username[0]}\nHP: {hp[0]}")
        clear()
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
            clear()
            continue

    input(f"Welcome, {username}")
    while True:
        try:
            confirmUsername = int(input(f"Would you like to keep this name?\n\n (1) Yes | (2) No\n\nChoice: "))
        except:
            clear()
            continue
        else:
            if confirmUsername == 1:
                eq.execute(""" INSERT INTO users (user, hp, cash, level, xp, gun1, gun2, gun3, gun4, potion1, potion2, potion3, potion4) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?); """, (username, 100, 0, 0, 0, "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"))
                eql.commit()
                clear()
                intro()
                break
            elif confirmUsername == 2:
                clear()
                newSave()
                break
            else:
                clear()
                continue

def loadSave():
    global username
    eq.execute(""" SELECT user from users; """)
    result = eq.fetchall()
    x = 0

    for i in result:
        x = x + 1

    if x == 0:
        clear()
        input("There are no saves!")
        startUp()
    else:
        while True:
            try:
                choice = int(input(f"{result}\n\n(1) Load Save 1 | (2) Load Save 2 | (3) Load Save 3 | (4) Go Back\n\nChoice: "))
            except:
                clear()
                continue
            else:
                if choice == 1:
                    clear()
                    username = result[choice-1]
                    break
                elif choice == 2 and x > 1:
                    clear()
                    username = result[choice-1]
                    break
                elif choice == 2 and x < 2:
                    clear()
                    input("No data found")
                    continue
                elif choice == 3 and x > 2:
                    clear()
                    username = result[choice-1]
                    break
                elif choice == 3 and x < 3:
                    clear()
                    input("No data found")
                else:
                    clear()
                    loadSave()

        while True:
            try: 
                confirmChoice = int(input(f"Confirm choice: {username[0]} (1) Yes | (2) No\n\nChoice: "))
            except:
                clear()
                continue
            else:
                if confirmChoice == 1:
                    clear()
                    intro()
                    break
                elif confirmChoice == 2:
                    clear()
                    loadSave()
                    break
                else:
                    clear()
                    continue

def deleteSave():
    input("| WARNING !!! | Entering dangeroust territory !!! | Proceed with caution |")


def startUp():
    while True:
        try:
            choice = int(input("(1) New Save | (2) Load Save | (3) Delete Save | (4) Exit\n\nChoice: "))
        except:
            clear()
            continue
        else:
            if choice == 1:
                clear()
                newSave()
                break
            elif choice == 2:
                clear()
                loadSave()
                break
            elif choice == 3:
                clear()
                deleteSave()
                break
            elif choice == 4:
                sys.exit()
            else:
                clear()
                continue

startUp()
