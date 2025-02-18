import sys, csv, os

#caso não tenha a quantidade de argumentos válida para execução do código
if(len(sys.argv) != 4):
    if(len(sys.argv) < 4):
        print("Poucos argumentos. Tente novamente")
    else:
        print("Muitos argumentos. Tente novamente")
    exit(1)
else:
    entrada = sys.argv[1]
    consulta = sys.argv[2]
    saida = sys.argv[3]

    #verifica a existência dos arquivos de entrada
    if not (os.path.isfile(entrada) and os.path.isfile(consulta)):
        print("Arquivo inexistente")
        exit(1)
        
#-----------------------------------------------------------------------------------
#recebe o arquivo de entrada com todos os registros e retorna os mesmos registros em um vetor
def recebeRegistro():
    with open(entrada, 'r') as arq:
        arquivo = arq.readlines()
    return arquivo
#----------------------------------------------------------------------------------------
#recebe o arquivo com os registros organizados em tuplas e monta as tuplas de indice primário e secundário 
def montaTupla(reader):
    tuplaPrimaria = []
    tuplaSecundaria = []

    RRN = 0
    #a tupla inicial é a tupla com os nomes das colunas
    tuplaSecundaria.append(("id", "name", "album", "artists", "track_number", "disc_number", "explicit", "key", "mode", "year"))
    
    #verifica linha por linha do arquivo para registrar as tuplas primária e secundária e assim, os registros poderão ser manipulados como matriz
    for linha in reader:
        RRN+=1

        #a tupla primaria com cada chave e RRN
        tuplaPrimaria.append((linha["id"], str(RRN)))
        #a tupla secundária com a chave e todos as colunas passíveis de pesquisa
        tuplaSecundaria.append((linha["id"], linha["name"], linha["album"], linha["artists"], linha["track_number"], linha["disc_number"], linha["explicit"], linha["key"], linha["mode"], linha["year"]))
    
    return tuplaPrimaria, tuplaSecundaria
