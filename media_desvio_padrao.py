def calcular_media(lista):
    return sum(lista) / len(lista)

def calcular_desvio_padrao(lista):
    media = calcular_media(lista)
    soma_quadrados_diferenca = sum((x - media) ** 2 for x in lista)
    desvio_padrao = math.sqrt(soma_quadrados_diferenca / len(lista))
    return desvio_padrao

def main():
    # Entrada da quantidade de listas e a quantidade de elementos de cada lista
    m = int(input("Quantidade de listas: "))
    n = int(input("Quantidade de elementos em cada lista: "))

    for i in range(m):
        print(f"Lista {i + 1}:")
        # Entrada dos elementos da lista
        lista = [int(input()) for _ in range(n)]

        # Calcula e imprime a média e o desvio padrão da lista
        media = calcular_media(lista)
        desvio_padrao = calcular_desvio_padrao(lista)
        print("{:.2f}".format(media))
        print("{:.2f}".format(desvio_padrao))

if __name__ == "__main__":
    main()
