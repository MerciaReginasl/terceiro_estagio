def calcular_estatisticas(valores):
    # Variáveis para armazenar os somatórios e as quantidades
    soma_impares = 0
    soma_pares = 0
    qtd_impares = 0
    qtd_pares = 0

    # Calcula os somatórios e as quantidades
    for valor in valores:
        if valor % 2 == 0:
            soma_pares += valor
            qtd_pares += 1
        else:
            soma_impares += valor
            qtd_impares += 1

    # Retorna os resultados
    return soma_impares, soma_pares, qtd_impares, qtd_pares

def main():
    # Entrada do valor de n
    n = int(input("Digite o valor de n: "))

    # Lista para armazenar os valores
    valores = []

    # Entrada dos valores
    print("Digite os valores da lista:")
    for _ in range(n):
        valor = int(input())
        valores.append(valor)

    # Chama a função para calcular as estatísticas
    soma_impares, soma_pares, qtd_impares, qtd_pares = calcular_estatisticas(valores)

    # Saída dos resultados
    print("Somatório dos números ímpares:", soma_impares)
    print("Somatório dos números pares:", soma_pares)
    print("Quantidade de números ímpares:", qtd_impares)
    print("Quantidade de números pares:", qtd_pares)
    print("Lista completa:", valores)

if __name__ == "__main__":
    main()