#-----------------------------------------------------------------------------------------------------
#realiza a consulta
def consultaTupla(arquivo, tuplaPrimaria, tuplaSecundaria):
    with open(consulta, 'r') as query, open(saida, 'w') as output:
        condicao = query.readline().strip("\n")     #armazena a primeira linha de condição
        valor = query.readline()                    #armazena os valores de cada condição para busca
        encontrou = 0
        colunaEscolhida = -1
        colunas = []
        linhasSelecionadas = []

        #para o caso de uma condição só
        if '&' not in condicao and '||' not in condicao:
            if condicao == 'artist_name':                                       #(gambiarra pra entrar um nome que não dá certo)
                colunaEscolhida = 3
            else:
                for i in range(len(tuplaSecundaria[0])):                        #verifica qual coluna da tupla condiz com a busca
                    if condicao in tuplaSecundaria[0][i]:
                        colunaEscolhida = i

            for i in range(len(tuplaSecundaria)):                               #verifica qual linha da coluna encontrada possui o valor que está sendo procurado
                if valor in tuplaSecundaria[i][colunaEscolhida]:    
                    encontrou+= 1                                               #incrementa a variável de conferência
                    for j in range(len(tuplaPrimaria)):                         #caso encontrar, verifica qual chave da tupla primária bate com a chave encontrada
                        if tuplaSecundaria[i][0] == tuplaPrimaria[j][0]:
                            output.write(arquivo[int(tuplaPrimaria[j][1])])     #escreve o registro encontrado no arquivo de saída

        #para o caso de mais de uma condicao com &
        if '&' in condicao and '||' not in condicao:
            condicao = condicao.split(" & ")
            valor = valor.split(", ")

            for k in range(len(condicao)):                                      #verifica quais colunas está procurando
                if 'artist_name' == condicao[k]:                                #(gambiarra pra entrar um nome que não dá certo)
                    condicao[k] = "artists"
                for i in range(len(tuplaSecundaria[0])):
                    if condicao[k] in tuplaSecundaria[0][i]:
                        colunas.append(i)                                       #armazena as colunas que serão verificadas

            for j in range(len(tuplaSecundaria)):                               #verifica quais linhas atendem à primeira coluna
                if valor[0] in tuplaSecundaria[j][colunas[0]]:
                    linhasSelecionadas.append(j)

            for k in range(1, len(valor)):                                      #a partir da primeira condição, verifica quais linhas atendem às outras condições
                tamanho = len(linhasSelecionadas)
                for i in range(tamanho):
                    #caso o valor da outra condição procurada não estiver na linha determinada, invalida essa linha
                    if (valor[k] not in tuplaSecundaria[linhasSelecionadas[i]][colunas[k]]): 
                        linhasSelecionadas[i] = -1

            for i in range(len(linhasSelecionadas)):
                if linhasSelecionadas[i] != -1:                                 #verifica quais linhas não foram invalidadas, logo são as que os dados bateram com a busca
                    encontrou+= 1
                    for j in range(len(tuplaPrimaria)):
                        #procura a chave na tupla primaria que bater coma chave encontrada
                        if tuplaSecundaria[linhasSelecionadas[i]][0] == tuplaPrimaria[j][0]:    
                            output.write(arquivo[int(tuplaPrimaria[j][1])]) #escreve o resultado no arquivo de saída

        #para o caso de mais de uma condicao com ||
        if '&' not in condicao and '||' in condicao:
            condicao = condicao.split(" || ")
            valor = valor.split(", ")

            for k in range(len(condicao)):                                          #verifica quais colunas está procurando
                if 'artist_name' == condicao[k]:                                    #(gambiarra pra entrar um nome que não dá certo)
                    condicao[k] = "artists"
                for i in range(len(tuplaSecundaria[0])):
                    if condicao[k] in tuplaSecundaria[0][i]:
                        colunas.append(i)                                           #armazena as colunas que está buscando
            
            for c in range(len(colunas)):
                for i in range(len(tuplaSecundaria)):                               #caso o valor seja encontrado, pode ser escrito no arquivo
                    if valor[c] in tuplaSecundaria[i][colunas[c]]:                  
                        encontrou+= 1
                        for j in range(len(tuplaPrimaria)):                         #procura a chave na tupla primaria que bater coma chave encontrada
                            if tuplaSecundaria[i][0] == tuplaPrimaria[j][0]:    
                                output.write(arquivo[int(tuplaPrimaria[j][1])])     #escreve o resultado no arquivo de saída
        
        #para o caso de mais de uma condicao com & e ||
        if '&' in condicao and '||' in condicao:
            condicao = condicao.split(" || ")                                       #para || é necessário atribuir as duas condições, por isso é splitado no || primeiro
            valor = valor.split(", ", len(condicao) -1)
    
            for c in range(len(condicao)):                                      
                if '&' in condicao[c]:                                              #verifica se existe & dentro das condições separadas, já que os || já foram separados
                    condicao[c] = condicao[c].split(" & ")
                    valor[c] = valor[c].split(", ")
                    
                    for k in range(len(condicao[c])):                               #verifica quais colunas está procurando
                        if 'artist_name' == condicao[c][k]:                         #(gambiarra pra entrar um nome que não dá certo)
                            condicao[c][k] = "artists"
                        for i in range(len(tuplaSecundaria[0])):
                            if condicao[c][k] in tuplaSecundaria[0][i]:
                                colunas.append(i)                                   #armazena as colunas que está buscando
                    
                    for j in range(len(tuplaSecundaria)):                           #verifica quais linhas atendem à primeira condição
                        if valor[c][0] in tuplaSecundaria[j][colunas[0]]:
                            linhasSelecionadas.append(j)                            #armazena as linhas encontradas
                    
                    for k in range(1, len(valor[c])):                               #a partir da primeira condição, verifica quais linhas atendem às outras condições
                        tamanho = len(linhasSelecionadas)
                        for i in range(tamanho):
                            #caso o valor procurado não estiver na linha determinada, invalida essa linha
                            if (valor[c][k] not in tuplaSecundaria[linhasSelecionadas[i]][colunas[k]]): 
                                linhasSelecionadas[i] = -1

                    for i in range(len(linhasSelecionadas)):                        #verifica quais linhas não foram invalidadas, logo são as que os dados bateram com a busca
                        if linhasSelecionadas[i] != -1:
                            encontrou+= 1
                            for j in range(len(tuplaPrimaria)):
                                if tuplaSecundaria[linhasSelecionadas[i]][0] == tuplaPrimaria[j][0]:
                                    output.write(arquivo[int(tuplaPrimaria[j][1])]) #escreve o resultado no arquivo de saída
                #caso a condição separada for só a palavra sozinha
                else:
                    if condicao[c] == 'artist_name':                                #(gambiarra pra entrar um nome que não dá certo)
                        colunaEscolhida = 3
                    else:
                        for i in range(len(tuplaSecundaria[0])):                    #verifica qual coluna bate com a condição procurada
                            if condicao[c] in tuplaSecundaria[0][i]:
                                colunaEscolhida = i

                    for i in range(len(tuplaSecundaria)):                           #procura em cada linha o valor desejado
                        if valor[c] in tuplaSecundaria[i][colunaEscolhida]:
                            encontrou+= 1
                            for j in range(len(tuplaPrimaria)):
                                if tuplaSecundaria[i][0] == tuplaPrimaria[j][0]:    #caso encontre o valor, procura a chave na tupla primária que bate com a chave encontrada
                                    output.write(arquivo[int(tuplaPrimaria[j][1])]) #escreve o resultado no arquivo de saída
        
        #caso nada tenha sido encontrado
        if encontrou == 0:
            print("Nenhum resultado foi encontrado")
#---------------------------------------------------------------------------------------
#recebe o arquivo de consulta e guarda os valores desse arquivo para realizar a consulta nos registros
def verificaConsulta():
    with open(consulta, 'r') as query:
        condicao = query.readline().strip("\n")
        valor = query.readline()

        if condicao == " " and valor == "":                                         #caso a consulta e os valores estiverem vazios
            print("Arquivo vazio")
            return False
        if condicao == "" or valor == "":                                           #caso a consulta ou os valores estiverem vazios
            print("Arquivo inválido para consulta")
            return False
        else:
            return True                                                             #caso estiver tudo certo com o arquivo de consulta
#---------------------------------------------------------------------------------------
#função principal
if __name__ == '__main__':
    if verificaConsulta():                                                          #caso a verificação for True, poderá começar a análise
        with open(entrada, 'r') as file:
            reader = csv.DictReader(file)                                           #recebe o registro em forma de dictionary para colocar legendas nos vetores
            arqRegistros = recebeRegistro()                                         #recebe o registro em forma de vetor
            
            primaria, secundaria = montaTupla(reader)                               #recebe as tuplas de consulta
            consultaTupla(arqRegistros, primaria, secundaria)                       #realiza a consulta em si