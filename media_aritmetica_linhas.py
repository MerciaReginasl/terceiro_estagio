#Dada a matriz M, determinar e mostrar as médias aritméticas de cada linha
numLin = int(input("Informe o número de linhas da matriz: "))
numCol = int(input("Informe o número de colunas da matriz: "))
matriz = []
print("Informe os elementos da matriz em ordem de linha, um em cada linha:")
for linha in range(0,numLin):
 matriz.append([])
 for coluna in range(0,numCol):
 matriz[linha].append(int(input()))
print("Matriz formatada(%dx%d):" % (numLin, numCol))
for linha in range(0,numLin):
 for coluna in range(0,numCol):
 print("%4d" % matriz[linha][coluna], end="")
 print()
print("Médias das linhas da matriz:")
for linha in range(0,numLin):
 soma = 0
 for coluna in range(0,numCol):
 soma += matriz[linha][coluna]
 print("Média da linha %d = %f" % (linha, soma/numCol))
