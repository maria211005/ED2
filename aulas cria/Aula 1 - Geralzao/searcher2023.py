# ---------------------------------------------------------
# ---------------------------------------------------------

vetor = [35, 27, 10, 42, 11, 10, 39, 13, 22]
print(vetor)
len(vetor)

# ---------------------------------------------------------
# ---------------------------------------------------------

def buscaLinear(array, x):
  for i in range(0, len(array)):
    #print(array[i])
    if(x == array[i]):
      return True
  return False

# ---------------------------------------------------------
# ---------------------------------------------------------

print(vetor)

# encontra (x = 10)
print(buscaLinear(vetor, 10))
# nao encontra
print(buscaLinear(vetor, 1))

# ---------------------------------------------------------
# ---------------------------------------------------------

# Opcao: verificar se o vetor estar ordenado
# se ele estiver ordenado, percorre até encontrar ou encontrar um elemento
# maior que o X (quem eu procuro)

# Opcao: se nao tiver ordenado -> ordena (sort)
# percorre até encontrar o elemento ou 
# encontrar um elemento maior que o X

def buscaOrdenada(array, x):
  # ordena o vetor (mesmo se ja estiver ordenado)
  array.sort()
  for i in range(0, len(array)):
    if(x == array[i]):
      return True
    if(array[i] > x):
      return False
  return False

# ---------------------------------------------------------
# ---------------------------------------------------------

# encontra (x = 10) - True
print(buscaOrdenada(vetor, 10))
# nao encontra - False
print(buscaOrdenada(vetor, 1))

# ---------------------------------------------------------
# ---------------------------------------------------------