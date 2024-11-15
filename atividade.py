#Bibliotecas para composição do código
from random import randint
import time
import copy
import sys
import math

#receber os parâmetros via linha de comando
if(len(sys.argv) != 3):
	print("Quantidade de argumentos inválida. Tente novamente")
else:
	entrada = sys.argv[1]     

#adequar o arquivo de entrada para uso dos valores
with open(entrada, "r") as f:
    #caso a leitura do arquivo for vazia
    if f.readline() == ' ':
        print("Arquivo vazio\nO programa será finalizado")
        exit(1)
    f.seek(0)   #desloca para o inicio do arquivo novamente caso tenha conteúdo 
    quant_numeros = f.readline().strip()    #assume o primeiro valor para a quantidade de números do vetor
    tipo_ord =  f.readline().strip()        #assume o segundo valor para o metodo com que seja organizado o vetor
    f.close()

#constroi o vetor inicial de acordo com o tipo de ordenação recebido
vetorInicial = []
if tipo_ord == 'c':                                                             #caso de vetor crescente
    for i in range (1, int(quant_numeros)+1):
        vetorInicial.append(i)
elif tipo_ord == 'd':                                                           #caso de vetor decrescente
    for i in range (int(quant_numeros), 0, -1):
        vetorInicial.append(i)
elif tipo_ord == 'r':                                                           #caso de vetor com valores aleatórios
    for i in range (int(quant_numeros)):
        vetorInicial.append(randint(0, 32000))
else:                                                                           #caso não tenha nenhum dos métodos aceitos
    print("Fora dos padrões: 'c', 'd' ou 'r'\nO programa será finalizado")
    exit(1)
    
#vetor inicial para comparar com as ordenações finais
print("Vetor inicial: ", vetorInicial)
print("--------------------------------------------------------------------------------------------------------------------------------------------")
#-------------------python--------------------------------------------------

#Bubble Sort
def bubbleSort(array):
    numeroComparacoes1 = 0
    troca = True
    while(troca):
        numeroComparacoes1 += 1
        troca = False
        
        for i in range(len(array)-1):
            numeroComparacoes1 += 1
            if(array[i] > array[i+1]):
                array[i], array[i+1] = array[i+1], array[i]
                troca = True
    return numeroComparacoes1

vetor1 = copy.deepcopy(vetorInicial)

inicio1 = time.time()
numeroComp = bubbleSort(vetor1)
fim1 = time.time()
duracao1 = (fim1 - inicio1)*1000

print("Bubble Sort:   ", vetor1, f"Tempo de execução:{duracao1:.4f} ms", "Número de Comparações:", numeroComp)
#-----------------------------------------------------------------------------------------

def insertionSort(array):
    numeroComparacoes2 = 0
    
    for i in range(1, len(array)):
        auxiliar = array[i]
        j = i-1
        
        numeroComparacoes2 += 1
        while (j >= 0) & (auxiliar < array[j]):
            numeroComparacoes2 += 1
            array[j+1] = array[j]
            j = j-1
            
        array[j+1] = auxiliar
            
    return numeroComparacoes2

vetor2 = copy.deepcopy(vetorInicial)

inicio1 = time.time()
numeroComp = insertionSort(vetor2)
fim1 = time.time()
duracao1 = (fim1 - inicio1)*1000

print("Insertion Sort:", vetor2, f"Tempo de execução:{duracao1:.4f} ms","Número de Comparações:", numeroComp)
#---------------------------------------------------------------------------------------

def selectionSort(array):
    numeroComparacoes3 = 0
    
    for N in range(len(array)):
        menor = array[N]
        indice = N
        
        for i in range(N, len(array)):
            numeroComparacoes3 += 1
            if array[i] < menor:
                menor = array[i]
                indice = i
                
        if menor != array[N]:
            array[N], array[indice] = array[indice], array[N]
            
    return numeroComparacoes3

vetor3 = copy.deepcopy(vetorInicial)

inicio1 = time.time()
numeroComp = selectionSort(vetor3)
fim1 = time.time()
duracao1 = (fim1 - inicio1)*1000

print("Selection Sort:", vetor3, f"Tempo de execução:{duracao1:.4f} ms","Número de Comparações:", numeroComp)
#-------------------------------------------------------------------------------------------

def Merge(array, inicio, meio, fim):
    numeroComp5 = 0
    vetor_auxiliar = [] #alocando dinamicamente o vetor 
    P1 = inicio #primeira e segunda metade respectivamente
    P2 = meio + 1 

    while(P1 <= meio and P2 <= fim):
        numeroComp5 += 1
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
            numeroComp5 += 1
    else:
        while P1 <= fim:
            vetor_auxiliar.append(array[P1])
            P1 = P1 + 1
            numeroComp5 += 1
    
    for i in range (inicio, fim+1):
        array[i] = vetor_auxiliar[i - inicio]
    
    return numeroComp5


