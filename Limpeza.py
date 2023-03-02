# Limpeza dos dados

# Importando bibliotecas necessárias
import csv
import sqlite3

# Abrindo o arquivo CSV com os dados de produção de alimentos
with open('producao_alimentos.csv', 'r') as dados_alimentos:
    
    # Lendo o arquivo
    reader = csv.reader(dados_alimentos)

    # Pulando a primeira linha, que contém os cabeçalhos das colunas
    next(reader)

    # Conectando ao banco de dados
    conn = sqlite3.connect('dsadb.db')

    # Deletando a tabela producao, se houver
    conn.execute('DROP TABLE IF EXISTS producao')

    # Criando uma nova tabela para armazenar os dados de produção de alimentos
    conn.execute('''CREATE TABLE producao (
                    produto TEXT,
                    quantidade INTEGER,
                    preco_medio REAL,
                    receita_total REAL
                )''')

    # Inserindo cada linha do arquivo com quantidade maior que 10 na tabela do banco de dados
    for row in reader:
        if int(row[1]) > 10:
            conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total) VALUES (?, ?, ?, ?)', row)

    conn.commit()
    conn.close()

print("Concluído com Sucesso!")