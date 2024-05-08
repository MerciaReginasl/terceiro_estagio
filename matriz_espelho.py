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
    for i in range(m):
        row = []
        for j in range(n):
            element = int(input(f"Digite o elemento da posição [{i}][{j}]: "))
            row.append(element)
        matrix.append(row)

    # Rotaciona e espelha a matriz
    result_matrix = rotate_and_mirror(matrix)

    # Saída da matriz resultante
    print("Matriz resultante após rotação de 180º e espelhamento:")
    for row in result_matrix:
        print(row)

if __name__ == "__main__":
    main()
