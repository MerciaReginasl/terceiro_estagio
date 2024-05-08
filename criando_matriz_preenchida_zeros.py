#Criar uma matriz m x n preenchida com zeros e mostrar a matriz na tela
#m e n são dinâmicos, recebidos do usuário
# use o conceito de FUNÇÃO

'''
EM3: Escreva um programa que cria uma matriz m x n, preenchida
 com zeros, e mostra a matriz na tela.
'''
# Função criar matriz
def cria_matriz(m, n, valor_inicial):
 matriz = []
 for i in range(m):
 linha = []
 for i in range(n):
 linha.append(valor_inicial)
 matriz.append(linha)
 return matriz
# Função que realiza as ações do programa principal
def principal():
 # recebe do usuário as dimensões da matriz
 m = int(input("Digite a dimensão m (n°. de linhas) da matriz: "))
 n = int(input("Digite a dimensão n (n°. de colunas) da matriz: "))
 matriz = cria_matriz(m, n, 0)
 print(matriz)
# Programa Principal
principal()

_________________________________________

'''
#EM4: Escreva um programa que cria uma matriz m x n, preenchida
 #com zeros, e mostra a matriz na tela, no formato padrão.
'''
# Função criar matriz
def cria_matriz(m, n, valor_inicial):
 matriz = []
 for i in range(m):
 linha = []
 for i in range(n):
 linha.append(valor_inicial)
 matriz.append(linha)
 return matriz
# Função mostrar matriz
def mostra_matriz(matriz):
 linhas = len(matriz)
 colunas = len(matriz[0])
 for i in range(linhas):
 for j in range(colunas):
 print(f"{matriz[i][j]} ", end="")
 print()
 return
# Função que realiza as ações do programa principal
def principal():
 # recebe do usuário as dimensões da matriz
 m = int(input("Digite a dimensão m (n°. de linhas) da matriz: "))
 n = int(input("Digite a dimensão n (n°. de colunas) da matriz: "))
 matriz = cria_matriz(m, n, 0)
 mostra_matriz(matriz)
# Programa Principal
principal()
