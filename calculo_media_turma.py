Calcule a média da turma
'''
# inicializa a matriz de notas da turma
turma = [
 [5.0, 4.5, 7.0, 5.2, 6.1],
 [2.1, 6.5, 8.0, 7.0, 6.7],
 [8.6, 7.0, 9.1, 8.7, 9.3]
]
# inicializa a variável de cálculo da média
media = 0
# laço de repetição para percorrer as linhas
for i in range(3):
 # laço de repetição para percorrer as linhas
 for j in range(5):
 # acumula a nota em media
 media = media + turma[i][j]
# finaliza o cálculo da média
media = media / 15
# exibe na tela o resultado
print(media)

____________________________________________________

#Solução escalável:
'''
EM1: Calcule a média da turma
'''
# inicializa a matriz de notas da turma
turma = [
 [5.0, 4.5, 7.0, 5.2, 6.1],
 [2.1, 6.5, 8.0, 7.0, 6.7],
 [8.6, 7.0, 9.1, 8.7, 9.3]
]
# descobre o tamanho da turma
linhas = len(turma)
colunas = len(turma[0])
# inicializa a variável de cálculo da média
media = 0
# laço de repetição para percorrer as linhas
for i in range(linhas):
 # laço de repetição para percorrer as linhas
 for j in range(colunas):
 # acumula a nota em media
 media = media + turma[i][j]
# finaliza o cálculo da média
media = media / (linhas * colunas)
# exibe na tela o resultado
print(media)
