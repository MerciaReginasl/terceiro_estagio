def rotate_and_mirror(matrix):
    # Inverte a ordem das linhas
    reversed_matrix = matrix[::-1]
    
    # Inverte a ordem dos elementos em cada linha
    rotated_matrix = [row[::-1] for row in reversed_matrix]
    
    return rotated_matrix

def main():
    # Entrada das dimensões da matriz
    m = int(input("Digite o número de linhas da matriz: "))
    n = int(input("Digite o número de colunas da matriz: "))

    # Entrada dos elementos da matriz
    matrix = []
    print("Digite os elementos da matriz:")
    for i in range(m):
        row = []
        for j in range(n):
            element = int(input(f"Digite o elemento da posição [{i}][{j}]: "))
            row.append(element)
        matrix.append(row)

    # Rotaciona e espelha a matriz
    result_matrix = rotate_and_mirror(matrix)

    # Saída da matriz resultante
    print("\nMatriz resultante após rotação de 180º e espelhamento:")
    for row in result_matrix:
        print(row)

if __name__ == "__main__":
    main()
Este programa solicita ao usuário as dimensões da matriz e, em seguida, pede os elementos da matriz. Em seguida, ele chama a função rotate_and_mirror para rotacionar a matriz em 180º e espelhá-la e imprime a matriz resultante.

User
em phyton Escreva um programa em Python que dada uma matriz qualquer de tamanho m×n
, devolve o resultado dessa matriz após ser rotacionada em 180º e espelhada.
ChatGPT
Aqui está um programa Python que realiza a rotação de 180º e o espelhamento de uma matriz:

python
Copy code
def rotate_and_mirror(matrix):
    # Inverte a ordem das linhas
    reversed_matrix = matrix[::-1]
    
    # Inverte a ordem dos elementos em cada linha
    rotated_matrix = [row[::-1] for row in reversed_matrix]
    
    return rotated_matrix

def main():
    # Entrada das dimensões da matriz
    m, n = map(int, input("Digite as dimensões da matriz (linhas colunas): ").split())

    # Entrada dos elementos da matriz
    print("Digite os elementos da matriz:")
    matrix = []
    for i in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)

    # Rotaciona e espelha a matriz
    result_matrix = rotate_and_mirror(matrix)

    # Saída da matriz resultante
    print("\nMatriz resultante após rotação de 180º e espelhamento:")
    for row in result_matrix:
        print(*row)

if __name__ == "__main__":
    main()
