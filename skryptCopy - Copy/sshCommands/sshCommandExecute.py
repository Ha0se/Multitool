from netmiko import ConnectHandler
import os
#Pobieranie danych do logowania
templogin = open('sshCommands/login.txt', 'r')
login = templogin.read()
templogin.close()

temppass = open('sshCommands/password.txt', 'r')
password = temppass.read()
temppass.close()

temphosts = open('sshCommands/hosts.txt', 'r')
hosts = temphosts.read().split()
temphosts.close()

tempcommands = open('sshCommands/commands.txt', 'r')
commands = tempcommands.read().split(";")
tempcommands.close()
#łaczenie z hostem i wydawanie komend zapisanych w commands.txt
def doRoboty():

    for host in hosts:
        device = {"device_type":"ubiquiti_edge", "host":host, "username":login, "password":password, "secret":password}

        connect = ConnectHandler(**device)
        connect.enable()

        for command in commands:
            output = connect.send_command(command)
            print(host)
            print(output)
            #zapisywanie outputu z urządzeń do pliku textowego
            f = open("sshCommands/output.txt", "a")
            f.write(host+"\n")
            f.close()

            f = open("sshCommands/output.txt", "a")
            f.write(output+"\n")
            f.close()
            
print("You can find output in sshCommands/output.txt")




