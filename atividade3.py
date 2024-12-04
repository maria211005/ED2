import sys

#receber os parâmetros via linha de comando
entrada = ''
saida = ''
if(len(sys.argv) != 3):
    print("Quantidade de argumentos inválida. Tente novamente")
    exit(1)
else:
    entrada = sys.argv[1]
    saida = sys.argv[2]
#---------------------------------------------------------------------------------------------
#define a forma com que será organizado os dados
def defineTipoOrdenacao(arquivo):
    with open(arquivo, "r") as f:
        linha1 = f.readlines(200)           #verifica se tem algo no arquivo
        if len(linha1) < 3:
            print("arquivo inválido\nO programa será finalizado")
            exit(1)
        f.seek(0)                           #se tiver dados no arquivo, desloca para o começo
        
        linha1 = f.readline()               
        linha1 = linha1.strip("\n")         
        linha1_sep = linha1.split(sep=",")  #separa em uma lista com as duas condições

        sort = linha1_sep[0]                #o primeiro é o método de ordenação
        order = linha1_sep[1]               #o segundo é a forma com que seja ordenado

        sort = sort[len(sort)-1]            #recebe a letra do método
        order = order[len(order)-1]         #recebe a letra 

        if sort != 'Q' and sort != 'H' and  sort != 'M' and sort != 'I':
            print(f"opção {sort} de sort inválida\no programa será finalizado")
            exit(1)
        if order != 'C' and order != 'D':
            print(f"opção {order} de order inválida\no programa será finalizado")
            exit(1)

        cabecalho = f.readline()
        registro = f.readlines()
            
    return sort, order, cabecalho, registro
#---------------------------------------------------------------------------------------
#def quickSort():
#def mergeSort():
def esquerda(i):
    return 2*i+1

def direita(i):
    return 2*i+2

#função que deixa o heap com o valor maximo na raiz
def maxHeapify(reg, i, tamReg, ord):
    left = esquerda(i) #chamando as funções p/ calcular a posicao dos filhos
    right = direita(i)
    maior = i

    if ord == 'C':
        if(left < tamReg and reg[left] > reg[maior]):
            maior = left
        
        if(right < tamReg and reg[right] > reg[maior]):
            maior = right

    if ord == 'D':
        if(left < tamReg and reg[left] < reg[maior]):
            maior = left
        
        if(right < tamReg and reg[right] < reg[maior]):
            maior = right

    if (maior != i):
        #corrige se o filho estiver maior que o pai, trocando os dois de lugar
        reg[i], reg[maior] = reg[maior], reg[i]
        maxHeapify(reg, maior, tamReg, ord)

def buildMaxHeap(reg, ord): #constroi o heap
    tamanhoHeap = len(reg)
    for i in range (len(reg)//2 - 1, -1, -1):
        maxHeapify(reg, i, tamanhoHeap, ord)

def heapSort(reg, ord):
    buildMaxHeap(reg, ord)
    tamanho = len(reg)
    for i in range (len(reg)-1, 0, -1): #troca o primeiro valor com o da ultima posicao livre
        (reg[0],reg[i]) = (reg[i],reg[0])
        tamanho -= 1
        maxHeapify(reg, 0, tamanho, ord)
#---------------------------------------------------------------------------------------------------------------------
#função de insertion sort
def insertionSort(reg, ord):
        for i in range(1, len(reg)): #percorrendo vetor 
            auxiliar = reg[i]
            j = i-1 #contador auxiliar
            
            if ord == 'C':
                while (j >= 0) & (auxiliar < reg[j]): #procura o menor elemento e joga na primeira posicao livre
                    reg[j+1] = reg[j]
                    j = j-1
                    
                    reg[j+1] = auxiliar
            if ord == 'D':
                while (j >= 0) & (auxiliar > reg[j]): #procura o maior elemento e joga na primeira posicao livre
                    reg[j+1] = reg[j]
                    j = j-1
                    
                    reg[j+1] = auxiliar
#----------------------------------------------------------------------------------------------------------------------
def escreveArquivo():
    with open(saida, 'w+') as output:
        output.write(header)

        tam = []
        for linha in registros:
            tam.append(len(linha))

        tamRegistro = tam[0]
        for i in range(len(tam)-1):
            if tam[i] > tamRegistro:
                tamRegistro = tam[i]

        for i in range (len(RRN)-1):    
            for linha in registros:
                linha_sep = linha.split(sep='|')
                if RRN[i] == int(linha_sep[0]):
                    linha = linha.strip('\n')
                    if len(linha) < tamRegistro:
                        dif = tamRegistro - len(linha) -1
                        linha = linha + '*' * dif + '\n'
                    else:
                        linha = linha + '\n'
                        #escreve a linha no arquivo de saida
                    output.write(linha)

#função principal
if __name__ == "__main__":
    metodoBusca, ordenacao, header, registros = defineTipoOrdenacao(entrada)

    RRN = []
    for linha in registros:
        linha_sep = linha.split(sep='|')
        RRN.append(int(linha_sep[0]))

    if metodoBusca == 'H':
        heapSort(RRN, ordenacao)
    if metodoBusca == 'I':
        insertionSort(RRN, ordenacao)
    #if metodoBusca == 'M':
        #mergeSort(registros)
    #if metodoBusca == 'Q':
        #quickSort(registros)

    escreveArquivo()