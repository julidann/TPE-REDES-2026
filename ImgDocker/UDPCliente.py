# Cliente UDP (Kurose 2.7.1). Uso: python3 UDPCliente.py <IP_destino> [puerto]
import sys
from socket import *

serverName = sys.argv[1]
serverPort = int(sys.argv[2]) if len(sys.argv) > 2 else 15000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(5)                          # UDP no avisa si se pierde: esperamos 5 s
message = input('Escriba una frase en minúsculas: ')
clientSocket.sendto(message.encode(), (serverName, serverPort))
print('Socket local:', clientSocket.getsockname())  # puerto efímero elegido por el SO
try:
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print('Respuesta de', serverAddress, ':', modifiedMessage.decode())
except timeout:
    print('Sin respuesta del servidor después de 5 segundos')
clientSocket.close()
