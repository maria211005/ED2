dados = [91, 3, 6, 75, 76, 89, -82, 31, -49, 70, 80, -93, 36, 77, -55]

def merge(vetor, inicio, meio, fim):
    aux = []
    p1 = inicio
    p2 = meio+1
    while(p1 < meio and p2 <= fim):
        if vetor[p1] < vetor[p2]:
            aux.append(vetor[p1])
            p1 = p1+1
        else:
            aux.append(vetor[p2])
            p2 = p2+1
    if p1 == meio:
        aux.append(vetor[p2])
    else:
        aux.append(vetor[p1])
    
    vetor = aux
    
def mergeSort(array, inicio, fim):
    if (inicio < fim):
        meio = (inicio + fim)/2
        mergeSort(array, inicio, meio)
        mergeSort(array, meio+1, fim)
    merge(array, inicio, meio, fim)
        
mergeSort(dados,0, len(dados))
print(dados)