from database import *
from client import *
import json
import ast

print("--------------------------------------------")
print("          QUESTIONÁRIO DE C115")
print("--------------------------------------------")

flag = True
while flag:
    print("------------------- MENU -------------------")
    print("1 - JOGAR")
    print("2 - SCORE")
    print("3 - SAIR")

    print("--------------------------------------------")
    op = int(input("Opção: "))
    print("--------------------------------------------")

    if op == 1:
        nome = input("Digite seu nome: ")
        score = 0
        for i in range(1,4):
            id = {'id': i}
            id = json.dumps(id)
            resposta = sendToServer(id)
            resposta = json.loads(resposta)
            option = (resposta['option1'], resposta['option2'], resposta['option3'], resposta['option4'])
            for index, op in enumerate(option):
                print(f'{index+1} - {op}')

            resp = int(input("Resposta: "))
            
            print('----------------------------------')
            if resp == resposta['answer']:
                score += 1
                print('Você acertou!')
            else:
                print('Você errou!')
            print('----------------------------------')

        dadosScore = {'nome': nome, 'score': score}
        dadosScore = json.dumps(dadosScore)
        flag = sendToServer(dadosScore)
        
    elif op == 2:
        print("--------------- PLACAR GERAL ---------------")
        
        placar = {'ver': 'placar'}
        placar = json.dumps(placar)
        resposta = sendToServer(placar)
        resposta = ast.literal_eval(resposta)

        for nome, score in resposta:
            print(f'{nome} - {score}')
    elif op == 3:
        print("Você saiu do jogo! Até mais")
        closeConection()
        flag = False
    else:
        print("Opção não encontrada, tente novamente.")

