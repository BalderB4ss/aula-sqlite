# Importar a biblioteca sqlite3
import sqlite3

#criar uma conexão com o banco de dados chamado "escola.db"
conexao = sqlite3.connect("escola.db")

#Criar um objeto "cursor" server para executar os comandos SQL
cursor = conexao.cursor()

# #criar uma tabela no banco de dados
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS alunos (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     idade INTEGER,
#     curso TEXT)
# """)
# print("Tabela criada com sucesso!")

# # Inserir um aluno no banco de dados
# nome = input("Digite o nome do aluno que deseja cadastrar: ")
# cursor.execute("""
# INSERT INTO alunos (nome,idade,curso)
# VALUES (?,?,?)
# """,(nome, 20, "Medicina"))

# # Podemos cadastrar varias informações no banco de dados
# alunos = [
#     ("Enzo", 22, "Direito"),
#     ("Murilo", 33, "computação"),
#     ("Eduardo", 41, "Computação")
# ]

# cursor.executemany("""
# INSERT INTO alunos (nome,idade,curso)
# VALUES (?,?,?)
# """,(alunos)
# )

# # Precisamos confirmar as alterações no banco de dados
# conexao.commit()

# Atualizar os dados no banco de dados
cursor.execute("""
UPDATE alunos
SET nome = ?, idade = ?,curso = ?
WHERE id = ?
""",("Maria",18, "ADS", 2))
conexao.commit()
print("Dados atualizados com sucesso!")

