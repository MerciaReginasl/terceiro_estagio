def encontrar_primeiro_par_adjacente(lista):
    for i in range(len(lista) - 1):
        if lista[i] * lista[i+1] > 0:
            return lista[i], lista[i+1]
    return 0

def main():
    # Entrada dos números inteiros
    numeros = list(map(int, input().split()))

    # Encontra o primeiro par adjacente com o mesmo sinal
    par_adjacente = encontrar_primeiro_par_adjacente(numeros)

    # Imprime o par adjacente encontrado ou 0 se não houver
    if par_adjacente != 0:
        print(par_adjacente[0], par_adjacente[1], end=" ")
    else:
        print(0)

if __name__ == "__main__":
    main()
