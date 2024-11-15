def counting_sort(array, exp):
    numero_elementos = len(array)
    output = [0] * numero_elementos
    contador  = [0] * 10

    for i in range(numero_elementos):
        posicao = (array[i] // exp) % 10
        contador[posicao] = contador[posicao] + 1

    for i in range(1, 10):
        contador [i] = contador [i] + contador [i - 1]

    i = numero_elementos - 1
    while i >= 0:
        posicao = (array[i] // exp) % 10
        output[contador [posicao] - 1] = array[i]
        contador [posicao] = contador[posicao]-1
        i = i-1

    for i in range(numero_elementos):
        array[i] = output[i]

def radix_sort(array):
    max1 = max(array)
    exp = 1
    while max1 // exp > 0:
        counting_sort(array, exp)
        exp *= 10

# Exemplo de uso
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Array antes da ordenação:")
print(arr)
radix_sort(arr)
print("Array após a ordenação:")
print(arr)