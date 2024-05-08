def calcular_media_idades(idades):
    total_idades = sum(idades)
    qtd_pessoas = len(idades)
    media = total_idades / qtd_pessoas
    return media

def main():
    # Entrada da quantidade de pessoas
    qtd_pessoas = int(input("Digite a quantidade de pessoas: "))

    # Entrada das idades de cada pessoa
    idades = []
    for i in range(qtd_pessoas):
        idade = int(input(f"Digite a idade da pessoa {i+1}: "))
        idades.append(idade)

    # Calcula a média das idades
    media = calcular_media_idades(idades)

    # Saída da média aritmética com 2 casas decimais
    print(f"A média das idades é: {media:.2f}")

if __name__ == "__main__":
    main()
