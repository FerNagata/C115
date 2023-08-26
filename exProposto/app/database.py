import psycopg2
import json

def selectQuestions(number):
    con = psycopg2.connect(host='localhost', port= 5432, database="trabalho1", user="postgres", password="postgres")
    cur = con.cursor()

    sql = "SELECT * FROM questions WHERE id = %s"
    cur.execute(sql, (number,))
    response = cur.fetchone()

    question = response[1]
    option1 = response[2]
    option2 = response[3]
    option3 = response[4]
    option4 = response[5]
    answer = response[6]

    arq_json = {
        'question': question,
        'option1': option1,
        'option2': option2,
        'option3': option3,
        'option4': option4,
        'answer': answer
    }

    arq_json = json.dumps(arq_json)

    cur.close()
    con.close()

    return arq_json

def selectScores():
    con = psycopg2.connect(host='localhost', port= 5432, database="trabalho1", user="postgres", password="postgres")
    cur = con.cursor()

    sql = "SELECT nome, score FROM scores"
    cur.execute(sql)
    response = cur.fetchall()
    print(response)
    
    cur.close()
    con.close()

    return response

def insertScores(name, score):
    con = psycopg2.connect(host='localhost', port= 5432, database="trabalho1", user="postgres", password="postgres")
    cur = con.cursor()

    sql = "INSERT INTO scores (nome, score) VALUES (%s, %s)"
    data = (name, score)
    cur.execute(sql, data)
    con.commit()

    cur.close()
    con.close()
