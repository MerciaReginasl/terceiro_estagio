def eh_quadrado_magico(matriz):
    n = len(matriz)
    # Soma das diagonais principal e secundária
    diagonal_principal = sum(matriz[i][i] for i in range(n))
    diagonal_secundaria = sum(matriz[i][n - i - 1] for i in range(n))
    if diagonal_principal != diagonal_secundaria:
        return False
    # Soma das linhas e colunas
    for i in range(n):
        linha_sum = sum(matriz[i][j] for j in range(n))
        coluna_sum = sum(matriz[j][i] for j in range(n))
        if linha_sum != coluna_sum or linha_sum != diagonal_principal:
            return False
    return True

def main():
    # Entrada da dimensão da matriz
    n = int(input())

    # Entrada dos elementos da matriz
    matriz = []
    for _ in range(n):
        linha = list(map(int, input().split()))
        matriz.append(linha)

    # Verifica se a matriz é um quadrado mágico
    if eh_quadrado_magico(matriz):
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    main()
