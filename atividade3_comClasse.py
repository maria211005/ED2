import sys

class Heroi:
    def __init__(self, linha_sep):
            self.key = linha_sep[0]
            self.Name = linha_sep[1]
            self.Alignment = linha_sep[2]
            self.Gender = linha_sep[3]
            self.EyeColor = linha_sep[4]
            self.Race = linha_sep[5]
            self.HairColor = linha_sep[6]
            self.Publisher = linha_sep[7]
            self.SkinColor = linha_sep[8]
            self.Height = linha_sep[9]
            self.Weight = linha_sep[10]
            self.Intelligence = linha_sep[11]
            self.Strength = linha_sep[12]
            self.Speed = linha_sep[13]
            self.Durability = linha_sep[14]
            self.Power = linha_sep[15]
            self.Combat = linha_sep[16]
            self.Total = linha_sep[17]

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
        if linha1[0] == '\n':
            print("arquivo vazio\nO programa será finalizado")
            exit(1)
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
#função de heap sort
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
#função de merge sort
def Merge(array, inicio, meio, fim, ord): #func. auxiliar 
    vetor_auxiliar = [] #alocando dinamicamente o vetor 
    P1 = inicio #primeira e segunda metade respectivamente
    P2 = meio + 1 

    if ord == 'C':
        while(P1 <= meio and P2 <= fim): #voltando da recursao e reagrupando 
            if(array[P1] < array[P2]): #add P1 no vetor aux
                vetor_auxiliar.append(array[P1])
                P1 = P1 + 1
            else: #add P2 no vetor aux
                vetor_auxiliar.append(array[P2])
                P2 = P2 + 1
    
    if ord == 'D':
        while(P1 <= meio and P2 <= fim): #voltando da recursao e reagrupando 
            if(array[P1] > array[P2]): #add P1 no vetor aux
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

def mergeSort(array, inicio, fim, ord): #func. principal
    if(inicio < fim):
        meio = ((inicio + fim)//2)
        #agora começa as recursivas 
        mergeSort(array, inicio, meio, ord) #dividindo recursivamente
        mergeSort(array, meio+1, fim, ord)
        Merge(array, inicio, meio, fim, ord)
#----------------------------------------------------------------------------------------------------------------------
def escreveArquivo(RRN):
    with open(saida, 'w+') as output:
        output.write(header)

        tam = []
        for linha in registros:
            tam.append(len(linha))

        tamRegistro = tam[0]
        for i in range(len(tam)-1):
            if tam[i] > tamRegistro:
                tamRegistro = tam[i]

        for i in range (len(RRN)):    
            for linha in registros:
                linha_sep = linha.split(sep='|')
                if RRN[i] == int(linha_sep[0]):
                    linha = linha.strip('\n')
                    if len(linha) < tamRegistro:
                        dif = tamRegistro - len(linha) -1
                        linha = linha + '|' +'*' * dif + '\n'
                    else:
                        linha = linha + '\n'
                        #escreve a linha no arquivo de saida
                    output.write(linha)
#---------------------------------------------------------------------------------------------------
def defineHeroi(registro):
    arq = []
    for linha in registro:
        linha_sep = linha.split(sep='|')
        resultado = Heroi(linha_sep)
        arq.append(resultado.key)
        arq.append(resultado.Name)
        arq.append(resultado.Alignment)
        arq.append(resultado.Gender)
        arq.append(resultado.EyeColor)
        arq.append(resultado.Race)
        arq.append(resultado.HairColor)
        arq.append(resultado.Publisher)
        arq.append(resultado.SkinColor)
        arq.append(resultado.Height)
        arq.append(resultado.Weight)
        arq.append(resultado.Intelligence)
        arq.append(resultado.Strength)
        arq.append(resultado.Speed)
        arq.append(resultado.Durability)
        arq.append(resultado.Power)
        arq.append(resultado.Combat)
        arq.append(resultado.Total)
    print(arq)
    
    return arq

#função principal
if __name__ == "__main__":
    metodoBusca, ordenacao, header, registros = defineTipoOrdenacao(entrada)
    print(f"metodo = {metodoBusca}, ordenacao = {ordenacao}")

    arquivo = []
    arquivo = defineHeroi(registros)
    key = []
    key.append(arquivo[0])
    for i in range(len(arquivo)):
        if '\n' in arquivo[i]:
            key.append(arquivo[i+1])
    
    print(key)
'''
    if metodoBusca == 'H':
        heapSort(key, ordenacao)
    if metodoBusca == 'I':
        insertionSort(key, ordenacao)
    if metodoBusca == 'M':
        mergeSort(key, 0, len(key) -1, ordenacao)
    #if metodoBusca == 'Q':
        #quickSort(registros)
    escreveArquivo(key)
'''