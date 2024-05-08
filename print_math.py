def printmat(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def multiply_matrix(matrix, c):
    multiplied_matrix = [[element * c for element in row] for row in matrix]
    return multiplied_matrix

def main():
    # Entrada do número de linhas e colunas
    m, n = map(int, input("Digite o número de linhas e colunas da matriz (m n): ").split())

    # Entrada dos elementos da matriz
    print("Digite os elementos da matriz:")
    matrix = []
    for i in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)

    # Entrada do número inteiro c
    c = int(input("Digite o número inteiro para multiplicar os elementos da matriz: "))

    # Multiplica os elementos da matriz por c
    multiplied_matrix = multiply_matrix(matrix, c)

    # Imprime a matriz resultante
    print("Matriz resultante após multiplicar cada elemento por", c, ":")
    printmat(multiplied_matrix)

if __name__ == "__main__":
    main()
