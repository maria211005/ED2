#METODO 1 - TAMANHO FIXO COM CAMPOS VARIADOS
def AbreArquivo(): 
    with open("animes.csv", 'r') as f: #da pra tirar da função 1 isso aqui 
        registros = f.readlines()
        if registros == '':
            print('O arquivo est� vazio\n')
            exit(1)
        else:
            f.close()
    return registros 
    

def escritaTamanhoFixo(registros): #passar o registros pra ca 
    tamanhos = []
    for linha in range(len(registros)): #lendo as linhas e pegando o tamanho de cada uma 
        contaBytes = 0
        while linha.seek(1) != '\n': 
            contaBytes = contaBytes+1 #contando o tamanho de cada linha
        tamanhos[linha] = contaBytes

    maiorValor = tamanhos[0]

    for i in range(len(tamanhos)): #acha a linha com maior valor 
        if(tamanhos[i] > maiorValor):
            maiorValor = tamanhos[i]

    TamReg = maiorValor

    with open('metodo1.txt', 'w') as output:
        for linha in registros:
            str.replace(",","|")
        
            if len(linha) < TamReg:
                newStr = linha + '*'*(TamReg - len(linha))
            else:
                newStr = linha
            
            output.write(newStr)

#--------------------------------------------------------
#METODO 2 - QTDD FIXA DE CAMPOS 
def escritaQtdeCampos(registros):
    #41 campos formam um registro ---> fazer um contador de pipe 
    #a cada 41 campos, concatenar 

    with open('metodo2.txt', 'w') as output:
        for linha in range(len(registros)): #percorrendo o arquivo todo 
            newStr = linha
            output.write(newStr[:len(newStr-2)]) 
#----------------------------------------------------------------
#METODO 3 - QTTD BYTES
def escritaQtdeBytes(registros):
    with open('metodo3.txt', 'w') as output:
        contadorBytes = 0
        for linha in range(len(registros)): #percorrendo o arquivo todo 
            newStr = linha
            while (linha.seek(1) != '\n'):
                contadorBytes = contadorBytes + 1 
            output.write(contadorBytes + newStr[:len(newStr-2)])

#------------------------------------------------------------
#METODO 4 - ARQUIVO DE INDEX 
def escritaArqIndex(registros):
    contadorBytes = 0
    with open('metodo4.txt', 'w') as output:
        for linha in range(len(registros)):
                    


if __name__ == "__main__":
    registro = AbreArquivo()
    escritaTamanhoFixo(registro)
    escritaQtdeCampos(registro)
    escritaQtdeBytes(registro)
