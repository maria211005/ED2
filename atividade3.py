import sys
#---------------------------------------------------------------------------------------
#definido o objeto heroi
#---------------------------------------------------------------------------------------
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
#---------------------------------------------------------------------------------------
#receber os parâmetros via linha de comando
#---------------------------------------------------------------------------------------
entrada = ''
saida = ''
#caso não tenha a quantidade de argumentos válida para execução do código
if(len(sys.argv) != 3):
    print("Quantidade de argumentos inválida. Tente novamente")
    exit(1)
else:
    entrada = sys.argv[1]
    saida = sys.argv[2]
#---------------------------------------------------------------------------------------
#define como será o método de ordenação e a forma com que serão ordenados
#---------------------------------------------------------------------------------------
def defineTipoOrdenacao(arquivo):
    with open(arquivo, "r") as f:
        linha1 = f.readlines(200)           #verifica se tem algo no arquivo
        if linha1[0] == '\n':
            print("arquivo vazio\nO programa será finalizado")
            exit(1)
        if len(linha1) < 3:
            print("arquivo incompleto\nO programa será finalizado")
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

        #leitura do header e dos registros do arquivo
        cabecalho = f.readline()
        registro = f.readlines()

        #encontrar a quantidade de campos do registro
        campos = []
        for linha in registro:
            linhaSep = linha.split(sep='|')
            campos.append(len(linhaSep))
        
        #quantidade de campos para evitar conflito com quantidades invalidas
        quantidadeCampos = campos[0]
        for i in range(len(campos)-1):
            if campos[i] > quantidadeCampos:
                quantidadeCampos = campos[i]

    return sort, order, cabecalho, registro, quantidadeCampos
#---------------------------------------------------------------------------------------
#função que define armazena os registros no objeto heroi e guarda as chaves para ordenação
#---------------------------------------------------------------------------------------
def defineChave(registro, quantCampos):
    arq = []
    for linha in registro:
        linha_sep = linha.split(sep='|')
        #caso a quantidade de campos não estiver na forma correta, os dados não serão recebidos no objeto
        if len(linha_sep) < quantCampos:
            linha_sep[len(linha_sep)-1] = linha_sep[len(linha_sep)-1].strip("\n")
            linha_sep.append("-\n")

        #escreve cada campo em um atributo
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

    key = []                                        #aloca um vetor de chaves
    key.append(int(arq[0]))                         #armazena o primeiro valor referente ao primeiro registro
    for i in range(len(arq)):
        if '\n' in arq[i] and i != len(arq) - 1:    #e enquanto for fim do registro mas não fim do arquivo
            key.append(int(arq[i+1]))               #o próximo elemento é o indice do proximo registro
    
    return key, arq
#---------------------------------------------------------------------------------------
#função de heap sort
#---------------------------------------------------------------------------------------
def esquerda(i):
    return 2*i+1

def direita(i):
    return 2*i+2

#função que deixa o heap com o valor maximo na raiz
def maxHeapify(reg, i, tamReg, ord):
    left = esquerda(i) #chamando as funções p/ calcular a posicao dos filhos
    right = direita(i)
    maior = i

    #caso o método escolhido for crescente
    if ord == 'C':
        if(left < tamReg and reg[left] > reg[maior]):
            maior = left
        
        if(right < tamReg and reg[right] > reg[maior]):
            maior = right

    #caso for descrescente
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
#---------------------------------------------------------------------------------------
#função de insertion sort
#---------------------------------------------------------------------------------------
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
#---------------------------------------------------------------------------------------
#função de merge sort
#---------------------------------------------------------------------------------------
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

        #dividindo recursivamente
        mergeSort(array, inicio, meio, ord)
        mergeSort(array, meio+1, fim, ord)
        
        Merge(array, inicio, meio, fim, ord)                #reorganiza os elementos dos vetores divididos
