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
    with open(entrada, "r") as file:
        file.seek(len(file.readline()))
        registros = file.readlines()

        tupla = []
        offset = 0
        for linha in registros:
            linha_sep = linha.split(",")
            chave = linha_sep[0]
            tupla.append(f"{chave}, {offset}")
            offset += 1
    return tupla, registros

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

def escreveArquivoIndices(tupla):
    saida = "arqIndices.txt"
    with open(saida, "w") as indices:
        for i in range(len(tupla)):
            tupla[i] = tupla[i].split(",")
            tupla[i][1] = tupla[i][1].strip(" ")
            indices.write(tupla[i][0] + "|" + tupla[i][1] + "\n")
        
    return saida

def BuscaBinaria(tupla, chave, reg):
    inicio = 0
    fim = len(tupla) - 1
    while(inicio <= fim):
        meio = (inicio + fim) // 2 
        chave_reg = tupla[meio]
        if chave_reg == chave: 
           return True

        #if chave_reg < chave:
        #   fim = meio - 1 

        #else
        #   inicio = meio + 1 

if __name__ == '__main__':
    tupla, regs = abreArquivo()
    OrdenaTupla(tupla, 0, len(tupla) -1)
    arqIndice = escreveArquivoIndices(tupla)

    BuscaBinaria(tupla, "BLEACH", regs)    
