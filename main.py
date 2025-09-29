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

# # Atualizar os dados no banco de dados
# cursor.execute("""
# UPDATE alunos
# SET nome = ?, idade = ?,curso = ?
# WHERE id = ?
# """,("Maria",18, "ADS", 2))
# conexao.commit()
# print("Dados atualizados com sucesso!")

# Consultar os dados no banco de dados
# cursor.execute("SELECT * FROM alunos")
# # Ferchall traz todas as linhas da consulta
# for linha in cursor.fetchall():
#     print(f"ID {linha[0]} | NOME: {linha[1]} | IDADE: {linha[2]} | CURSO: {linha[3]}")

# # Selecionar apenas os alunos de computação no banco
# cursor.execute("SELECT * FROM alunos WHERE curso = ?", ("Computação",))
# for linha in cursor.fetchall():
#     print(f"ID {linha[0]} | NOME: {linha[1]} | IDADE: {linha[2]} | CURSO: {linha[3]}")

# Deletando dados do banco
'''cursor.execute("DELETE FROM alunos WHERE id =?", (3,))
conexao.commit()
# Sempre fechar a conexão no final
conexao.close()'''

# Versão melhor
def deletar_aluno():
    try:
        conexao = sqlite3.connect("escola.db")
        cursor = conexao.cursor()
        id_aluno = int(input("Digite o id do aluno que deseja deletar:"))
        cursor.execute("DELETE FROM alunos WHERE id =?", (id_aluno,))
        conexao.commit()

        # Verifcar se o aluno foi realmente deletado
        if cursor.rowcount > 0:
            print("Aluno removido com sucesso!")
        else:
            print("Nenhum aluno cadastrado com o ID fornecido")
    except Exception as erro:
        print("Erro ao tentar excluir o aluno {erro}")
    finally:
        # Sempre fecha a conexão com sucesso ou erro
        if conexao:
            conexao.close()

deletar_aluno()