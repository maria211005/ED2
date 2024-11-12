dados = [91, 3, 6, 75, 76, 89, -82, 31, -49, 70, 80, -93, 36, 77, -55]
import time

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
    
inicio2 = time.time()
selectionSort(array = dados)
fim2 = time.time()
duracao2 = fim2 - inicio2

print("Selection Sort:", dados)
print(f"Duração: {duracao2:.6f} s")