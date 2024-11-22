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
    TamReg = len(max(registros))
    with open('metodo1.txt', 'w') as output:
        for linha in registros:
            linha = linha.strip('\n')
            str.replace(",","|")
        
            if len(linha) < TamReg:
                newStr = linha + '*'*(TamReg - len(linha)-1) + '\n'
            else:
                newStr = linha
            
            output.write(newStr)
#--------------------------------------------------------
#METODO 2 - QTDD FIXA DE CAMPOS 
def escritaQtdeCampos(registros):
    with open('metodo2.txt', 'w') as output:
        for linha in range(len(registros)): #percorrendo o arquivo todo 
            str.replace(",", "|")
            newStr = linha
            output.write(newStr[:len(newStr)-1]) 
#----------------------------------------------------------
#METODO 3 - QTTD BYTES
def escritaQtdeBytes(registros):
    with open('metodo3.txt', 'w') as output:
        contadorBytes = 0
        for linha in range(len(registros)): #percorrendo o arquivo todo 
            str.replace(",","|")
            newStr = linha
            while (linha.seek(1) != '\n'):
                contadorBytes = contadorBytes + 1 
            output.write(contadorBytes + newStr[:len(newStr-1)])
#------------------------------------------------------------
#METODO 4 - ARQUIVO DE INDEX 
def escritaArqIndex(registros):
    somador = 0
    with open('metodo4.txt', 'w') as output:
        output.write(somador)
        for linha in range(len(registros)):
            linha = linha.strip('\n') #tirando \n de tudo
            while (linha.seek(1) != ''):
                somador = somador + 1
            if linha.seek(0) != None:
                valorPosicao = somador + 1
                output.write(valorPosicao + '')
#-------------------------------------------------------------
#METODO 5 - DELIMITADORES 
def escritaDelimitadores(registros):
    with open('metodo5.txt', 'w') as output:
        for linha in range(len(registros)):
            str.replace(",","|")
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