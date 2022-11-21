def drukuj (zmienna1, zmienna2):
    print()
    print(f"Normal: {zmienna1}")
    print(f"Reverse: {zmienna2}")
    print()
#odwrócenie listy
def reverseIP():
    normalIP = input("podaj adres IP\n: ")
    tempList = normalIP.split(".")
    tempList.reverse()
    changed = '.'.join(tempList)
    drukuj(normalIP, changed)
