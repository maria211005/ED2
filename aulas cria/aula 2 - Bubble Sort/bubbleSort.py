#Ordena o vetor usando BubbleSort
#Parâmetros:
#array: vetor a ser ordenado
#option: opção que define se a ordenação é crescente ou
#decrescente
#Esse algoritmo tem um comportamento assintótico O(N2)

dados = [91, 3, 6, 75, 76, 89, -82, 31, -49, 70, 80, -93, 36, 77, -55]


def bubbleSort(array):
    troca = True
    while(troca):
        troca = False
        
        for i in range(0, len(array)-1):
            if(array[i] > array[i+1]):
                array[i], array[i+1] = array[i+1], array[i]
                troca = True

bubbleSort(array = dados)
print(dados)