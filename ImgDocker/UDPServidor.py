# Servidor UDP: recibe una frase y la devuelve en mayúsculas (Kurose 2.7.1)
from socket import *

serverPort = 15000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('Servidor UDP escuchando en el puerto', serverPort)

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print('Datagrama desde', clientAddress)  # IP y puerto origen que ve el servidor
    serverSocket.sendto(message.decode().upper().encode(), clientAddress)
