#Armazenar os nomes e idades de 6 pessoas em uma matriz, e imprimir o nome da pessoa mais nova:

▪ Solução:
'''
#EM2: Escreva um programa que armazena os nomes e idades de 6 pessoas,
 #em uma matriz, e imprima o nome da pessoa mais nova.
'''
matriz = []
# preenche a matriz
for i in range(6):
 linha = []
 linha.append(input(f"Digite o nome da pessoa {i+1}: "))
 linha.append(input(f"Digite a idade de {linha[0]}: "))
 matriz.append(linha)
# procura a pessoa mais nova
menor = matriz[0][1]
pos = 0
for i in range(6):
 if matriz[i][1] < menor:
 menor = matriz[i][1]
 pos = i
# imprime a matriz
for i in range(6):
 print(matriz[i])
# imprime a pessoa mais nova
print(f"A pessoa mais nova é {matriz[pos][0]}")
