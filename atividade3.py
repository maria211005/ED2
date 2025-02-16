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

    if not (os.path.isfile(entrada) and os.path.isfile(consulta)):
        print("Arquivo inexistente")
        exit(1)
        
#-----------------------------------------------------------------------------------
#recebe o arquivo de entrada com todos os registros e organiza-os
def recebeRegistro():
    with open(entrada, 'r') as arq:
        arquivo = arq.readlines()
    return arquivo
#----------------------------------------------------------------------------------------
#recebe o arquivo com as condições de consulta e o registro que deseja procurar
def montaTupla(reader):
    tuplaPrimaria = []
    tuplaSecundaria = []

    RRN = 0
    tuplaSecundaria.append(("id", "name", "album", "artists", "track_number", "disc_number", "explicit", "key", "mode", "year"))
    
    for linha in reader:
        RRN+=1

        tuplaPrimaria.append((linha["id"], str(RRN)))
        tuplaSecundaria.append((linha["id"], linha["name"], linha["album"], linha["artists"], linha["track_number"], linha["disc_number"], linha["explicit"], linha["key"], linha["mode"], linha["year"]))
    
    return tuplaPrimaria, tuplaSecundaria
#-----------------------------------------------------------------------------------------------------
def consultaTupla(arquivo, tuplaPrimaria, tuplaSecundaria):
    with open(consulta, 'r') as query, open(saida, 'w') as output:
        condicao = query.readline().strip("\n")
        valor = query.readline()
        encontrou = 0
        colunaEscolhida = -1
        colunas = []
        linhasSelecionadas = []

        #para o caso de uma condição só
        if '&' not in condicao and '||' not in condicao:
            for i in range(len(tuplaSecundaria[0])):
                if condicao in tuplaSecundaria[0][i]:
                    colunaEscolhida = i

            for i in range(len(tuplaSecundaria)):
                if valor in tuplaSecundaria[i][colunaEscolhida]:
                    encontrou+= 1
                    for j in range(len(tuplaPrimaria)):
                        if tuplaSecundaria[i][0] == tuplaPrimaria[j][0]:
                            output.write(arquivo[int(tuplaPrimaria[j][1])])

        #para o caso de mais de uma condicao com &
        if '&' in condicao and '||' not in condicao:
            condicao = condicao.split(" & ")
            valor = valor.split(", ")

            #verifica quais colunas está procurando
            for k in range(len(condicao)):
                for i in range(len(tuplaSecundaria[0])):
                    if condicao[k] in tuplaSecundaria[0][i]:
                        colunas.append(i)
            
            #verifica quais linhas atendem à primeira condição
            for j in range(len(tuplaSecundaria)):
                if valor[0] in tuplaSecundaria[j][colunas[0]]:
                    linhasSelecionadas.append(j)

            #a partir da primeira condição, verifica quais linhas atendem às outras condições
            for k in range(1, len(valor)):
                tamanho = len(linhasSelecionadas)
                for i in range(tamanho):
                    #caso o valor procurado não estiver na linha determinada, invalida essa linha
                    if (valor[k] not in tuplaSecundaria[linhasSelecionadas[i]][colunas[k]]): 
                        linhasSelecionadas[i] = -1

            for i in range(len(linhasSelecionadas)):
                if linhasSelecionadas[i] != -1:
                    encontrou+= 1
                    for j in range(len(tuplaPrimaria)):
                        if tuplaSecundaria[linhasSelecionadas[i]][0] == tuplaPrimaria[j][0]:
                            output.write(arquivo[int(tuplaPrimaria[j][1])])

        #para o caso de mais de uma condicao com ||
        if '&' not in condicao and '||' in condicao:
            condicao = condicao.split(" || ")
            valor = valor.split(", ")

            #verifica quais colunas está procurando
            for k in range(len(condicao)):
                for i in range(len(tuplaSecundaria[0])):
                    if condicao[k] in tuplaSecundaria[0][i]:
                        colunas.append(i)
            
            for c in range(len(colunas)):
                for i in range(len(tuplaSecundaria)):
                    if valor[c] in tuplaSecundaria[i][colunas[c]]:
                        encontrou+= 1
                        for j in range(len(tuplaPrimaria)):
                            if tuplaSecundaria[i][0] == tuplaPrimaria[j][0]:
                                output.write(arquivo[int(tuplaPrimaria[j][1])])
        
        #para o caso de mais de uma condicao com & e ||
        if '&' in condicao and '||' in condicao:
            condicao = condicao.split(" || ")
            valor = valor.split(", ", len(condicao) -1)
    
            #para || é necessário atribuir as duas condições, por isso é splitado no || primeiro
            for c in range(len(condicao)):
                if '&' in condicao[c]:
                    condicao[c] = condicao[c].split(" & ")
                    valor[c] = valor[c].split(", ")
                    
                    #verifica quais colunas está procurando
                    for k in range(len(condicao[c])):
                        for i in range(len(tuplaSecundaria[0])):
                            if condicao[c][k] in tuplaSecundaria[0][i]:
                                colunas.append(i)
                    
                    #verifica quais linhas atendem à primeira condição
                    for j in range(len(tuplaSecundaria)):
                        if valor[c][0] in tuplaSecundaria[j][colunas[0]]:
                            linhasSelecionadas.append(j)

                    #a partir da primeira condição, verifica quais linhas atendem às outras condições
                    for k in range(1, len(valor[c])):
                        tamanho = len(linhasSelecionadas)
                        for i in range(tamanho):
                            #caso o valor procurado não estiver na linha determinada, invalida essa linha
                            if (valor[c][k] not in tuplaSecundaria[linhasSelecionadas[i]][colunas[k]]): 
                                linhasSelecionadas[i] = -1

                    for i in range(len(linhasSelecionadas)):
                        if linhasSelecionadas[i] != -1:
                            encontrou+= 1
                            for j in range(len(tuplaPrimaria)):
                                if tuplaSecundaria[linhasSelecionadas[i]][0] == tuplaPrimaria[j][0]:
                                    output.write(arquivo[int(tuplaPrimaria[j][1])])
                else:
                    for i in range(len(tuplaSecundaria[0])):
                        if condicao[c] in tuplaSecundaria[0][i]:
                            colunaEscolhida = i

                    for i in range(len(tuplaSecundaria)):
                        if valor[c] in tuplaSecundaria[i][colunaEscolhida]:
                            encontrou+= 1
                            for j in range(len(tuplaPrimaria)):
                                if tuplaSecundaria[i][0] == tuplaPrimaria[j][0]:
                                    output.write(arquivo[int(tuplaPrimaria[j][1])])
        
        #caso nada tenha sido encontrado
        if encontrou == 0:
            print("Nenhum resultado foi encontrado")
#---------------------------------------------------------------------------------------
def verificaConsulta():
    with open(consulta, 'r') as query:
        condicao = query.readline().strip("\n")
        valor = query.readline()
        if condicao == " " and valor == "":
            print("Arquivo vazio")
            return False
        if condicao == "" or valor == "":
            print("Arquivo inválido para consulta")
            return False
        else:
            return True
#---------------------------------------------------------------------------------------
if __name__ == '__main__':
    if verificaConsulta():
        with open(entrada, 'r') as file:
            reader = csv.DictReader(file)
            arqRegistros = recebeRegistro()
            
            primaria, secundaria = montaTupla(reader)
            consultaTupla(arqRegistros, primaria, secundaria)
