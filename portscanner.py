import socket
from IPy import IP

# Recebe o Domain Name e retorna o endereco IP
def getIP(ip):
    try:
        IP(ip) # Se receber o Endereco Ip, simplesmente o retorna
        return ip
    except ValueError:
        return socket.gethostbyname(ip)

# Testa a conexao com a porta e retorna se esta aberta ou fechada
def scanPort(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5) # Chama a funcao depois de 0.5 millisegundos
        sock.connect((ipaddress, port))
        print('[+] Port' + str(port) + ' is open.')
    except:
        print('[-] Port' + str(port) + ' is closed.')

# Recebe o Domain Name ou Endereco IP
ipaddress = input('[+] Digite o alvo que quer escanear: ')
# Converte o Domain Name no respectivo endereco IP
convertedIp = getIP(ipaddress)

# Scanneia as portas dentro do intervalo determinado
for port in range(70,95):
    scanPort(convertedIp, port)
