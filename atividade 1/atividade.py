#teste pra ver se ta enviando certo o cod no git
from random import randint
import time

with open("input8.txt", "r") as f:
    quant_numeros = f.readline().strip()
    if type(quant_numeros) != int:
        print("Erro ao receber variável")
        exit(1)
    tipo_ord =  f.readline().strip()
    f.close()
        
print(quant_numeros, tipo_ord)
dados = []
if tipo_ord == 'c':
    for i in range (1, quant_numeros+1):
        dados.append(i)
elif tipo_ord == 'd':
    for i in range (quant_numeros, 0, -1):
        dados.append(i)
elif tipo_ord == 'r':
    for i in range (quant_numeros):
        dados.append(randint(0, 32000))
else:
    print("Fora dos padrões: 'c', 'd' ou 'r'\nO programa será finalizado")
    exit(1)

print("Começo: ",dados)
#---------------------------------------------------------------------
def bubbleSort(array):
    troca = True
    while(troca):
        troca = False
        
        for i in range(0, len(array)-1):
            if(array[i] > array[i+1]):
                array[i], array[i+1] = array[i+1], array[i]
                troca = True

inicio1 = time.time()
bubbleSort(dados)
fim1 = time.time()
duracao1 = fim1 - inicio1

print("Bubble Sort:", dados,  "Tempo de execução:", duracao1)
