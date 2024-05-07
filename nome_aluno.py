nome1 = input("Informe o nome do aluno 1: ")
nome2 = input("Informe o nome do aluno 2: ")
nome3 = input("Informe o nome do aluno 3: ")
nota1 = float(input("Informe a nota de " + nome1 +\
":"))
nota2 = float(input("Informe a nota de " + nome2 +\
":"))
nota3 = float(input("Informe a nota de " + nome3 +\
":"))
media = (nota1 + nota2 + nota3)/3
print("A media da turma foi %.1f", % media)
if nota1 > media:
 print("Parabéns, %s!", % nome1)
if nota2 > media:
 print("Parabéns, %s!", % nome2)
if nota3 > media:
 print("Parabéns, %s!", % nome3)
