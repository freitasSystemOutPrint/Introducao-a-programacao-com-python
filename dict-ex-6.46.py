tabela = {
    "Alface": 0.45,
    "Batata": 1.20,
    "Tomate": 2.50,
    "Feijao": 1.50}

#print(tabela["Tomate"])
#print(tabela)

while True:
    produto=input("Digite o nome do produto, fim para terminar")
    if produto == "fim":
        break
    if produto in tabela:
        print(f'Preço {tabela[produto]} {tabela}')
    else:
        print('Produto não encontrado.')