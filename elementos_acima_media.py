def main():
    # Entrada dos números
    numeros = list(map(int, input().split()))

    # Calcula a média dos números
    media = sum(numeros) / len(numeros)

    # Imprime os números acima da média
    for num in numeros:
        if num > media:
            print(num, end=" ")

if __name__ == "__main__":
    main()
