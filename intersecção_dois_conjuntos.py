def quantidade_elementos_comuns(a, b):
    # Converte as listas em conjuntos para facilitar a comparação
    set_a = set(a)
    set_b = set(b)

    # Retorna a quantidade de elementos em comum entre os conjuntos
    return len(set_a.intersection(set_b))

def main():
    # Entrada da quantidade de elementos de a e b
    n = int(input("Quantidade de elementos de a: "))
    m = int(input("Quantidade de elementos de b: "))

    # Entrada dos elementos de a e b
    elementos_a = [int(input()) for _ in range(n)]
    elementos_b = [int(input()) for _ in range(m)]

    # Calcula a quantidade de elementos de a que estão em b
    quantidade = quantidade_elementos_comuns(elementos_a, elementos_b)

    # Saída da quantidade de elementos em comum
    print(quantidade)

if __name__ == "__main__":
    main()
