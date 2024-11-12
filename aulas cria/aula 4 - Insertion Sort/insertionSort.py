dados = [91, 3, 6, 75, 76, 89, -82, 31, -49, 70, 80, -93, 36, 77, -55]

def insertionSort(array):
    for i in range(1, len(array)):
        auxiliar = array[i]
        j = i-1
        while (j >= 0) & (auxiliar < array[j]):
            array[j+1] = array[j]
            j = j-1
        array[j+1] = auxiliar
    return array
        
insertionSort(array = dados)
print(dados)