def posicao_maior(matriz):
    maior_elemento = matriz[0][0]
    linha_maior, coluna_maior = 0, 0

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] > maior_elemento:
                maior_elemento = matriz[i][j]
                linha_maior, coluna_maior = i, j

    return linha_maior, coluna_maior

def main():
    # Entrada do número de linhas e colunas
    m, n = map(int, input().split())

    # Entrada da matriz
    matriz = []
    for _ in range(m):
        linha = list(map(int, input().split()))
        matriz.append(linha)

    # Encontra os índices do maior elemento
    linha_maior, coluna_maior = posicao_maior(matriz)

    # Saída dos índices do maior elemento
    print(linha_maior, coluna_maior)

if __name__ == "__main__":
    main()
