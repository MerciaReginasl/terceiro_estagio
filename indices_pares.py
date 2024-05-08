def elementos_indices_pares(lista):
    for i in range(0, len(lista), 2):
        print(lista[i], end=" ")

def main():
    # Entrada da lista de números inteiros
    lista = list(map(int, input().split()))

    # Encontra e imprime os elementos em índices pares
    elementos_indices_pares(lista)

if __name__ == "__main__":
    main()
