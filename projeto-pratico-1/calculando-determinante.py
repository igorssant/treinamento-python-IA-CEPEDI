import numpy as np

def calculo_determinante(matriz:np.array) -> np.array:
    indices = list(range(len(matriz)))
    total = 0
     
    if ((matriz.shape[0] == 2) and (matriz.shape[1] == 2)):
        return ((matriz[0][0] * matriz[1][1]) - (matriz[1][0] * matriz[0][1]))
 
    for indice_atual in indices:
        matriz_temporaria = np.copy(matriz)
        matriz_temporaria = matriz_temporaria[1:]
        tamanho = matriz_temporaria.shape[0] 
 
        for i in range(tamanho):
            matriz_temporaria[i] = matriz_temporaria[i][0:indice_atual] + matriz_temporaria[i][(indice_atual+1):] 
 
        sinal = (-1) ** (indice_atual % 2)
        sub_determinante = calculo_determinante(matriz_temporaria)
        total += sinal * matriz[0][indice_atual] * sub_determinante
        
    return total

def main():
    linhas = int(input("Digite a quantidade de linhas da matriz:\n"))
    colunas = int(input("Digite a quantidade de colunas da matriz:\n"))
    
    matriz = np.zeroes((linhas, colunas))
    
    print("Digite os valores das linhas da matriz")
    
    for i in range(linhas):
        matriz[i,:] = input().split()


if __name__ == "__main__":
    main()
