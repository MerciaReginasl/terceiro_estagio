def verificar_ordem(lista):
    crescente = all(lista[i] < lista[i+1] for i in range(len(lista)-1))
    decrescente = all(lista[i] > lista[i+1] for i in range(len(lista)-1))
    iguais = any(lista[i] == lista[i+1] for i in range(len(lista)-1))
    
    return crescente, decrescente, iguais

def main():
    # Entrada da quantidade de elementos
    n = int(input("Quantidade de elementos: "))

    # Entrada das 3 listas
    lista1 = [int(input("Lista 1 - Elemento {}: ".format(i+1))) for i in range(n)]
    lista2 = [int(input("Lista 2 - Elemento {}: ".format(i+1))) for i in range(n)]
    lista3 = [int(input("Lista 3 - Elemento {}: ".format(i+1))) for i in range(n)]

    # Verifica a ordem das listas
    ordem_lista1 = verificar_ordem(lista1)
    ordem_lista2 = verificar_ordem(lista2)
    ordem_lista3 = verificar_ordem(lista3)

    # Saída para a lista 1
    print("Lista 1:")
    print("É crescente?", ordem_lista1[0])
    print("É decrescente?", ordem_lista1[1])
    print("Possui elementos consecutivos iguais?", ordem_lista1[2])

    # Saída para a lista 2
    print("\nLista 2:")
    print("É crescente?", ordem_lista2[0])
    print("É decrescente?", ordem_lista2[1])
    print("Possui elementos consecutivos iguais?", ordem_lista2[2])

    # Saída para a lista 3
    print("\nLista 3:")
    print("É crescente?", ordem_lista3[0])
    print("É decrescente?", ordem_lista3[1])
    print("Possui elementos consecutivos iguais?", ordem_lista3[2])

if __name__ == "__main__":
    main()
