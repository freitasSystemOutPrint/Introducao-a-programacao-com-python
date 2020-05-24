import sqlite3
dados = [   ("João" , "94-99578-8574"),
            ("André", "94-99147-9445"),
            ("Maria", "94-99784-4752")]
conexao = sqlite3.connect("agenda.db2")
cursor = conexao.cursor()
cursor.executemany('''
        insert into agenda (nome, telefone)
        values(?, ?)
''', dados)
conexao.commit()
cursor.close()
conexao.close()