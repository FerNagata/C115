from socket import *
import time
mensagem = " conceitos e tecnologias para dispositivos conectados "

serverName = 'localhost'
serverPort = 12005
clientSocket = socket( AF_INET , SOCK_STREAM )
clientSocket.connect(( serverName , serverPort))

def sendToServer(mensagem: str):
    clientSocket.sendall(mensagem.encode())
    time.sleep(1)  # Aguarda um segundo entre mensagens
    resp = clientSocket.recv(1024).decode()
    return resp
    
def closeConection():
    mensagem = 'break'
    clientSocket.sendall(mensagem.encode())
    time.sleep(2)  # Aguarda um segundo entre mensagens
    clientSocket.close()
    

