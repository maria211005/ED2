#atividade de indice secundário
with open("tracks_menor.csv", 'r') as arq:
    header = arq.readline()
    arquivo = arq.readlines()

    print(header)
    tam = []
    maxRegistro = 0
    for i in range(len(arquivo)):
        arquivo[i] = arquivo[i].strip('\n')
        tam.append(len(arquivo[i]))

        if tam[i] > maxRegistro:
            maxRegistro = tam[i]
    
    for i in range (len(arquivo)):
        arquivo[i] = arquivo[i].replace(",","|")
        if len(arquivo[i]) < maxRegistro:
            arquivo[i] = arquivo[i] + "*"*(maxRegistro-len(arquivo[i]))
            print(arquivo[i])