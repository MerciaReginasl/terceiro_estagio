def main():
    # Entrada dos números inteiros
    numeros = list(map(int, input().split()))

    # Encontra o maior elemento da lista e seu índice
    maior_elemento = max(numeros)
    indice_maior_elemento = numeros.index(maior_elemento)

    # Imprime o valor e o índice do maior elemento
    print(maior_elemento, indice_maior_elemento)

if __name__ == "__main__":
    main()
