import numpy as np
import pandas as pd


def retorna_mediana(vetor:np.array, tamanho:int = 0) -> np.array:
    if tamanho == 0:
        tamanho = len(vetor)
    
    inicio = vetor[0]
    meio = vetor[tamanho]
    fim = vetor[-1]
    
    return np.median(vetor[0])


def quicksort(vetor:np.array) -> np.array:
    tamanho = len(vetor)
    
    if tamanho < 2:
        return vetor
    
    else:
        mediana = retorna_mediana(vetor, tamanho)
        pivo = np.where(vetor == mediana)[0][0]
        
        # realizando a troca
        auxiliar = vetor[pivo]
        vetor[pivo] = vetor[-1]
        vetor[-1] = auxiliar
        
        contador = 0
        
        for i in range(tamanho - 1):
            if vetor[i] <= vetor[-1]:
                
                # realizando a troca
                auxiliar = vetor[contador]
                vetor[contador] = vetor[i]
                vetor[i] = auxiliar
                
                contador += 1
    
        parte_esquerda = quicksort(vetor[:contador])
        parte_direita = quicksort(vetor[(contador + 1):])
    
        return np.concatenate((parte_esquerda, [vetor[contador]], parte_direita))


def main():
    vetor = np.array([9, 1, 3, 4, 2, 0], dtype = "uint8")
    vetor = quicksort(vetor)


if __name__ == "__main__":
    main()
    