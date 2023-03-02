# Transformando os dados da coluna receita_total removendo o ponto para evitar 
# que os dados sejam truncados.

# Importando as bibliotecas necessárias
import csv
import sqlite3

# Criando uma função para remover o ponto nos dados da coluna receita_total
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

    # Criando uma nova tabela para armazenar os dados de produção de alimentos
    conn.execute('''CREATE TABLE producao (
                    produto TEXT,
                    quantidade INTEGER,
                    preco_medio REAL,
                    receita_total INTEGER
                )''')

    # Inserindo cada linha do arquivo com quantidade maior que 10 na tabela do banco de dados
    for row in reader:
        if int(row[1]) > 10:
            
            # Chamando a função que remove o ponto
            row[3] = remove_ponto(row[3])

            # Inserindo os valores no banco de dados
            conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total) VALUES (?, ?, ?, ?)', row)

    conn.commit()
    conn.close()

print('Concluído com Sucesso!')