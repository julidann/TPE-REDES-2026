# Cliente TCP (Kurose 2.7.2). Uso: python3 TCPCliente.py <IP_destino> [puerto]
import sys
from socket import *

serverName = sys.argv[1]
serverPort = int(sys.argv[2]) if len(sys.argv) > 2 else 15000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print('Socket local:', clientSocket.getsockname())  # puerto efímero elegido por el SO
sentence = input('Escriba una frase en minúsculas: ')
clientSocket.send(sentence.encode())
print('Respuesta del servidor:', clientSocket.recv(1024).decode())
clientSocket.close()
