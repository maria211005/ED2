import sys

entrada = ''
#caso não tenha a quantidade de argumentos válida para execução do código
if(len(sys.argv) != 3):
    print("Quantidade de argumentos inválida. Tente novamente")
    exit(1)
else:
    entrada = sys.argv[1]

#PESQUISA
#1) Procurar a chave na tabela de índices
#--> busca binária
#--> se achou ---> (chave, RRN)
#--> calcular offset
#--> leitura usando o RRN
#--> retorna registro para o usuário

#INSERÇÃO
#1) gerar una chave para o novo registro
#2) realizar uma pesquisa (chamar a função anterior)
#--> verifica se o novo registro ja existe (tem que retornar vazio)
#3) leitura do cabeçalho (last)
#--> se for last == -1:
#    RRN + 1
#    adicionar o registro no fim do arquivo 
#    adicionar na tabela de índices (chave, RRN)
#    ordenar a tabela de índices

def abreArquivo():
    with open(entrada, "r+") as file:
        file.seek(len(file.readline()))
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

        file.seek(0)
        file.seek(len(file.readline()))
        for linha in registros:
            linha = linha.strip("\n")
            if len(linha) < maxRegistro:            #verifica o tamanho da linha pra inserir caracteres especiais ou não
                dif = maxRegistro - len(linha) -1
                linha = linha + '*' * dif + '\n'
            else:                                   #caso for a maior linha
                linha = linha + '\n'
            file.write(linha)
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
    
if __name__ == '__main__':
    tupla, regs, tamRegs = abreArquivo()
    OrdenaTupla(tupla, 0, len(tupla) -1)

    menu = 1
    while menu != 0:
        menu = int(input("O que deseja fazer:\n1- Pesquisar\n2- Inserir\n0- Sair\n"))
        if menu == 1:
            anime = str(input("Qual anime deseja buscar: "))
            chaveEncontrada = BuscaBinaria(tupla, anime)
            if chaveEncontrada == 'O registro não foi encontrado\n':
                print(chaveEncontrada)
            else:
                buscaRegistro(entrada, tamRegs, chaveEncontrada)
        #if menu == 2:
            #inserir registro
        if menu == 0:
            print("Programa finalizado")
            exit(0)
        if menu != 1 and menu != 2:
            print("Valor inválido\nTente novamente\n")