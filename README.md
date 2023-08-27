# Trabalho 1

Objetivo: Crie um programa cliente servidor que envia três questões em sequência de múltipla escolha para um cliente após este se conectar, o cliente deve responder às questões e o servidor retornar com quantas questões acertou, mostrando em uma lista o acerto/erro de cada.  Criar um banco de dados para as questões no servidor. Utilizar uma parte da aplicação sendo dockerizada.   Exemplo de questão:

Qual é a capital da Itália? 
1. Roma; 
2. Paris; 
3. Lisboa; 
4. Londres 

Será usado um banco de dados do postgrest dentro de um container, do docker-compose.
---
### Meu ambiente:
Foi utilizado a IDE VSCode (OBS: Pode usar qualquer IDE).

E a biblioteca psycopg2, para fazer a conexão entre o python e o Postgres.

- Para a instalação, execute o seguinte comando:
 `pip install psycopg2-binary`

---

## Para executar o código:

No diretório raiz, executar o docker-compose, para criar um banco de dados (Postgresql):
```
docker-compose up –build
```

Depois executar o server.py:
```
python3 app/server.py
```

Por fim executar o client.py:
```
python3 app/client.py
```
