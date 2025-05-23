#METODO 1 - ESCRITA DE TAMANHO FIXO
def escritaTamanhoFixo(registros): #passar o registros pra ca    
    with open('metodo1.txt', 'w') as output:
        TamReg = 0
        tam = []
        
        for linha in registros:
            tam.append(len(linha))
            
        TamReg = tam[0]
        for i in range(len(tam)):
            if tam[i] > TamReg:
                TamReg = tam[i]
        
        for linha in registros:
            linha = linha.strip('\n')
            linha = linha.replace(",", "|")
        
            if len(linha) < TamReg:
                dif = TamReg - len(linha) -1
                linha = linha + '*' * dif + '\n'
            else:
                linha = linha + '\n'
            
            output.write(linha)
#--------------------------------------------------------
#METODO 2 - QTDD FIXA DE CAMPOS 
def escritaQtdeCampos(registros):
    with open('metodo2.txt', 'w') as output:
        for linha in registros: #percorrendo o arquivo todo 
            linha = linha.replace(",", "|")
            linha = linha.replace("\n","|")
            output.write(linha)
#----------------------------------------------------------
#METODO 3 - QTTD BYTES
def escritaQtdeBytes(registros):
    with open('metodo3.txt', 'w') as output:
        for linha in registros: #percorrendo o arquivo todo 
            tamanho = len(linha)
            linha = linha.replace(",","|")
            linha = linha.strip('\n')
            output.write(str(tamanho) + linha + "|")
#------------------------------------------------------------
#METODO 4 - ARQUIVO DE INDEX 
def escritaArqIndex(registros):
    somador = 0
    with open('metodo4.txt', 'w') as output:
        for linha in registros:
            output.write(str(somador) + '\n')
            somador += len(linha) + 1
#-------------------------------------------------------------
#METODO 5 - DELIMITADORES 
def escritaDelimitadores(registros):
    with open('metodo5.txt', 'w') as output:
        for linha in registros:
            linha = linha.replace(",","|")
            linha = linha.strip('\n')
            output.write(linha + "|#")
#-------------------------------------------------------------
#função principal
if __name__ == "__main__":
    with open("animesCompleto.txt", 'r') as f:
        registros = f.readlines()
        if registros == '':
            print('O arquivo está vazio\n')
            exit(1)
        else:
            registros.pop(0)
            
    reg1 = registros
    reg2 = registros
    reg3 = registros
    reg4 = registros
    reg5 = registros

    escritaTamanhoFixo(reg1)
    escritaQtdeCampos(reg2)
    escritaQtdeBytes(reg3)
    escritaArqIndex(reg4)
    escritaDelimitadores(reg5)