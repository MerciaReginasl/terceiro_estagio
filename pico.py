def verifica_pico(lista):
    if len(lista) < 3:
        return False

    crescente = False
    decrescente = False

    for i in range(1, len(lista)):
        if lista[i] > lista[i-1]:
            crescente = True
        elif lista[i] < lista[i-1]:
            decrescente = True

        if crescente and decrescente:
            return True

    return False

def main():
    n = int(input())
    numeros = [int(input()) for _ in range(n)]

    if verifica_pico(numeros):
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    main()
