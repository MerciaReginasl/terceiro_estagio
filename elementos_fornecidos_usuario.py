'''
Os elementos ai,j de uma matriz inteira Am,n (fornecida pelo
usuário) representam os custos de transporte da cidade i para a
cidade j. Dado um itinerário fornecido pelo usuário, fornecer o
custo desse itinerário. Exemplo:
O custo do itinerário [0, 3, 1, 3, 3, 2, 1, 0] é
a0,3 + a3,1 + a1,3 + a3,3 + a3,2 + a2,1 + a1,0 = 3 + 1 + 400 + 5 + 2 + 1 + 5 = 417
'''

numLin = int(input("Informe o número de linhas da matriz: "))
numCol = int(input("Informe o número de colunas da matriz: "))
matriz = []
print("Informe os elementos da matriz em ordem de linha, "+" um em cada linha:")
for linha in range(0,numLin):
 matriz.append([])
 for coluna in range(0,numCol):
 matriz[linha].append(int(input()))
print("Matriz({numLin}x{numCol}):")
for linha in range(0,numLin):
 for coluna in range(0,numCol):
 print(“{matriz[linha][coluna]:4d} ", end="")
 print()

numInt = int(input("Informe o número de coordenadas do
intinerário: "))
intinerario = []
print("Informe as coordenadas do intinerário:")
for posicao in range(0,numInt):
 intinerario.append(int(input()))
print(intinerario)
custo = 0
for posicao in range(0,numInt-1):
 custo +=
matriz[intinerario[posicao]][intinerario[posicao+1]]
print("O custo do intinerário {intinerario} é {custo:.2f}")
