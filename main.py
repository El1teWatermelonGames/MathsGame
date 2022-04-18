from colorama import init, Fore, Style, Back
import linecache
import random

init()
version = str("V1.1.2")
config = str('config.txt')


def menu():
    print("type " + Back.LIGHTYELLOW_EX + Fore.BLACK + "exit" + Style.RESET_ALL + " to exit to menu during a question")
    print(Fore.GREEN + "Addition, " + Fore.RED + "Subtraction, " + Fore.YELLOW + "Multiplication, " + Fore.BLUE + "Division" + Style.RESET_ALL)
    print("Answer with " + Fore.GREEN + "a" + Style.RESET_ALL + "/" + Fore.RED + "s" + Style.RESET_ALL + "/" + Fore.YELLOW + "m" + Style.RESET_ALL + "/" + Fore.BLUE + "d" + Style.RESET_ALL)
    menu_selection = str(input())
    menu_selection.lower()
    if menu_selection == "a":
        print(Fore.GREEN + "Addition" + Style.RESET_ALL)
        add_menu()
    elif menu_selection == "s":
        print(Fore.RED + "Subtraction" + Style.RESET_ALL)
        sub_menu()
    elif menu_selection == "m":
        print(Fore.YELLOW + "Multiplication" + Style.RESET_ALL)
        tim_menu()
    elif menu_selection == "d":
        print(Fore.BLUE + "Division" + Style.RESET_ALL)
        div_menu()
    else:
        menu()


def add_menu():
    print(Fore.GREEN + "Easy, " + Fore.YELLOW + "Medium, " + Fore.RED + "Hard" + Style.RESET_ALL)
    print("Answer with " + Fore.GREEN + "e" + Style.RESET_ALL + "/" + Fore.YELLOW + "m" + Style.RESET_ALL + "/" + Fore.RED + "h" + Style.RESET_ALL)
    menu_selection = str(input())
    if menu_selection == "e":
        addE()
    elif menu_selection == "m":
        addM()
    elif menu_selection == "h":
        addH()
    elif menu_selection == "exit":
        menu()
    else:
        add_menu()


def addE():
    global addMinE
    global addMaxE
    i1 = int(random.randint(addMinE, addMaxE))
    i2 = int(random.randint(addMinE, addMaxE))
    cans = i1 + i2
    tp1 = str(i1)
    tp2 = str(i2)
    print(tp1 + " + " + tp2 + " =")
    pans = str(input())
    if pans == "exit":
        menu()
    else:
        pansi = int(pans)
        if pansi == cans:
            print(Fore.GREEN + "Correct" + Style.RESET_ALL)
            addE()
        else:
            can = str(cans)
            print(Fore.RED + "Incorrect")
            print("The answer was " + can + Style.RESET_ALL)
            addE()


def addM():
    global addMinM
    global addMaxM
    i1 = int(random.randint(addMinM, addMaxM))
    i2 = int(random.randint(addMinM, addMaxM))
    cans = i1 + i2
    tp1 = str(i1)
    tp2 = str(i2)
    print(tp1 + " + " + tp2 + " =")
    pans = str(input())
    if pans == "exit":
        menu()
    else:
        pansi = int(pans)
        if pansi == cans:
            print(Fore.GREEN + "Correct" + Style.RESET_ALL)
            addM()
        else:
            can = str(cans)
            print(Fore.RED + "Incorrect")
            print("The answer was " + can + Style.RESET_ALL)
            addM()


def addH():
    global addMinH
    global addMaxH
    i1 = int(random.randint(addMinH, addMaxH))
    i2 = int(random.randint(addMinH, addMaxH))
    cans = i1 + i2
    tp1 = str(i1)
    tp2 = str(i2)
    print(tp1 + " + " + tp2 + " =")
    pans = str(input())
    if pans == "exit":
        menu()
    else:
        pansi = int(pans)
        if pansi == cans:
            print(Fore.GREEN + "Correct" + Style.RESET_ALL)
            addH()
        else:
            can = str(cans)
            print(Fore.RED + "Incorrect")
            print("The answer was " + can + Style.RESET_ALL)
            addH()


def sub_menu():
    print(Fore.GREEN + "Easy, " + Fore.YELLOW + "Medium, " + Fore.RED + "Hard" + Style.RESET_ALL)
    print("Answer with " + Fore.GREEN + "e" + Style.RESET_ALL + "/" + Fore.YELLOW + "m" + Style.RESET_ALL + "/" + Fore.RED + "h" + Style.RESET_ALL)
    menu_selection = str(input())
    if menu_selection == "e":
        subE()
    elif menu_selection == "m":
        subM()
    elif menu_selection == "h":
        subH()
    elif menu_selection == "exit":
        menu()
    else:
        sub_menu()


