with open("animes.csv", 'r') as f:
    registros = f.readlines()
    if registros == '':
        print('O arquivo está vazio\n')
        exit(1)
    else:
        f.close()

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