#teste pra ver se ta enviando certo o cod no git
from random import randint
import time
import copy

with open("input1.txt", "r") as f:
    if f.readline() == ' ':
        print("Arquivo vazio")
        exit(1)
    f.seek(0)
    quant_numeros = f.readline().strip()
    tipo_ord =  f.readline().strip()
    f.close()
        
dados = []
if tipo_ord == 'c':
    for i in range (1, int(quant_numeros)+1):
        dados.append(i)
elif tipo_ord == 'd':
    for i in range (int(quant_numeros), 0, -1):
        dados.append(i)
elif tipo_ord == 'r':
    for i in range (int(quant_numeros)):
        dados.append(randint(0, 32000))
else:
    print("Fora dos padrões: 'c', 'd' ou 'r'\nO programa será finalizado")
    exit(1)

#---------------------------------------------------------------------
def bubbleSort(array):
    numeroComparacoes1 = 0
    troca = True
    while(troca):
        troca = False
        
        for i in range(0, len(array)-1):
            if(array[i] > array[i+1]):
                numeroComparacoes1 = numeroComparacoes1 + 1
                array[i], array[i+1] = array[i+1], array[i]
                troca = True
    return numeroComparacoes1

print("Vetor inicial:", dados)
vetor1 = copy.deepcopy(dados)

inicio1 = time.time()
numeroComp1 = bubbleSort(vetor1)
fim1 = time.time()
duracao1 = (fim1 - inicio1)*1000

print("Bubble Sort:", vetor1)
print(f"Tempo de execução:{duracao1:.4f} ms","\nNúmero de Comparações:", numeroComp1)
print("#---------------------------------------------------------------------")

def insertionSort(array):
    numeroComparacoes2 = 0
    for i in range(1, len(array)):
        auxiliar = array[i]
        j = i-1
        while (j >= 0) & (auxiliar < array[j]):
            numeroComparacoes2 = numeroComparacoes2 + 1
            array[j+1] = array[j]
            j = j-1
        array[j+1] = auxiliar
    return numeroComparacoes2

print("Vetor inicial:", dados)
vetor2 = copy.deepcopy(dados)

inicio1 = time.time()
numeroComp2 = insertionSort(vetor2)
fim1 = time.time()
duracao1 = (fim1 - inicio1)*1000

print("Insertion Sort:", vetor2)
print(f"Tempo de execução:{duracao1:.4f} ms","\nNúmero de Comparações:", numeroComp2)
print("#---------------------------------------------------------------------")

def selectionSort(array):
    numeroComparacoes3 = 0
    for N in range(len(array)):
        menor = array[N]
        indice = N
        for i in range(N, len(array)):
            if array[i] < menor:
                numeroComparacoes3 = numeroComparacoes3 + 1
                menor = array[i]
                indice = i
        if menor != array[N]:
            array[N], array[indice] = array[indice], array[N]
    return numeroComparacoes3

print("Vetor inicial:", dados)
vetor3 = copy.deepcopy(dados)

inicio1 = time.time()
numeroComp3 = insertionSort(vetor3)
fim1 = time.time()
duracao1 = (fim1 - inicio1)*1000

print("Selection Sort:", vetor3)
print(f"Tempo de execução:{duracao1:.4f} ms","\nNúmero de Comparações:", numeroComp3)
print("#---------------------------------------------------------------------")