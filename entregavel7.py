import sys
import os

#METODO 1 - TAMANHO FIXO COM CAMPOS VARIADOS
def AbreArquivo(): 
    with open("animes.csv", 'r') as f: #da pra tirar da função 1 isso aqui 
        registros = f.readlines()
        if registros == '':
            print('O arquivo está vazio\n')
            exit(1)
        else:
            registros.pop(0)
            f.close()
    return registros 
#------------------------------------------------------------------    
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
                newStr = linha + '*' * dif + '\n'
            else:
                newStr = linha + '\n'
            
            output.write(newStr)
#--------------------------------------------------------
#METODO 2 - QTDD FIXA DE CAMPOS 
def escritaQtdeCampos(registros):
    with open('metodo2.txt', 'w') as output:
        for linha in registro: #percorrendo o arquivo todo 
            linha = linha.replace(",", "|")
            linha_concatenada = linha.strip('\n')
            output.write(linha_concatenada) 
#----------------------------------------------------------
#METODO 3 - QTTD BYTES
def escritaQtdeBytes(registros):
    with open('metodo3.txt', 'w') as output:
        for linha in registros: #percorrendo o arquivo todo 
            linha = linha.replace(",","|")
            linha = linha.strip('\n')
            output.write(str(len(linha)) + linha)
#------------------------------------------------------------
#METODO 4 - ARQUIVO DE INDEX 
def escritaArqIndex(registros):
    somador = 0
    with open('metodo4.txt', 'w') as output:
        for linha in registros:
            output.write(str(somador) + '\n')
            somador += len(linha)
#-------------------------------------------------------------
#METODO 5 - DELIMITADORES 
def escritaDelimitadores(registros):
    with open('metodo5.txt', 'w') as output:
        for linha in registros:
            linha = linha.replace(",","|")
            linha = linha.strip('\n')
            output.write(linha + '#')
#-------------------------------------------------------------
#função principal
if __name__ == "__main__":
    registro = AbreArquivo()
    reg1 = registro
    reg2 = registro
    reg3 = registro
    reg4 = registro
    reg5 = registro

    escritaTamanhoFixo(reg1)
    escritaQtdeCampos(reg2)
    escritaQtdeBytes(reg3)
    escritaArqIndex(reg4)
    escritaDelimitadores(reg5)