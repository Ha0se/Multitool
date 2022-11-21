from multiprocessing import Process
from netmiko import ConnectHandler
import concurrent.futures
import time

#zapisuje hasło z pliku by nie trzeba było recznie wpisywać
temppass = open('password.txt', 'r')
password = temppass.read()
temppass.close()

#utworzenie listy hostów
hostRange = []
#dodawanie hostów do listy hostów
with open('Stations.txt', 'r') as hosts:
    for line in hosts:
        hostname = line.strip()
        host = {'device_type': 'linux',
            'host': hostname,
            'username': 'login',
            'password': password}
        hostRange.append(host)

starting_time = time.perf_counter()

#funkcja na łączenie z hostem
def open_connection(host):
    try:
        connection = ConnectHandler(**host)
        print('Trying station: ', host['host'])
        print('Connection Established to Host:', host['host'])
        sendcommand = connection.send_command('script.sh')
        return sendcommand
    except:
        print('Connection Failed to host', host['host'])
        
#żależnie od ilości rdzeni, tyle połączeń jednoscześnie zostanie otwartych i wykolnanych komend na hostach
if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(open_connection, hostRange)
        for result in results:
            print(result)

finish = time.perf_counter()
print('Time Elapsed:', finish - starting_time)
