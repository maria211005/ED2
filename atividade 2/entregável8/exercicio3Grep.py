def escreveOutput(registros, saida): #passar o registros pra ca
    with open(saida, 'w+') as output:
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
        
def readRecordByRRN(saida, RRN):
    with open(saida, "r") as f:
        registros = f.readlines()
        if registros == '':
            print('O arquivo está vazio\n')
            exit(1)
        else:
            f.close()
        
        return registros[RRN]
            
if __name__ == "__main__":
    with open("teste.txt", "r") as f:
        registros = f.readlines()
        if registros == '':
            print('O arquivo está vazio\n')
            exit(1)
        #else:
            #registros.pop(0)
            
    escreveOutput(registros, "RRN.txt")
    
    valorRRN = int(input("Digite a posição que deseja encontrar o anime:"))
    resultado = readRecordByRRN("RRN.txt", valorRRN)
    print(f"Encontrado:\n{resultado}")