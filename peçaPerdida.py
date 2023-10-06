#A quantidade de peças que deveriam ter no quebra cabeças
entradaUm = int(input("Digite a primeira entrada: "))
#A entrada que corresponde a todas as peças que temos do quebra cabeça
entradaDois = input("Digite a segunda entrada: ")
#Lista incompleta
listaInc = []
#Lista de todos os números entre n e 1, incluindo os 2
listaComp = []
#For loop que vai adicionar os valores entre n e 1 na lista completa
for i in range(entradaUm):
    listaComp.append(i + 1)
#For loop que vai remover os valores que existem na lista incompleta mas não existem na lista completa
for i in range(len(entradaDois)):
    if(entradaDois[i] != " "):
        listaComp.remove(int(entradaDois[i]))
#O resultado é igual ao valor que sobrar na lista completa
resultado = str(listaComp[0])
#Printa o resultado
print(resultado)
