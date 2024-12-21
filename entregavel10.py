import sys
#-----------------------------------------------------------------------------
#função sys.argv
#-----------------------------------------------------------------------------
entrada = ''
#caso não tenha a quantidade de argumentos válida para execução do código
if(len(sys.argv) != 3):
    print("Quantidade de argumentos inválida. Tente novamente")
    exit(1)
else:
    entrada = sys.argv[1]
    entrada2 = sys.argv[2]

#-----------------------------------------------------------------------------
#funções de abertura e organização
#-----------------------------------------------------------------------------
#abre o arquivo para obter as informações dos registros
def abreArquivo():
    with open(entrada, "r+") as file:           #abre o arquivo inicial
        #recebe o cabeçalho e os registros
        header = file.readline()
        registros = file.readlines()

        tupla = []
        offset = 0
        tam = []
        for linha in registros:
            tam.append(len(linha))              #guarda o tamanho de cada linha
            linha_sep = linha.split(",")
            chave = linha_sep[0]                #guarda o nome do registro como chave
            tupla.append(f"{chave}|{offset}")   #monta a tupla com a chave do registro e o indice da linha
            offset += 1
        
        #define o maior registro para alinhar os outros
        maxRegistro = tam[0]
        for i in range(len(tam)-1):
            if tam[i] > maxRegistro:
                maxRegistro = tam[i]

    with open(entrada2, "w") as output:     #abre um segundo arquivo para escrever os registros alinhados
        output.write(header)
        for linha in registros:
            linha = organizaLinha(linha, maxRegistro)   #adiciona os caracteres especiais de cada registro
            output.write(linha)
    return tupla, registros, maxRegistro

#função de organizar as linhas do registro
def organizaLinha(linha, maxRegistro):
    linha = linha.strip("\n")
    linha = linha.replace(",","|")
    if len(linha) < maxRegistro:            #verifica o tamanho da linha pra inserir caracteres especiais ou não
        dif = maxRegistro - len(linha) -1
        linha = linha + '*' * dif + '\n'
    else:                                   #caso for a maior linha
        linha = linha + '\n'
    return linha

#função auxiliar da função de ordenação
def ParticionaTupla(tupla, inicio, fim):
    esquerda = inicio 
    direita = fim
    pivo = tupla[inicio]

    while(esquerda < direita):
        while(tupla[esquerda] <= pivo and esquerda < fim):
            esquerda = esquerda + 1

        while(tupla[direita] > pivo and direita > inicio):
            direita = direita - 1 

        if(esquerda < direita):
            tupla[esquerda], tupla[direita] = tupla[direita], tupla[esquerda]
    
    tupla[direita], tupla[inicio] = tupla[inicio], tupla[direita]

    return direita

#função de ordenar a tupla 
def OrdenaTupla(tupla, inicio, fim):
    if(inicio < fim):
        pivo = ParticionaTupla(tupla, inicio, fim) 
        OrdenaTupla(tupla, inicio, pivo-1)
        OrdenaTupla(tupla, pivo+1, fim)

#-----------------------------------------------------------------------------
#funções de pesquisa
#-----------------------------------------------------------------------------
#realiza a busca para encontrar o registro pesquisado
def BuscaBinaria(tupla, chave):
    inicio = 0
    fim = len(tupla) - 1
    while(inicio <= fim):
        meio = (inicio + fim) // 2          
        chave_reg = tupla[meio]             #determina o meio do vetor
        chave_reg = chave_reg.split("|")
        if chave in chave_reg[0]:           #caso encontrar a chave
           return chave_reg

        if chave_reg[0] > chave:            #caso a chave for menor que o meio
           fim = meio - 1 

        else:                               #caso a chave for maior que o meio
           inicio = meio + 1
    
    if inicio > fim:                        #caso percorrer todo o vetor de chaves e não encontrar
        return -1

#realiza a localização e exibição do registro encontrado
def buscaRegistro(arqEntrada, maxRegistro, chave):
    rrn = int(chave[1])

    with open(arqEntrada, 'r') as file:
        file.seek(len(file.readline()) + rrn*maxRegistro)   #desloca do inicio do arquivo até o registro encontrado
        print("Registro Encontrado\n" + file.readline())    #exibe o registro

#função de pesquisa do registro
def pesquisa_de_registro(tupla, tamRegs, anime, origem):
    chaveEncontrada = BuscaBinaria(tupla, anime)
    if chaveEncontrada == -1:
        return chaveEncontrada
    else:
        if origem == 0:
            buscaRegistro(entrada2, tamRegs, chaveEncontrada)
        else:
            return 1
        
#-----------------------------------------------------------------------------
#funções de inserção
#-----------------------------------------------------------------------------
def insereTupla(novoRegistro_sep, tupla):
    novachave = novoRegistro_sep[0]
    rrn = len(tupla)
    tupla.append(f"{novachave}|{rrn}")
    OrdenaTupla(tupla, 0, len(tupla)-1)

def insereArquivo(novoRegistro):
    with open(entrada, 'a') as output:
        output.write("\n"+novoRegistro)
    with open(entrada2, 'a') as output:
        novoRegistro = organizaLinha(novoRegistro, tamRegs)
        output.write("\n"+novoRegistro)

def insercao_de_registro(tupla, tamRegs):
    novoRegistro = str(input("Qual o novo registro que deseja inserir:"))
    novoRegistro_sep = novoRegistro.split(",")
    verificaRegistro = pesquisa_de_registro(tupla, tamRegs, novoRegistro_sep[0], 1)
    if verificaRegistro == 1:
        print("O registro já existe\n")
    else:
        insereTupla(novoRegistro_sep, tupla)
        insereArquivo(novoRegistro)
        print("Registro inserido\n")
#-----------------------------------------------------------------------------
#função principal
#-----------------------------------------------------------------------------
if __name__ == '__main__':
    #abre o arquivo e retorna o vetor de tuplas, os registros e o tamanho dos registros
    tupla, regs, tamRegs = abreArquivo()
    OrdenaTupla(tupla, 0, len(tupla) -1)    #ordena as tuplas para busca binaria

    menu = 1
    while menu != 0:
        menu = int(input("O que deseja fazer:\n1- Pesquisar\n2- Inserir\n0- Sair\n"))
        if menu == 1:       #pesquisa de registro
            anime = str(input("Qual anime deseja buscar: "))
            chave = pesquisa_de_registro(tupla, tamRegs, anime, 0)
            if chave == -1:
                print('O registro não foi encontrado\n')
        if menu == 2:       #inserção de registro
            insercao_de_registro(tupla, tamRegs)
        if menu == 0:
            print("Programa finalizado")
            exit(0)
        if menu != 1 and menu != 2:
            print("Valor inválido\nTente novamente\n")