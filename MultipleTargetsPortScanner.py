import socket
from IPy import IP

# Converte o Domain Name no Endereco Ip dos alvos
def getIp(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return  socket.gethostbyname(ip)

def scan(target):
    convertedIp = getIp(target)
    print('\n' + '[-_0 Scanning Target] ' + str(target))
    for port in range(1,100):
        scanPort(convertedIp, port)

# Identifica o service que está executando na porta aberta.
def getBanner(sock):
    return sock.recv(1024)
# Realiza a tentativa de conexao com a porta do alvo
def scanPort(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.05)
        sock.connect((ipaddress, port))
        try:
            bannerService = getBanner(sock)
            print('[+] Open port' + str(port) + ' : ' + str(bannerService.decode().strip('\n')))
        except:
            print('[+] Open port ' + str(port))
    except:
        pass

# Recebe um ou mais alvos
targets = input('[+] Digite os alvos que quer escanear (Se for mais de um, separe por ","): ')
if ',' in targets:
    for ipAdd in targets.split(','):
        scan(ipAdd.strip(' '))
else:
    scan(targets)
