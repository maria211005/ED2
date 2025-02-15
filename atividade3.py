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
        arq.seek(len(arq.readline()))
        arquivo = arq.readlines()

        #organizando o arquivo para alinhar os registros para procura
        tam = []
        maxRegistro = 0
        for i in range(len(arquivo)):
            arquivo[i] = arquivo[i].strip('\n')

            tam.append(len(arquivo[i]))

            if tam[i] > maxRegistro:
                maxRegistro = tam[i]

        for i in range (len(arquivo)):
            if len(arquivo[i]) < maxRegistro:
                arquivo[i] = arquivo[i] + "," + "*"*(maxRegistro-len(arquivo[i])-2) + "\n"
            else:
                arquivo[i] = arquivo[i] + "\n"
    return arquivo
#----------------------------------------------------------------------------------------
#recebe o arquivo com as condições de consulta e o registro que deseja procurar
def consultaRegistro(reader):
    with open(consulta, 'r') as query:
        condicao = query.readline().strip("\n")
        valor = query.readline()

        if '&' not in condicao and '||' not in condicao:
            print(condicao)

        if ('&' in condicao and '||' not in condicao) or ('&' not in condicao and '||' in condicao):
            condicao = condicao.split()
            print(condicao)
                
        if '&' in condicao and '||' in condicao:
            condicao = condicao.split()
            print(condicao)
#---------------------------------------------------------------------------------------
def montaTupla(reader):
    tuplaPrimaria = []
    tuplaName = []
    tuplaAlbum = []
    tuplaArtists = []
    tuplaTrack = []
    tuplaDisc = []
    tuplaExplict = []
    tuplaKey = []
    tuplaMode = []
    tuplaYear = []

    i = 0
    for linha in reader:
        i+=1
        tuplaPrimaria.append((linha["id"], str(i)))
        tuplaName.append((linha["id"], linha["name"]))
        tuplaAlbum.append((linha["id"], linha["album"]))
        tuplaArtists.append((linha["id"], linha["artists"]))
        tuplaTrack.append((linha["id"], linha["track_number"]))
        tuplaDisc.append((linha["id"], linha["disc_number"]))
        tuplaExplict.append((linha["id"], linha["explicit"]))
        tuplaKey.append((linha["id"], linha["key"]))
        tuplaMode.append((linha["id"], linha["mode"]))
        tuplaYear.append((linha["id"], linha["year"]))

    #name, album, artists, track_number, disc_number, explicit, key, mode, year    
    print(tuplaYear)
#---------------------------------------------------------------------------------------
if __name__ == '__main__':
    with open(entrada, 'r') as file:
        reader = csv.DictReader(file)
        arqRegistros = recebeRegistro()

        montaTupla(reader)
    #tem que fazer as tuplas pra mandar na pesquisa
        #consultaRegistro(reader)