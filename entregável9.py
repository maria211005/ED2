import sys
entrada = ''
#receber os parâmetros via linha de comando
if(len(sys.argv) != 3):
	print("Quantidade de argumentos inválida. Tente novamente")
else:
	entrada = sys.argv[1]

'''
def Remoção de registro com Reuso( )
    encontrar o registro que será invalidado usando o RRN

    calcular o deslocamento em relação ao inicio do arquivo, multiplicando o RRN por tamanho do registro (offset)

    fseek no offset 

    ler o cabeçalho e descobrir o valor da variável last

    o registro que é invalidado recebe * seguido do id do registro que é armazenado no cabeçalho (last)

    atualizar o last, ele recebe o valor do registro que foi invalidado
        - escrever novamente o cabeçalho atualizando o valor da variável
        
        
def Inserção de registro com reuso( ) 
    descobrir se é possível fazer reuso de posições
        ler o cabeçalho e verificar o valor do last
        se last = -1, não tem valor para reuso 
            append no fim do arquivo
        senao, há posições para ser usadas 
            atualizar o valor do last
            no começo da linha indexada pelo last há (* id)
            last = id
            sobrescreve o valor da linha
            
        incrementa a quantidade de registros validos

'''    
def removeRegistro(registro, tamRegistro):
    RRN = int(input("qual o indice que deseja remover?")) 
#def insereNovoRegistro():

def escritaTamanhoFixo(registros):
    with open('saida.txt', 'w') as f:
        TamReg = 0
        tam = []
        
        for linha in registros:
            tam.append(len(linha))
            
        TamReg = tam[0]
        for i in range(len(tam)):
            if tam[i] > TamReg:
                TamReg = tam[i]
        i = 0
        for linha in registros:
            linha = linha.strip('\n')
            linha = linha.replace(",", "|")
        
            if len(linha) < TamReg:
                dif = TamReg - len(linha) -1
                linha = linha + '*' * dif + '\n'
            else:
                linha = linha + '\n'
            
            f.write(linha)
    return TamReg, f.name

if __name__ == "__main__":
    with open(entrada, 'r') as f:
        registros = f.readlines()
        if registros == '':
            print('O arquivo está vazio\n')
            exit(1)
        else:
            registros.pop(0)

    tamanhoRegistro, arqLenght = escritaTamanhoFixo(registros)
    print(tamanhoRegistro, arqLenght)
    
    
    #removeRegistro(registros, tamanhoRegistro)