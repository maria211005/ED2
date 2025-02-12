import sys

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
        header = arq.readline().split(',')
        arquivo = arq.readlines()

        #organizando o arquivo para alinhar os registros para procura
        tam = []
        maxRegistro = 0
        for i in range(len(arquivo)):
            arquivo[i] = arquivo[i].strip('\n')
            arquivo[i] = arquivo[i].replace(",","|")

            tam.append(len(arquivo[i]))

            if tam[i] > maxRegistro:
                maxRegistro = tam[i]

        for i in range (len(arquivo)):
            if len(arquivo[i]) < maxRegistro:
                arquivo[i] = arquivo[i] + "|" + "*"*(maxRegistro-len(arquivo[i])-2) + "\n"
            else:
                arquivo[i] = arquivo[i] + "\n"
        
    return arquivo, header
#----------------------------------------------------------------------------------------
#recebe o arquivo com as condições de consulta e o registro que deseja procurar
def consultaRegistro(arquivo, cabecalho):
    with open(consulta, 'r') as query:
        #name, album, artists, track_number, disc_number, explicit, key, mode, year
        condicao = query.readline().strip("\n")
        valor = query.readline()

        if '&' in condicao:
            print("consulta booleana com &")
        if '||' in condicao:
            print("consulta booleana com ||")
        else:
            for i in range(len(cabecalho)):
                if cabecalho[i] == condicao:
                    coluna = i
            #aqui não ta dando certo 
            for i in range(len(arquivo)):
                arquivo[i] = arquivo[i].split("|")
                print(arquivo[i][coluna])
#---------------------------------------------------------------------------------------
#arquivo de saída com os registros pesquisados
'''
with open(saida, 'w') as output:
    for i in range (len(arquivo)):
        output.write(arquivo[i])
'''

if __name__ == '__main__':
    arqRegistros, cabecalho = recebeRegistro()
    consultaRegistro(arqRegistros, cabecalho)