def subE():
    global subMinE
    global subMaxE
    global subNegTF
    i1 = int(random.randint(subMinE, subMaxE))
    i2 = int(random.randint(subMinE, subMaxE))
    cans = i1 - i2
    if subNegTF == 0:
        if cans < 0:
            subE()
    tp1 = str(i1)
    tp2 = str(i2)
    print(tp1 + " - " + tp2 + " =")
    pans = str(input())
    if pans == "exit":
        menu()
    else:
        pansi = int(pans)
        if pansi == cans:
            print(Fore.GREEN + "Correct" + Style.RESET_ALL)
            subE()
        else:
            can = str(cans)
            print(Fore.RED + "Incorrect")
            print("The answer was " + can + Style.RESET_ALL)
            subE()


def subM():
    global subMinM
    global subMaxM
    global subNegTF
    i1 = int(random.randint(subMinM, subMaxM))
    i2 = int(random.randint(subMinM, subMaxM))
    cans = i1 - i2
    if subNegTF == 0:
        if cans < 0:
            subM()
    tp1 = str(i1)
    tp2 = str(i2)
    print(tp1 + " - " + tp2 + " =")
    pans = str(input())
    if pans == "exit":
        menu()
    else:
        pansi = int(pans)
        if pansi == cans:
            print(Fore.GREEN + "Correct" + Style.RESET_ALL)
            subM()
        else:
            can = str(cans)
            print(Fore.RED + "Incorrect")
            print("The answer was " + can + Style.RESET_ALL)
            subM()


def subH():
    global subMinH
    global subMaxH
    global subNegTF
    i1 = int(random.randint(subMinH, subMaxH))
    i2 = int(random.randint(subMinH, subMaxH))
    cans = i1 - i2
    if subNegTF == 0:
        if cans < 0:
            subH()
    tp1 = str(i1)
    tp2 = str(i2)
    print(tp1 + " - " + tp2 + " =")
    pans = str(input())
    if pans == "exit":
        menu()
    else:
        pansi = int(pans)
        if pansi == cans:
            print(Fore.GREEN + "Correct" + Style.RESET_ALL)
            subH()
        else:
            can = str(cans)
            print(Fore.RED + "Incorrect")
            print("The answer was " + can + Style.RESET_ALL)
            subH()


def tim_menu():
    print(Fore.GREEN + "Easy, " + Fore.YELLOW + "Medium, " + Fore.RED + "Hard" + Style.RESET_ALL)
    print("Answer with " + Fore.GREEN + "e" + Style.RESET_ALL + "/" + Fore.YELLOW + "m" + Style.RESET_ALL + "/" + Fore.RED + "h" + Style.RESET_ALL)
    menu_selection = str(input())
    if menu_selection == "e":
        timE()
    elif menu_selection == "m":
        timM()
    elif menu_selection == "h":
        timH()
    elif menu_selection == "exit":
        menu()
    else:
        tim_menu()


def timE():
    global timMinE
    global timMaxE
    i1 = int(random.randint(timMinE, timMaxE))
    i2 = int(random.randint(timMinE, timMaxE))
    cans = i1 * i2
    tp1 = str(i1)
    tp2 = str(i2)
    print(tp1 + " * " + tp2 + " =")
    pans = str(input())
    if pans == "exit":
        menu()
    else:
        pansi = int(pans)
        if pansi == cans:
            print(Fore.GREEN + "Correct" + Style.RESET_ALL)
            timE()
        else:
            can = str(cans)
            print(Fore.RED + "Incorrect")
            print("The answer was " + can + Style.RESET_ALL)
            timE()


def timM():
    global timMinM
    global timMaxM
    i1 = int(random.randint(timMinM, timMaxM))
    i2 = int(random.randint(timMinM, timMaxM))
    cans = i1 * i2
    tp1 = str(i1)
    tp2 = str(i2)
    print(tp1 + " * " + tp2 + " =")
    pans = str(input())
    if pans == "exit":
        menu()
    else:
        pansi = int(pans)
        if pansi == cans:
            print(Fore.GREEN + "Correct" + Style.RESET_ALL)
            timM()
        else:
            can = str(cans)
            print(Fore.RED + "Incorrect")
            print("The answer was " + can + Style.RESET_ALL)
            timM()


def timH():
    global timMinH
    global timMaxH
    i1 = int(random.randint(timMinH, timMaxH))
    i2 = int(random.randint(timMinH, timMaxH))
    cans = i1 * i2
    tp1 = str(i1)
    tp2 = str(i2)
    print(tp1 + " * " + tp2 + " =")
    pans = str(input())
    if pans == "exit":
        menu()
    else:
        pansi = int(pans)
        if pansi == cans:
            print(Fore.GREEN + "Correct" + Style.RESET_ALL)
            timH()
        else:
            can = str(cans)
            print(Fore.RED + "Incorrect")
            print("The answer was " + can + Style.RESET_ALL)
            timH()


def div_menu():
    print(Fore.GREEN + "Easy, " + Fore.YELLOW + "Medium, " + Fore.RED + "Hard" + Style.RESET_ALL)
    print("Answer with " + Fore.GREEN + "e" + Style.RESET_ALL + "/" + Fore.YELLOW + "m" + Style.RESET_ALL + "/" + Fore.RED + "h" + Style.RESET_ALL)
    menu_selection = str(input())
    if menu_selection == "e":
        divE()
    elif menu_selection == "m":
        divM()
    elif menu_selection == "h":
        divH()
    elif menu_selection == "exit":
        menu()
    else:
        div_menu()


