import os
import sys
import time
import random
import sqlite3

global username

eql = sqlite3.connect('data.db')
eq = eql.cursor()

eq.execute('''CREATE TABLE IF NOT EXISTS users (
    user text,
    hp int,
    cash int,
    level int, 
    xp int,
    gun1 text,
    gun2 text,
    gun3 text,
    gun4 text,
    potion1 text,
    potion2 text,
    potion3 text,
    potion4 text,
    key1 int,
    key2 int,
    key3 int,
    key4 int,
    r_ammo int,
    s_ammo int,
    p_ammo int
)''')

def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return

# [[Rifles], [SMG], [Snipers], [HandGuns]]
starterWeapons = [["AK-47", "AR-15"], ["M1911"]]

weaponsI = [["M16"], ["UZI"], ["G17"]]
weaponsII = [["Beretta M9"]]
weaponsIII = [["AUG-A3"], ["Barrett .50"]]

def main():

    def explore():

        global username

        eq.execute(""" SELECT gun1, gun2, gun3, gun4 FROM users WHERE user = ?; """, (username,))
        result = eq.fetchall()
        x = 0

        for i in result:
            x = x + 1

        if x == 0:
            input("You have no guns!")
            menu()
        else:
            print(result)
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

                            for i in range(timex):
                                time.sleep(1)
                                clear()
                                print(f"Currently Exploring\n\nTime elapsed: {i}")

                            cash, xp = rewards(1)

                            eq.execute("SELECT cash FROM users WHERE user = ?;", (username,))
                            result_cash = eq.fetchone()

                            eq.execute("SELECT xp FROM users WHERE user = ?;", (username,))
                            result_xp = eq.fetchone()

                            
                            cashReward = result_cash[0] + cash 
                            xpReward = result_xp[0] + xp

                            eq.execute("UPDATE users SET cash = ?, xp = ? WHERE user = ?;", (cashReward, xpReward, username))
                            eql.commit()

                            input(f"You have gained {cash} cash and {xp} xp")

                            menu()
                            
    def arcs():
        print("WIP") 

    def rewards(x):
        if x == 1:
            cash = random.randrange(50, 80)
            xp = random.randrange(10, 20)

        return cash, xp
        

    def lootCrates():
        eq.execute(""" SELECT cash, key1, key2, key3, key4 FROM users WHERE user = ?;""", (username,))
        result = eq.fetchone()

        clear()

        cash = result[0]
        lootCrate1 = result[1]
        lootCrate2 = result[2]
        lootCrate3 = result[3]
        lootCrate4 = result[4]

        print(cash)
        print(lootCrate1)

        while True:
            try:
                shop = int(input("Welcome to the Loot Crate shop! | (1) Browse | (2) Leave\n\nChoice: "))
            except:
                continue
            else:
                if shop == 1:
                    break
                elif shop == 2:
                    menu()
                    break
                else:
                    continue

        while True:
            clear()
            try:
                catalog = int(input("(1) 50$ Loot Crate | (2) 100$ Loot Crate | (3) 500$ Loot Crate | (4) 1,200$ Loot Crate | (5) Exit\n\nChoice: "))
            except:
                continue
            else:
                if catalog == 1 and cash > 49:
                    cash = cash - 50
    
                elif catalog == 2 and cash > 99:
                    cash = cash - 100
                elif catalog == 3 and cash > 499:
                    cash = cash - 500
                elif catalog == 4 and cash > 1199:
                    cash = cash - 1200
                elif catalog == 5:
                    lootCrates()
                else:
                    print("Pooron")

    def bag():
        eq.execute(""" SELECT hp, xp, cash, gun1, gun2, gun3, gun4, key1, key2, key3, key4 FROM users WHERE user = ?;""", (username,))
        result = eq.fetchone()
        clear()
        print(f"Bag\n\nWeapon 1: {result[3]}\nWeapon 2: {result[4]}\nWeapon 3: {result[5]}\nWeapon 4: {result[6]}\nLoot Crate 1: {result[7]}")


    def menu():
        eq.execute(""" SELECT hp, xp, cash FROM users WHERE user = ?;""", (username,))
        hp = eq.fetchone()
        clear()
        while True:
            try:
                choice = int(input(f"Character Info | Username: {username} | HP: {hp[0]} | XP: {hp[1]} | Cash: {hp[2]}\n\n(1) Explore | (2) View Bag | (3) Loot Crates | (4) Leave\n\nChoice: "))
            except:
                clear()
                continue
            else:
                if choice == 1:
                    clear()
                    explore()
                    break
                elif choice == 2:
                    bag()
                elif choice == 3:
                    lootCrates()
                elif choice == 4:
                    sys.exit()
                else:
                    clear()
                    continue

    def levelChecker():
        eq.execute(" SELECT xp FROM users WHERE user = ?;", (username,))
        xp = eq.fetchone()

        for i in range(xp[0]):
            if xp[0] < 99:
                continue
            else:
                print(i)

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
                eq.execute("UPDATE users SET gun1 = 'AK-47' WHERE user = ?;""", (username,))
                eql.commit()
                break
            elif starterWeapon == 2:
                eq.execute("UPDATE users SET gun1 = 'AR-15' WHERE user = ?;""", (username,))
                eql.commit()
                break
            elif starterWeapon == 3:
                eq.execute("UPDATE users SET gun1 = 'M1911' WHERE user = ?;""", (username,))
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
    eq.execute(""" SELECT gun1 FROM users WHERE user = ?;""", (username,))
    result = eq.fetchone()

    if result[0] == 'N/A':
        input("Universal Studios Production")
        input("Made by WolvTMG\n\n[Enter] to continue")

        input(f"Welcome to Rainfare, {username}, choose your starter weapon")
        clear()
        starterWeaponChoice()
    else:
        eq.execute(""" SELECT hp FROM users WHERE user = ?;""", (username,))
        hp = eq.fetchone()

        clear()
        main()

def newSave():
    global username
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
    username = username[0]

    while True:
        try:
            confirmUsername = int(input(f"Would you like to keep this name?\n\n (1) Yes | (2) No\n\nChoice: "))
        except:
            clear()
            continue
        else:
            if confirmUsername == 1:
                eq.execute(""" INSERT INTO users (user, hp, cash, level, xp, gun1, gun2, gun3, gun4, potion1, potion2, potion3, potion4, key1, key2, key3, key4, r_ammo, s_ammo, p_ammo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?); """, (username, 100, 0, 0, 0, "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", 0, 0, 0, 0, 0, 0 ,0))
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
                    startUp()

        while True:
            try: 
                confirmChoice = int(input(f"Confirm choice: {username[0]} (1) Yes | (2) No\n\nChoice: "))
            except:
                clear()
                continue
            else:
                if confirmChoice == 1:
                    input(username)
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
                choice = int(input(f"{result}\n\n(1) Delete Save 1 | (2) Delete Save 2 | (3) Delete Save 3 | (4) Go Back\n\nChoice: "))
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
                    startUp()

        while True:
            try: 
                confirmChoice = int(input(f"Confirm choice: {username[0]} (1) Yes | (2) No\n\nChoice: "))
            except:
                clear()
                continue
            else:
                if confirmChoice == 1:
                    clear()
                    eq.execute("""DELETE FROM users WHERE user = ?;""", (username))
                    eql.commit()
                    startUp()
                    break
                elif confirmChoice == 2:
                    clear()
                    deleteSave()
                    break
                else:
                    clear()
                    continue


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
