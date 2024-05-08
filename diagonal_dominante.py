def diagonal_dominante(matriz):
    n = len(matriz)
    for i in range(n):
        diagonal_element = matriz[i][i]
        other_elements_sum = sum(abs(matriz[i][j]) for j in range(n) if j != i)
        if diagonal_element <= other_elements_sum:
            return False
    return True

def main():
    # Entrada da ordem da matriz
    n = int(input())

    # Entrada dos elementos da matriz
    matriz = []
    for _ in range(n):
        linha = list(map(int, input().split()))
        matriz.append(linha)

    # Verifica se a matriz é estritamente diagonal dominante
    if diagonal_dominante(matriz):
        print("SIM")
    else:
        print("NAO")

if __name__ == "__main__":
    main()
