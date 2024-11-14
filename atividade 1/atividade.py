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

print("Bubble Sort:", vetor1, f"   Tempo de execução:{duracao1:.4f} ms", "Número de Comparações:", numeroComp1)
#-----------------------------------------------------------------------------------------

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

vetor2 = copy.deepcopy(dados)

inicio1 = time.time()
numeroComp2 = insertionSort(vetor2)
fim1 = time.time()
duracao1 = (fim1 - inicio1)*1000

print("Insertion Sort:", vetor2, f"Tempo de execução:{duracao1:.4f} ms","Número de Comparações:", numeroComp2)
#---------------------------------------------------------------------------------------

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

vetor3 = copy.deepcopy(dados)

inicio1 = time.time()
numeroComp3 = insertionSort(vetor3)
fim1 = time.time()
duracao1 = (fim1 - inicio1)*1000

print("Selection Sort:", vetor3, f"Tempo de execução:{duracao1:.4f} ms","Número de Comparações:", numeroComp3)
#-------------------------------------------------------------------------------------------

def Merge(array, inicio, meio, fim):
    vetor_auxiliar = [] #alocando dinamicamente o vetor 
    P1 = inicio #primeira e segunda metade respectivamente
    P2 = meio + 1 

    while(P1 <= meio and P2 <= fim):
        if(array[P1] < array[P2]): #add P1 no vetor aux
            vetor_auxiliar.append(array[P1])
            P1 = P1 + 1
        else: #add P2 no vetor aux
            vetor_auxiliar.append(array[P2])
            P2 = P2 + 1
    
    #saiu do while
    if (P1 == meio+1):
        while P2 <= fim:
            vetor_auxiliar.append(array[P2])
            P2 = P2 + 1
    else:
        while P1 <= fim:
            vetor_auxiliar.append(array[P1])
            P1 = P1 + 1
    
    for i in range (inicio, fim+1):
        array[i] = vetor_auxiliar[i - inicio]


def mergeSort(array, inicio, fim):
    if(inicio < fim):
        meio = ((inicio + fim)//2)
        #agora começa as recursivas 
        mergeSort(array, inicio, meio) #divide a primeira metade
        mergeSort(array, meio+1, fim) #divide a segunda metade
        Merge(array, inicio, meio, fim)

vetor4 = copy.deepcopy(dados)

inicio1 = time.time()
mergeSort(vetor4, 0, len(vetor4)-1) 
fim1 = time.time()
duracao1 = (fim1 - inicio1)*1000
print("Merge Sort:", vetor4)
#-------------------------------------------------------------
def Particiona(array, inicio, fim):
    esquerda = inicio
    direita = fim 
    pivo = array[inicio]

    #direcionando para que lado vai cada elemento 
    while(esquerda < direita):
        while(array[esquerda] <= pivo and esquerda < fim):
            esquerda = esquerda + 1 #movendo o esq
        
        while(array[direita] > pivo and direita > inicio):
            direita = direita - 1 #movendo o dir 

        if(esquerda < direita):
            #trocando os dois vetores
            array[esquerda], array[direita] = array[direita], array[esquerda]
    array[direita], array[inicio] = array[inicio], array[direita]
    return(direita)

def QuickSort(array, inicio, fim):
    numeroComp5 = 0
    if(inicio < fim):
        numeroComp5 = numeroComp5 + 1
        pivo = Particiona(array, inicio, fim)
        QuickSort(array, inicio, pivo-1)
        QuickSort(array, pivo+1, fim)

vetor5 = copy.deepcopy(dados)

inicio1 = time.time()
numeroComp5 = QuickSort(vetor5, 0, len(vetor5)-1)
fim1 = time.time()
duracao1 = (fim1 - inicio1)*1000
print("Quick Sort:", vetor5)

'''
#--------------------------------------------------------------
def esquerda(i):
    return 2*i+1

def direita(i):
    return 2*i+2

#função que deixa o heap com o valor maximo na raiz
def maxHeapify(array, i):
    left = esquerda(i) #chamando as funções p/ calcular a posicao dos filhos
    right = direita(i)
    maior = i

    if(left <= len(array) and array[left] > array[i]):
        maior = left
    
    if(right <= len(array) and array[right] > array[maior]):
        maior = right

    if (maior != i):
        #corrige se o filho estiver maior que o pai, trocando os dois de lugar
        array[i],array[maior] = array[maior],array[i]
        maxHeapify(array, maior) 

def buildMaxHeap(array):
    tamanhoHeap = len(array)
    for i in range (tamanhoHeap//2, 1):
        maxHeapify(array, i)

def heapSort(array):
    numeroComp6 = 0
    buildMaxHeap(array)
    tamanho = len(array)
    for i in range (tamanho, 2, -1):
        numeroComp6 = numeroComp6 + 1
        array[1],array[i] = array[i],array[1]
        tamanho = tamanho - 1
        maxHeapify(array, 1)

vetor6 = copy.deepcopy(dados)

inicio1 = time.time()
numeroComp6 = heapSort(vetor6)
fim1 = time.time()
duracao1 = (fim1 - inicio1)*1000
#------------------------------------------------------------------------

'''