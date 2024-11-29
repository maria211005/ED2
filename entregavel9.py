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
'''        
def removeRegistro(tamHeader, tamRegistro, maiorLinha):
    recebe = 1
    while recebe == 1:
        RRN = int(input("qual o indice que deseja remover?\n"))
        deslocamento = tamHeader + (RRN-1)*tamRegistro

        with open(saida, 'r+') as output:
            output.seek(deslocamento)
            if output.read(1) == '*':
                print("Registro já removido\nTente Novamente\n")
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
                    if RRN == maiorLinha:
                        linha = f"*{last}" + linha[3:-2]
                    else:
                        linha = f"*{last}" + linha[2:-2]
                else:
                    if RRN == maiorLinha:
                        linha = f"*{last}" + linha[3:-2]
                    else:
                        linha = f"*{last}" + linha[2:-3]
                output.seek(deslocamento)
                output.write(linha)

                recebe = int(input("Registro Removido\nGostaria de remover mais algum registro?\n1- Sim\n0-Não\n"))
                if recebe == 0:
                    return int(last)
    
'''        
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
def insereNovoRegistro(tamHeader, tamRegistro, maiorLinha, last): 
    novoRegistro = str(input("Insira o novo registro a ser inserido:\n"))

    with open(saida, 'r+') as output:
        #significa que nao temos posicoes disponiveis 
        if(last == -1):
            print("Registro sendo inserido no final do arquivo...\n")
            output.seek(0, 2)
            output.write(novoRegistro)
        else:
            #atualizando valor do last
            output.seek(tamHeader + (last-1)*tamRegistro + 1) #chegando aonde ta o numero do last
            newLast = output.read(2)
            output.seek(tamHeader + (last-1)*tamRegistro)
            output.write(novoRegistro)
            output.seek(tamHeader -3)
            output.write(newLast + " ")
            #last = id ---> essa id ta indexada pelo last


def escritaTamanhoFixo(registros):
    #abre o arquivo de saida
    with open(saida, 'w') as output:
        #adiciona o last no cabeçalho
        registros[0] = registros[0].strip('\n') + ",last:-1\n"
        TamReg = 0
        tam = []
        #guarda o tamanho de cada linha pra encontrar a maior registro e alinhar os outros
        for linha in registros:
            tam.append(len(linha))
        
        tamHeader = tam[0] #tamanho do cabeçalho

        #define a maior linha e guarda seu índice
        TamReg = tam[1]
        maiorLinha = 0
        for i in range(1, len(tam)):
            if tam[i] > TamReg:
                TamReg = tam[i]
                maiorLinha = i
        
        #adiciona caracteres
        for linha in registros:
            linha = linha.strip('\n')
            linha = linha.replace(",", "|")
        
            if len(linha) < TamReg:
                dif = TamReg - len(linha) -1
                linha = linha + '*' * dif + '\n'
            else:
                linha = linha + '\n'
            
            output.write(linha)
    return tamHeader, TamReg, maiorLinha

if __name__ == "__main__":
    #abre o arquivo de entrada
    with open(entrada, 'r') as f:
        registros = f.readlines()
        if registros == '':
            print('O arquivo está vazio\n')
            exit(1)

    #alinha os registros
    #retorna o tamanho do cabeçalho, o tamanho de cada registro e o índice da maior linha
    tamanhoHeader, tamanhoRegistro, maiorLinha = escritaTamanhoFixo(registros)

    #menu de opções
    menu = 1
    last = -1
    while menu != 0:#enquanto não quiser sair do código
        menu = int(input("O que gostaria de fazer?\n1- Remover\n2- Inserir\n0- Sair\n"))
        if menu == 1:#caso queira remover algum registro
            last = removeRegistro(tamanhoHeader, tamanhoRegistro, maiorLinha)
        if menu == 2:#caso queira inserir algum registro
            insereNovoRegistro(tamanhoHeader, tamanhoRegistro, maiorLinha, last)
        if menu != 0 and menu != 1 and menu != 2:#caso insira algum valor fora das opções
            print("valor incorreto\nTente novamente:\n")
    
    if menu == 0:#caso queira a opcao de sair
        print("o programa será finalizado\n")
        exit()