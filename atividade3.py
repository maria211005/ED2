import sys, csv, re

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
        header = arq.readline()
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
    return arquivo, header
#----------------------------------------------------------------------------------------
#recebe o arquivo com as condições de consulta e o registro que deseja procurar
def consultaRegistro(reader):
    with open(consulta, 'r') as query:
        #name, album, artists, track_number, disc_number, explicit, key, mode, year
        condicao = query.readline().strip("\n")
        valor = query.readline()

        if '&' not in condicao and '||' not in condicao:
            i = 0
            '''
            encontrou = 0
            for linha in reader:
                i+=1
                if valor in linha[f"{condicao}"]:
                    print(i, linha[f"{condicao}"])
                    encontrou+=1
            
            if encontrou ==0:
                print("não encontramos o que deseja procurar")
        '''
            with open(saida, 'w') as output:
                for linha in reader:
                    i+=1
                    if valor in linha[f"{condicao}"]:
                        output.write(str(i) + " " + linha[f"{condicao}"] + "\n")

        else:
            re.split("[& ||]", condicao)
            print(condicao)
                

#---------------------------------------------------------------------------------------
#arquivo de saída com os registros pesquisados
'''
with open(saida, 'w') as output:
    for i in range (len(arquivo)):
        output.write(arquivo[i])
'''

if __name__ == '__main__':
    with open(entrada, 'r') as file:
        reader = csv.DictReader(file)
        arqRegistros, cabecalho = recebeRegistro()
    #tem que fazer as tuplas pra mandar na pesquisa
        consultaRegistro(reader)