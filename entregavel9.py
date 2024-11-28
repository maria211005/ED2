import sys

entrada = ''
saida = ''
#receber os parâmetros via linha de comando
if(len(sys.argv) != 3):
    print("Quantidade de argumentos inválida. Tente novamente")
    exit(1)
else:
    entrada = sys.argv[1]
    saida = sys.argv[2]

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
def removeRegistro(arquivoSaida, tamHeader, tamRegistro):
    recebe = 1
    while recebe == 1:
        RRN = int(input("qual o indice que deseja remover?\n"))
        deslocamento = tamHeader + (RRN-1)*tamRegistro

        with open(arquivoSaida, 'r+') as output:
            output.seek(deslocamento)
            if output.read(1) == '*':
                print("Elemento já removido\nTente Novamente\n")
            else:
                output.seek(tamHeader -3)
                last = output.readline()
                last = last.strip('\n')
                output.seek(tamHeader -3)
                if RRN < 10:
                    output.write(str(RRN) + " ")  
                else:
                    output.write(str(RRN))

                output.seek(deslocamento)
                linha = output.readline()
                if int(last) < 0 or int(last) > 9:
                    linha = f"*{last}" + linha[2:-2]
                else:
                    linha = f"*{last}" + linha[2:-3]
                output.seek(deslocamento)
                output.write(linha)

                recebe = int(input("Anime Removido\nGostaria de remover mais algum anime?\n1- Sim\n0-Não\n"))
                if recebe == 0:
                    return 
    
#def insereNovoRegistro():

def escritaTamanhoFixo(registros):
    with open(saida, 'w') as output:
        registros[0] = registros[0].strip('\n') + ",last:-1\n"
        TamReg = 0
        tam = []
        
        for linha in registros:
            tam.append(len(linha))
        
        tamHeader = tam[0]
        TamReg = tam[1]
        for i in range(1, len(tam)):
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
            
            output.write(linha)
    return tamHeader, TamReg

if __name__ == "__main__":
    with open(entrada, 'r') as f:
        registros = f.readlines()
        if registros == '':
            print('O arquivo está vazio\n')
            exit(1)

    tamanhoHeader, tamanhoRegistro = escritaTamanhoFixo(registros)
    menu = 1
    while menu != 0:
        menu = int(input("O que gostaria de fazer?\n1- Remover\n2- Inserir\n0- Sair\n"))
        if menu == 1:
            removeRegistro(saida, tamanhoHeader, tamanhoRegistro)
        #if menu == 2:
            #inserirRegistro
        if menu != 0 and menu != 1 and menu != 2:
            print("valor incorreto\nTente novamente:\n")
    
    if menu == 0:
        print("o programa será finalizado\n")
        exit()