#Adicionando vários elementos na matriz:
# inicializando matriz vazia de notas da turma
turma = []
# lendo três notas de cinco alunos
for i in range(0,3,1):
 notas = [] # inicializando lista vazia de notas
 for j in range(0,5,1):
 mensagem = f"Digite a nota{j+1} do aluno {i+1}: "
 notas.append(float(input(mensagem)))
 turma.append(notas) # inserindo lista de notas na matriz
# mostrando toda a matriz de notas
print(turma)