def mergeSort(array, inicio, fim):
    numeroComparacoes5 = 0
    if(inicio < fim):
        meio = ((inicio + fim)//2)
        #agora começa as recursivas 
        mergeSort(array, inicio, meio) #divide a primeira metade
        mergeSort(array, meio+1, fim) #divide a segunda metade
        numeroComparacoes5 += Merge(array, inicio, meio, fim)
    
    return numeroComparacoes5

vetor4 = copy.deepcopy(vetorInicial)

inicio1 = time.time()
numeroComp = mergeSort(vetor4, 0, len(vetor4)-1) 
fim1 = time.time()
duracao1 = (fim1 - inicio1)*1000

print("Merge Sort:    ", vetor4, f"Tempo de execução:{duracao1:.4f} ms", "Número de Comparações:", numeroComp)
#-------------------------------------------------------------
def Particiona(array, inicio, fim):
    numeroComparacoes6 = 0
    esquerda = inicio
    direita = fim 
    pivo = array[inicio]

    #direcionando para que lado vai cada elemento 
    while(esquerda < direita):
        while(array[esquerda] <= pivo and esquerda < fim):
            numeroComparacoes6 += 1
            esquerda = esquerda + 1 #movendo o esq
        
        while(array[direita] > pivo and direita > inicio):
            numeroComparacoes6 += 1
            direita = direita - 1 #movendo o dir 

        numeroComparacoes6 += 1
        if(esquerda < direita):
            #trocando os dois vetores
            array[esquerda], array[direita] = array[direita], array[esquerda]
            
    array[direita], array[inicio] = array[inicio], array[direita]
    
    return(direita), numeroComparacoes6

def QuickSort(array, inicio, fim):
    numeroComp = 0
    if(inicio < fim):
        pivo, numeroComp = Particiona(array, inicio, fim)
        QuickSort(array, inicio, pivo-1)
        QuickSort(array, pivo+1, fim)
        
    return numeroComp

vetor5 = copy.deepcopy(vetorInicial)

inicio1 = time.time()
numeroComp = QuickSort(vetor5, 0, len(vetor5)-1)
fim1 = time.time()
duracao1 = (fim1 - inicio1)*1000
print("Quick Sort:    ", vetor5, f"Tempo de execução:{duracao1:.4f} ms", "Número de Comparações:", numeroComp)

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
    tamanhoHeap = len(array)-1
    for i in range (tamanhoHeap//2, 1, -1):
        maxHeapify(array, i)

def heapSort(array):
    numeroComp6 = 0
    buildMaxHeap(array)
    tamanho = len(array)-1
    for i in range (tamanho, 1, -1):
        numeroComp6 = numeroComp6 + 1
        array[0],array[i] = array[i],array[0]
        tamanho = tamanho - 1
        maxHeapify(array, 1)

vetor6 = copy.deepcopy(vetorInicial)

inicio1 = time.time()
numeroComp6 = heapSort(vetor6)
fim1 = time.time()
duracao1 = (fim1 - inicio1)*1000
#------------------------------------------------------------------------


#RADIX SORT ---> pra funcionar precisa do counting sort como auxiliar 
def countingSort(array, digito_numero, radix):
    #criar dois vetores 
    tamanho_array = len(array)

    lista_organizada = [] 
    #alocando a lista do tamanho do array
    for i in range (0, tamanho_array):
        lista_organizada[i] = 0
        #amg eu acho que da pra so multiplicar pelo tamanho mas td bem KKKKKKKK

    vetor_auxiliar = []
    for i in range (0, radix):
        vetor_auxiliar[i] = 0

    for i in range (0, tamanho_array):
        digito_array = (array[i]/radix ** digito_numero) % radix
        vetor_auxiliar[digito_array] = vetor_auxiliar[digito_array]+1

    for j in range (1, radix):
        vetor_auxiliar[j] = vetor_auxiliar[j] + vetor_auxiliar[j-1]

    for k in range (tamanho_array-1, -1, -1):
        digito_array = (array[k]/radix ** digito_numero) % radix
        vetor_auxiliar[digito_array] = vetor_auxiliar[digito_array]-1
        lista_organizada[vetor_auxiliar[digito_array]] = array[k]

        return lista_organizada
    
def radixSort(array, radix):
    maior_valor_lista = max(array)
    output = array
    digitos = int(math.floor(math.log(maior_valor_lista, radix)+1))

    for i in range (digitos):
        output = countingSort(output, i, radix)

    return output

vetor7 = copy.deepcopy(vetorInicial)

inicio1 = time.time()
radixSort(vetor7)
fim1 = time.time()
duracao1 = (fim1 - inicio1)*1000

print("Selection Sort:", vetor7, f"Tempo de execução:{duracao1:.4f} ms")
'''