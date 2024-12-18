#só abri o arquivo pra dizer q fiz algo agora KKKKKKKKKKKKKKKKKKKKKKKKKKK

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
    with open("animes.txt", "r") as file:
        header = file.readline()
        registros = file.readlines()

        tupla = []
        offset = 0
        for linha in registros:
            linha_sep = linha.split(",")
            chave = linha_sep[0]
            tupla.append(f"{chave}, {offset}")
            tamLinha = len(linha)
            offset += tamLinha
    return tupla 

abreArquivo()

def ParticionaTupla(tupla, inicio, fim):
    esquerda = inicio 
    direita = fim
    pivo = tupla[inicio]

    while(esquerda < direita):
        while(tupla[esquerda] <= pivo and esquerda < fim):
            esquerda = esquerda + 1

    while(direita > esquerda):
        while(tupla[direita] >= pivo and direita > inicio):
            direita = direita - 1 

    if(esquerda < direita):
        tupla[esquerda], tupla[direita] = tupla[direita], tupla[esquerda] 

def OrdenaTupla(tupla, inicio, fim):
    if(inicio < fim):
        pivo = ParticionaTupla(tupla, inicio, fim) 
        OrdenaTupla(tupla, inicio, pivo-1)
        OrdenaTupla(tupla, pivo+1, fim)

