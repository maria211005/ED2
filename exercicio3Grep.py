def readRecordByRRN(registros, RRN): #passar o registros pra ca  
    with open("animes.csv", 'r') as f: #da pra tirar da função 1 isso aqui 
        registros = f.readlines()
        if registros == '':
            print('O arquivo está vazio\n')
            exit(1)
        else:
            registros.pop(0)
            f.close()

    TamReg = max(registros)
    with open("grepRRN.txt", 'w') as output:
        for linha in registros:
            linha = linha.strip('\n')
            str.replace(",","|")
        
            if len(linha) < TamReg:
                newStr = linha + '*'*(TamReg - len(linha)-1) + '\n'
            else:
                newStr = linha
            
            output.write(newStr)
    
    return output[RRN]
            
            
    