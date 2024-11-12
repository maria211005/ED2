#Ordena o vetor usando Selection Sort
#Parâmetros:
#array: vetor a ser ordenado
#option: 1 - ordenação crescente, 2 - ordenação decrescente
import time
dados = [91, 3, 6, 75, 76, 89, -82, 31, -49, 70, 80, -93, 36, 77, -55]

def selectionSort(array):
    for N in range(len(array)):
        menor = array[N]
        indice = N
        for i in range(N, len(array)):
            if array[i] < menor:
                menor = array[i]
                indice = i
        if menor != array[N]:
            array[N], array[indice] = array[indice], array[N]
    return array

inicio = time.time()
selectionSort(array = dados)
fim = time.time()
duracao = fim - inicio

print(dados)
print(f"Demorou {duracao:.6f} s para compilar")