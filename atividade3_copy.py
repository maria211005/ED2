import sys, csv

entrada = ''
saida = ''
#caso não tenha a quantidade de argumentos válida para execução do código
if(len(sys.argv) != 4):
    print("Quantidade de argumentos inválida. Tente novamente")
    exit(1)
else:
    entrada = sys.argv[1]
    consulta = sys.argv[2]
    saida = sys.argv[3]
#-----------------------------------------------------------------------------------
#recebe o arquivo de entrada com todos os registros e organiza-os
def recebeRegistro():
    with open(entrada, 'r') as arq:
        arquivo = arq.readlines()
    return arquivo
#----------------------------------------------------------------------------------------
#recebe o arquivo com as condições de consulta e o registro que deseja procurar
def montaTupla(arquivo, reader):
    tuplaPrimaria = []
    tuplaSecundaria = []

    RRN = 0
    tuplaSecundaria.append(("id", "name", "album", "artists", "track_number", "disc_number", "explicit", "key", "mode", "year"))
    
    for linha in reader:
        RRN+=1

        tuplaPrimaria.append((linha["id"], str(RRN)))
        tuplaSecundaria.append((linha["id"], linha["name"], linha["album"], linha["artists"], linha["track_number"], linha["disc_number"], linha["explicit"], linha["key"], linha["mode"], linha["year"]))

    with open(consulta, 'r') as query, open(saida, 'w') as output:
        condicao = query.readline().strip("\n")
        valor = query.readline()

        if '&' not in condicao and '||' not in condicao:
            for i in range(len(tuplaSecundaria[0])):
                if condicao == tuplaSecundaria[0][i]:
                    colunaEscolhida = i
            
            for i in range(len(tuplaSecundaria)):
                if valor in tuplaSecundaria[i][colunaEscolhida]:
                    for j in range(len(tuplaPrimaria)):
                        if tuplaSecundaria[i][0] == tuplaPrimaria[j][0]:
                            output.write(arquivo[int(tuplaPrimaria[j][1])])

        if '&' in condicao and '||' not in condicao:
            condicao = condicao.split(" & ")
            valor = valor.split(", ")

            colunas = []
            linhasSelecionadas = []
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
                    for j in range(len(tuplaPrimaria)):
                        if tuplaSecundaria[linhasSelecionadas[i]][0] == tuplaPrimaria[j][0]:
                            output.write(arquivo[int(tuplaPrimaria[j][1])])

        if '&' in condicao and '||' in condicao:
            condicao = condicao.split()

#---------------------------------------------------------------------------------------
if __name__ == '__main__':
    with open(entrada, 'r') as file:
        reader = csv.DictReader(file)
        arqRegistros = recebeRegistro()
        montaTupla(arqRegistros, reader)
    #tem que fazer as tuplas pra mandar na pesquisa