import os

def checkUser():
    wait = "1"
    while True:
        if wait == "1":
            login = input("Podaj login osoby: ")
            #os.system start cmd otwiera cmd i wykonuje komende
            os.system(f'start cmd /k "net user {login} /domain"')
            wait = input("Czy chcesz sprawdzić kogoś jeszcze? 0 - nie, 1 - tak: ")
        elif wait == "0":
            break
