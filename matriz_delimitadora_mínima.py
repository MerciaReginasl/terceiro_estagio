def menor_recorte(matriz):
    # Encontrando limites superior e inferior
    min_linha = min(i for i, row in enumerate(matriz) if 1 in row)
    max_linha = max(i for i, row in enumerate(matriz) if 1 in row)
    min_coluna = min(j for row in matriz for j, val in enumerate(row) if val == 1)
    max_coluna = max(j for row in matriz for j, val in enumerate(row) if val == 1)
    
    # Criando a matriz de recorte
    recorte = [row[min_coluna:max_coluna + 1] for row in matriz[min_linha:max_linha + 1]]
    
    return recorte

# Exemplo de matriz de entrada
matriz_entrada = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Chamando a função e imprimindo a matriz de recorte
recorte = menor_recorte(matriz_entrada)
for linha in recorte:
    print(linha)
