from socket import *
from database import *
import json

serverPort = 12005
serverSocket = socket(AF_INET , SOCK_STREAM)
# atribui a porta ao socket criado
serverSocket.bind(('localhost', serverPort ))
# aceita conexoes
#com no maximo um cliente na fila
serverSocket.listen(1000)
print ('The server is ready to receive ')
# while True :
connectionSocket , addr = serverSocket.accept()
print(f"Conexão de: {addr}")

while True:
    # Recebe dados do cliente
    dados = connectionSocket.recv(1024).decode()
    print(f"Recebido do cliente: {dados}")

    if (dados == 'break'):
        print("Conexão fechada pelo cliente.")
        break
    else:
        dados = json.loads(dados) # string -> json
        if 'id' in dados:
            id = dados['id']
            respDB = selectQuestions(id)
        elif 'nome' in dados:
            nome = dados['nome']
            score = dados['score']
            insertScores(nome, score)
            respDB = '{"flag": Inserido!}'
        else:
            respDB = selectScores()
            respDB = str(respDB)

        connectionSocket.sendall(respDB.encode())
        print(f"Enviado para o cliente: {respDB}")

# Fecha a conexão
connectionSocket.close()
print("Conexão fechada.")
