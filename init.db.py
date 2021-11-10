import sqlite3

connection = sqlite3.connect('connectmei.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()


cur.execute("INSERT INTO pessoasfisicas (nomepf, cpf, sexopf, emailpf, celularpf, logradouropf, numeropf, bairropf, cidadepf, ufpf, ceppf, senhapf) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", ('Allana Raimunda Joana Barbosa', 41167709810, 'F', 'allanaraimundajoanabarbosa_@sabesp.com.br', 16994697475, 'Rua São Lourenço', '188', 'Jardim São José', 'Matão', 'SP', 15996018, 'cdef4321'))


cur.execute("INSERT INTO pessoasjuridicas (nomepj, cnpj, profissao_nome, emailpj, celularpj, logradouropj, numeropj, bairropj, cidadepj, ufpj, ceppj, senhapj) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", ('Teste1', 85918867000183, 'ABATEDOR(A) DE AVES COM COMERCIALIZAÇÃO DO PRODUTO INDEPENDENTE 4724-5/00', 'marketing@benicioesarahpadariame.com.br', 11995385171, 'Rua da Moeda', '400', 'Vila Itaberaba', 'São Paulo', 'SP', 2847010,  'abcd123'))


connection.commit()
connection.close()