def readRecordByRRN(registros, RRN): #passar o registros pra ca
    with open("grepRRN.txt", 'r+') as output:
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
        
        
        
if __name__ == "__main__":
    with open("teste.txt", "r") as f:
        registros = f.readlines()
        if registros == '':
            print('O arquivo está vazio\n')
            exit(1)
        else:
            f.close()
            
    resultado = readRecordByRRN(registros, 3)
    print(resultado)