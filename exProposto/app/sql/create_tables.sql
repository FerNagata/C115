CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    question VARCHAR(50) NOT NULL,
    option1 VARCHAR(50) NOT NULL,
    option2 VARCHAR(50) NOT NULL,
    option3 VARCHAR(50) NOT NULL,
    option4 VARCHAR(50) NOT NULL,
    answer INT NOT NULL
);

CREATE TABLE scores(
    id SERIAL PRIMARY KEY,  
    nome VARCHAR(50) NOT NULL,
    score INT NOT NULL
);

INSERT INTO questions (question, option1, option2, option3, option4, answer)
VALUES ('Qual o maior país do mundo?', 'Brasil', 'China', 'Rússia', 'EUA', 3);

INSERT INTO questions (question, option1, option2, option3, option4, answer)
VALUES ('Quantos continentes existem no mundo?', '4', '5', '6', '7', 3);

INSERT INTO questions (question, option1, option2, option3, option4, answer)
VALUES ('Qual o país com a maior população?', 'Índia', 'China', 'Paquistão', 'EUA', 1);


