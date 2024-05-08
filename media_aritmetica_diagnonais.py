#Dada a matriz quadrada Q (m=n), determine e mostre a média aritmética dos
#elementos da diagonal principal:
ordem = int(input("Informe a ordem da matriz quadrada: "))
matriz = []
print("Informe os elementos da matriz em ordem de linha, um em cada linha: ")
for linha in range(0,ordem):
 matriz.append([])
 for coluna in range(0,ordem):
 matriz[linha].append(int(input()))
print(f"Matriz({ordem:2d}x{ordem:2d}):")
for linha in range(0,ordem):
 for coluna in range(0,ordem):
 print(f"{matriz[linha][coluna]:4d} ", end="")
 print()
soma = 0
for indice in range(0,ordem):
 soma += matriz[indice][indice]
print(f"Média da diagonal principal = {soma/ordem:.4f}")