#---------------------------------------------------------------------------------------
#função de quick sort
#---------------------------------------------------------------------------------------
def particiona(array, inicio, fim, ord):
    esquerda = inicio
    direita = fim 
    pivot = array[inicio]

    if ord == 'C':
        while(esquerda < direita):
            while(array[esquerda] <= pivot and esquerda < fim):
                esquerda = esquerda + 1 #movimentando

            while(array[direita] > pivot and direita > inicio):
                direita = direita - 1 #movimentando 

            if(esquerda < direita):
                array[esquerda], array[direita] = array[direita], array[esquerda]

    if ord == 'D':
        while(esquerda < direita):
            while(array[esquerda] >= pivot and esquerda < fim):
                esquerda = esquerda + 1 #movimentando

            while(array[direita] < pivot and direita > inicio):
                direita = direita - 1 #movimentando 

            if(esquerda < direita):
                array[esquerda], array[direita] = array[direita], array[esquerda]
    
    array[direita], array[inicio] = array[inicio], array[direita]

    return direita

def quickSort(array, inicio, fim, ord):
    if(inicio < fim):
        pivo = particiona(array, inicio, fim, ord)
        quickSort(array, inicio, pivo-1, ord) 
        quickSort(array, pivo+1, fim, ord)
#---------------------------------------------------------------------------------------
#função de escrita dos registros no arquivo de saída
#---------------------------------------------------------------------------------------
def escreveArquivo(chave):
    with open(saida, 'w+') as output:
        output.write(header)                                #escreve o cabeçalho no arquivo
        tam = []
        quantCarac = 0
        #escreve todos os registros no arquivo de saída e armazena o tamanho de cada um deles em um vetor
        for i in range(len(arq)):
            if '\n' in arq[i]:                              #verifica se o elemento do vetor é o fim do registro
                output.write(arq[i])
                quantCarac = quantCarac + len(arq[i]) + 1
                tam.append(quantCarac)                      #guarda o tamanho do registro no vetor
                quantCarac = 0
            else:
                output.write(arq[i] + "|")                  #caso contrário, continua escrevendo os elementos do vetor no arquivo
                quantCarac = quantCarac + len(arq[i]) + 1

        #verifica qual o maior registro
        maxRegistro = tam[0]
        for i in range(len(tam)-1):
            if tam[i] > maxRegistro:
                maxRegistro = tam[i]

        output.seek(len(header))
        registros = output.readlines()                      #faz a leitura de todos os registros já escritos
        output.seek(len(header))

        #analisa as chaves dos herois para ordenar o arquivo
        for i in range (len(chave)):    
            for linha in registros:
                linha_sep = linha.split(sep='|')
                if chave[i] == int(linha_sep[0]):           #caso a chave indicada for igual ao campo key do registro
                    linha = linha.strip('\n')
                    if len(linha) < maxRegistro:            #verifica o tamanho da linha pra inserir caracteres especiais ou não
                        dif = maxRegistro - len(linha) -1
                        linha = linha + '|' +'*' * dif + '\n'
                    else:                                   #caso for a maior linha
                        linha = linha + '\n'
                    output.write(linha)                     #sobrescreve a linha no arquivo de saida
#---------------------------------------------------------------------------------------
#função principal
#---------------------------------------------------------------------------------------
if __name__ == "__main__":
    #abre o arquivo de entrada para receber as informações do arquivo como: metodo com que será ordenado
    #como será ordenado, cabeçalho do arquivo, cada linha de registro e quantos campos tem um registro
    metodoBusca, ordenacao, header, registros, quantCampos = defineTipoOrdenacao(entrada)

    #separa as chaves do arquivo em um vetor para ordenar
    #retorna o vetor e o arquivo com os atributos de cada heroi separados
    key, arq = defineChave(registros, quantCampos)

    #métodos de ordenação
    if metodoBusca == 'H':
        heapSort(key, ordenacao)
    if metodoBusca == 'I':
        insertionSort(key, ordenacao)
    if metodoBusca == 'M':
        mergeSort(key, 0, len(key) -1, ordenacao)
    if metodoBusca == 'Q':
        quickSort(key, 0, len(key) -1, ordenacao)

    #escreve os registros no arquivo de forma ordenada
    escreveArquivo(key)

    print("Os herois do professor M estão organizados!!") #YUPIIIIIIII