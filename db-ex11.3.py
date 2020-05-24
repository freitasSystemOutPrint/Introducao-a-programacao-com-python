import sqlite3
conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()
cursor.execute('''
        create table agenda (
            nome text,
            telefone text )
''')

cursor.execute('''
        insert into agenda (nome, telefone)
            values(?, ?)

''', ("Freitas", "94-99248-3518"))
conexao.commit()
cursor.close()
conexao.close()