def divE():
    global divMinE
    global divMaxE
    global divFracTF
    i1 = random.randint(divMinE, divMaxE)
    i2 = random.randint(divMinE, divMaxE)
    if divFracTF == 0:
        i1m = i2 * random.randint(divMinE, divMaxE)
        if i1m > divi1maxE:
            divE()
        i1 = i1m
    if i1 == 0:
        divE()
    if i2 == 0:
        divE()
    cans = i1 / i2
    if divFracTF == 0:
        if i1 < i2:
            divE()
    tp1 = str(i1)
    tp2 = str(i2)
    print(tp1 + " / " + tp2 + " =")
    pans = str(input())
    if pans == "exit":
        menu()
    else:
        pansf = float(pans)
        if pansf == cans:
            print(Fore.GREEN + "Correct" + Style.RESET_ALL)
            divE()
        else:
            can = str(cans)
            print(Fore.RED + "Incorrect")
            print("The answer was " + can + Style.RESET_ALL)
            divE()


def divM():
    global divMinM
    global divMaxM
    global divFracTF
    i1 = random.randint(divMinM, divMaxM)
    i2 = random.randint(divMinM, divMaxM)
    if divFracTF == 0:
        i1m = i2 * random.randint(divMinM, divMaxM)
        if i1m > divi1maxM:
            divM()
        i1 = i1m
    if i1 == 0:
        divM()
    if i2 == 0:
        divM()
    cans = i1 / i2
    if divFracTF == 0:
        if i1 < i2:
            divM()
    tp1 = str(i1)
    tp2 = str(i2)
    print(tp1 + " / " + tp2 + " =")
    pans = str(input())
    if pans == "exit":
        menu()
    else:
        pansf = float(pans)
        if pansf == cans:
            print(Fore.GREEN + "Correct" + Style.RESET_ALL)
            divE()
        else:
            can = str(cans)
            print(Fore.RED + "Incorrect")
            print("The answer was " + can + Style.RESET_ALL)
            divE()


def divH():
    global divMinH
    global divMaxH
    global divFracTF
    i1 = random.randint(divMinH, divMaxH)
    i2 = random.randint(divMinH, divMaxH)
    if divFracTF == 0:
        i1m = i2 * random.randint(divMinH, divMaxH)
        if i1m > divi1maxH:
            divH()
        i1 = i1m
    if i1 == 0:
        divH()
    if i2 == 0:
        divH()
    cans = i1 / i2
    if divFracTF == 0:
        if i1 < i2:
            divH()
    tp1 = str(i1)
    tp2 = str(i2)
    print(tp1 + " / " + tp2 + " =")
    pans = str(input())
    if pans == "exit":
        menu()
    else:
        pansf = float(pans)
        if pansf == cans:
            print(Fore.GREEN + "Correct" + Style.RESET_ALL)
            divH()
        else:
            can = str(cans)
            print(Fore.RED + "Incorrect")
            print("The answer was " + can + Style.RESET_ALL)
            divH()


global addMinE
global addMaxE
global addMinM
global addMaxM
global addMinH
global addMaxH

global subMinE
global subMaxE
global subMinM
global subMaxM
global subMinH
global subMaxH

global timMinE
global timMaxE
global timMinM
global timMaxM
global timMinH
global timMaxH

global divMinE
global divMaxE
global divMinM
global divMaxM
global divMinH
global divMaxH

global subNegTF
global divFracTF

global divi1maxE
global divi1maxM
global divi1maxH

addMinE = int(linecache.getline(config, 4))
addMaxE = int(linecache.getline(config, 5))
addMinM = int(linecache.getline(config, 7))
addMaxM = int(linecache.getline(config, 8))
addMinH = int(linecache.getline(config, 10))
addMaxH = int(linecache.getline(config, 11))

subMinE = int(linecache.getline(config, 15))
subMaxE = int(linecache.getline(config, 16))
subMinM = int(linecache.getline(config, 18))
subMaxM = int(linecache.getline(config, 19))
subMinH = int(linecache.getline(config, 21))
subMaxH = int(linecache.getline(config, 22))

timMinE = int(linecache.getline(config, 26))
timMaxE = int(linecache.getline(config, 27))
timMinM = int(linecache.getline(config, 29))
timMaxM = int(linecache.getline(config, 30))
timMinH = int(linecache.getline(config, 32))
timMaxH = int(linecache.getline(config, 33))

divMinE = int(linecache.getline(config, 37))
divMaxE = int(linecache.getline(config, 38))
divMinM = int(linecache.getline(config, 40))
divMaxM = int(linecache.getline(config, 41))
divMinH = int(linecache.getline(config, 43))
divMaxH = int(linecache.getline(config, 44))

subNegTF = int(linecache.getline(config, 46))
divFracTF = int(linecache.getline(config, 49))

divi1maxE = int(linecache.getline(config, 52))
divi1maxM = int(linecache.getline(config, 54))
divi1maxH = int(linecache.getline(config, 56))

print(Fore.YELLOW + version + Style.RESET_ALL)
menu()
