
print("Witaj w Multitool`u, co potrzebujesz? ")

while True:
    opcja = input("1 - CheckUser \n2 - MultiSSHConnect \n3 - MacAddress changer \n4 - IP reverser \n5 - Koniec\n:")
    #Opcja 1 sprawdza stan konta użytkownika w domenie
    if opcja == "1":
        from checkUser import cmdCommand
        cmdCommand.checkUser()
    #Opcja 2 wykonuje komendy, jedna po drugiej, host po hoscie
    elif opcja == "2":
        
        temphosts = open('sshCommands/hosts.txt', 'r')
        hosts = temphosts.read().split()
        temphosts.close()

        tempcommands = open('sshCommands/commands.txt', 'r')
        commands = tempcommands.read().split(";")
        tempcommands.close()

        print(hosts)
        print(commands)

        ready = input("Czy hosty i komendy sie zgadzaja? 0 - nie, 1 - tak: ")

        if ready == "1":
            from sshCommands import sshCommandExecute
            sshCommandExecute.doRoboty()
        else:
            pass
    #Opcja 3 zmienia format macaddresu na inny
    elif opcja == "3":
        from macAddress import changer
        changer.changer()
    #Opcja 4 odwraca kolejność adresu IP
    elif opcja == "4":
        from reverseIP import reverseIP
        reverseIP.reverseIP()

    elif opcja == "5":
        break

# do dodania 6 opcja - multiSSH, obecnie działa tylko uruchamiając plik bezpośrednio.