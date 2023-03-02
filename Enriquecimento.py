# Adicionando uma coluna na tabela producao com a margem de lucrode cada produto

# importando as bibliotecas necessárias

import csv
import sqlite3

# Criando uma função para remover o ponto da coluna receita_total
def remove_ponto(valor):
    return int(valor.replace('.', ''))

# Abrindo o arquivo CSV com os dados da produção de alimentos
with open('producao_alimentos.csv', 'r') as dados_alimentos:
    
    # Lendo o arquivo CSV
    reader = csv.reader(dados_alimentos)

    # Pulando a primeira linha, que contém os cabeçalhos das colunas
    next(reader)

    # Conectando ao banco de dados
    conn = sqlite3.connect('dsadb.db')

    # Deletando a tabela existente, se houver
    conn.execute('DROP TABLE IF EXISTS producao')

    # Criando uma nova tabela para armazenar os dados de produção de alimentos com a nova coluna 'margem_lucro'
    conn.execute('''CREATE TABLE producao (
                    produto TEXT,
                    quantidade INTEGER,
                    preco_medio REAL,
                    receita_total INTEGER,
                    margem_lucro REAL
                )''')

    # Inserindo cada linha do arquivo com quantidade maior que 10 na tabela do banco de dados
    for row in reader:
        if int(row[1]) > 10:
            
            # Chamando a função que remove o ponto
            row[3] = remove_ponto(row[3])

            # Calculando a margem de lucro
            margem_lucro = (row[3] / float(row[1])) - float(row[2])

            # Inserindo a linha com a nova coluna 'margem_lucro' na tabela do banco de dados
            conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total, margem_lucro) VALUES (?, ?, ?, ?, ?)', (row[0], row[1], row[2], row[3], margem_lucro))

    conn.commit()
    conn.close()

print("Concluído com Sucesso!")