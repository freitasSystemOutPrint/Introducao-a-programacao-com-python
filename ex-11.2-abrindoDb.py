import sqlite3
conexao = sqlite3.connect("agenda.db2")
cursor = conexao.cursor()
cursor.execute("select * from agenda")
resultato = cursor.fetchone()
print(f'Nome:  {resultato} \n Tefefone: {resultato}')
print('Nome: %s\nTelefone: %s' % (resultato))