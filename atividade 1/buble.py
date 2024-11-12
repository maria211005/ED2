import time

def bubbleSort(array):
        troca = True
        while(troca):
            troca = False
            
            for i in range(0, len(array)-1):
                if(array[i] > array[i+1]):
                    array[i], array[i+1] = array[i+1], array[i]
                    troca = True
                    
inicio1 = time.time()
bubbleSort(array)
fim1 = time.time()
duracao1 = fim1 - inicio1

print("Bubble Sort:")
print(f"Duração: {duracao1:.6f} s")
