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

entrada2 = "animes2.txt"
#INSERÇÃO
#1) gerar una chave para o novo registro
#2) realizar uma pesquisa (chamar a função anterior)
#--> verifica se o novo registro ja existe (tem que retornar vazio)
#3) leitura do cabeçalho (last)
#--> se for last == -1:         (amiga, o professor falou que não precisa fazer de reuso)
#    RRN + 1
#    adicionar o registro no fim do arquivo 
#    adicionar na tabela de índices (chave, RRN)
#    ordenar a tabela de índices

#-----------------------------------------------------------------------------
#funções de abertura e organização
#-----------------------------------------------------------------------------
def abreArquivo():
    with open(entrada, "r+") as file:
        header = file.readline()
        registros = file.readlines()

        tupla = []
        offset = 0
        tam = []
        for linha in registros:
            tam.append(len(linha))
            linha_sep = linha.split(",")
            chave = linha_sep[0]
            tupla.append(f"{chave}|{offset}")
            offset += 1

        maxRegistro = tam[0]
        for i in range(len(tam)-1):
            if tam[i] > maxRegistro:
                maxRegistro = tam[i]

    with open(entrada2, "w") as output:
        output.write(header)
        for linha in registros:
            linha = linha.strip("\n")
            linha = linha.replace(",","|")
            if len(linha) < maxRegistro:            #verifica o tamanho da linha pra inserir caracteres especiais ou não
                dif = maxRegistro - len(linha) -1
                linha = linha + '*' * dif + '\n'
            else:                                   #caso for a maior linha
                linha = linha + '\n'
            output.write(linha)
    return tupla, registros, maxRegistro

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

def OrdenaTupla(tupla, inicio, fim):
    if(inicio < fim):
        pivo = ParticionaTupla(tupla, inicio, fim) 
        OrdenaTupla(tupla, inicio, pivo-1)
        OrdenaTupla(tupla, pivo+1, fim)
#-----------------------------------------------------------------------------
#funções de pesquisa
#-----------------------------------------------------------------------------
def BuscaBinaria(tupla, chave):
    inicio = 0
    fim = len(tupla) - 1
    while(inicio <= fim):
        meio = (inicio + fim) // 2 
        chave_reg = tupla[meio]
        chave_reg = chave_reg.split("|")
        if chave in chave_reg[0]: 
           return chave_reg

        if chave_reg[0] > chave:
           fim = meio - 1 

        else:
           inicio = meio + 1
    
    if inicio > fim:
        return "O registro não foi encontrado\n"
    
def buscaRegistro(arqEntrada, maxRegistro, chave):
    rrn = int(chave[1])

    with open(arqEntrada, 'r') as file:
        file.seek(len(file.readline()) + rrn*maxRegistro)
        print("Registro Encontrado\n" + file.readline())

def pesquisa_de_registro(tupla, tamRegs, anime, origem):
    chaveEncontrada = BuscaBinaria(tupla, anime)
    if chaveEncontrada == 'O registro não foi encontrado\n':
        return chaveEncontrada
    else:
        if origem == 0:
            buscaRegistro(entrada2, tamRegs, chaveEncontrada)
        else:
            return "O registro já existe\n"
#-----------------------------------------------------------------------------
#funções de inserção
#-----------------------------------------------------------------------------
def insercao_de_registro(tupla, tamRegs):
    novoRegistro = str(input("Qual o novo registro que deseja inserir:"))
    novoRegistro = novoRegistro.split("|")
    chave = pesquisa_de_registro(tupla, tamRegs, novoRegistro[0], 1)
    print(chave)
#-----------------------------------------------------------------------------
#função principal
#-----------------------------------------------------------------------------
if __name__ == '__main__':
    tupla, regs, tamRegs = abreArquivo()
    OrdenaTupla(tupla, 0, len(tupla) -1)

    menu = 1
    while menu != 0:
        menu = int(input("O que deseja fazer:\n1- Pesquisar\n2- Inserir\n0- Sair\n"))
        if menu == 1:
            anime = str(input("Qual anime deseja buscar: "))
            chave = pesquisa_de_registro(tupla, tamRegs, anime, 0)
            if chave == 'O registro não foi encontrado\n':
                print(chave)
        if menu == 2:
            insercao_de_registro(tupla, tamRegs)
        if menu == 0:
            print("Programa finalizado")
            exit(0)
        if menu != 1 and menu != 2:
            print("Valor inválido\nTente novamente\n")