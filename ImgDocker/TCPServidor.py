# Servidor TCP: recibe una frase y la devuelve en mayúsculas (Kurose 2.7.2)
from socket import *

serverPort = 15000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Servidor TCP escuchando en el puerto', serverPort)

while True:
    connectionSocket, addr = serverSocket.accept()
    print('Conexión desde', addr)          # IP y puerto origen que ve el servidor
    sentence = connectionSocket.recv(1024).decode()
    connectionSocket.send(sentence.upper().encode())
    connectionSocket.close()
