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

with open(entrada, 'r') as arq:
    header = arq.readline()
    arquivo = arq.readlines()

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
            arquivo[i] = arquivo[i] + "|" + "*"*(maxRegistro-len(arquivo[i])) + "\n"
        else:
            arquivo[i] = arquivo[i] + "\n"

with open(consulta, 'r') as query:
    condicao = query.readline().strip("\n")
    valor = query.readline()

    if '&' in condicao or '||' in condicao:
        print("consulta booleana")
    else:
        print("consulta simples")

with open(saida, 'w') as output:
    output.write(header)
    for i in range (len(arquivo)):
        output.write(arquivo[i])
