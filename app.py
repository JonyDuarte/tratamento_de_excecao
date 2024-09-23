#tratamento de excecao
try:
    nome=( input("informe o nome:"))
    idade= int(input("informe a idade:")) 

    print("nome: {nome}.")
    print("idade: {idade}.")
except:
    print("Não foi posssível mostrar os dados.")