#lendo cinco notas e mostrando a média da
turma
notas = []
for i in range(0, 5, 1):
 mensagem = f"Digite a nota{i+1}: "
 notas.append(float(input(mensagem)))
media = 0
for i in range(0, 5, 1):
 media += notas[i]
media /= 5
print(notas)
print(media)
