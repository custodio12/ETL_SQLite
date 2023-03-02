# Conectando com o banco de dados

# Importando bibliotecas necessárias

import csv
import sqlite3

# Criando um novo banco de dados
conn = sqlite3.connect('dsadb.db')

# Criando uma tabela para armazenar os dados
conn.execute('''CREATE TABLE producao (
                produto TEXT,
                quantidade INTEGER,
                preco_medio REAL,
                receita_total REAL
            )''')

# Gravando e fechando conexão
conn.commit()
conn.close()

# Abrindo o arquivo CSV com os dados de produção de alimentos
with open('producao_alimentos.csv', 'r') as dados_alimentos:
    
    # Lendo o arquivo
    reader = csv.reader(dados_alimentos)

    # Pulando a primeira linha, que contém os cabeçalhos das colunas
    next(reader)

    # Conectando ao banco de dados
    conn = sqlite3.connect('dsadb.db')

    # Insere cada linha do arquivo na tabela do banco de dados
    for row in reader:
        conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total) VALUES (?, ?, ?, ?)', row)

    conn.commit()
    conn.close()

print("Concluído com Sucesso!")