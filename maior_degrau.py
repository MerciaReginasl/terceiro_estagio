def maior_altura_degrau(n, sequencia):
    maior_altura = 0
    
    for i in range(1, n):
        diferenca_absoluta = abs(sequencia[i] - sequencia[i-1])
        if diferenca_absoluta > maior_altura:
            maior_altura = diferenca_absoluta
    
    return maior_altura

def main():
    # Entrada da quantidade de termos e da sequência
    n = int(input("Quantidade de termos: "))
    sequencia = [int(input()) for _ in range(n)]

    # Calcula a maior altura de um degrau
    altura_maxima = maior_altura_degrau(n, sequencia)

    # Saída da maior altura de um degrau
    print("Maior altura de um degrau:", altura_maxima)

if __name__ == "__main__":
    main()
