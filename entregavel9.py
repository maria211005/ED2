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

def escritaTamanhoFixo(registros):
    #abre o arquivo de saida
    with open(saida, 'w') as output:
        #adiciona o last no cabeçalho
        registros[0] = registros[0].strip('\n') + ",last:-1\n"
        tam = []
        #guarda o tamanho de cada linha pra encontrar a maior registro e alinhar os outros
        for linha in registros:
            tam.append(len(linha))
        
        tamHeader = tam[0] #tamanho do cabeçalho

        #define a maior linha e guarda seu índice
        tamRegistro = tam[1]
        maiorLinha = 0
        for i in range(1, len(tam)):
            if tam[i] > tamRegistro:
                tamRegistro = tam[i]
                maiorLinha = i
        
        #adiciona caracteres especiais para completar as linhas que tem menos que a maior linha
        for linha in registros:
            linha = linha.strip('\n')
            linha = linha.replace(",", "|")
        
            if len(linha) < tamRegistro:
                dif = tamRegistro - len(linha) -1
                linha = linha + '*' * dif + '\n'
            else:
                linha = linha + '\n'
            
            #escreve a linha no arquivo de saida
            output.write(linha)
    return tamHeader, tamRegistro, maiorLinha    #retorna para a main

def removeRegistro(tamHeader, tamRegistro, maiorLinha, quantRegistros):
    recebe = 1
    while recebe != 0:#enquanto quiser remover registros
        RRN = int(input("qual o indice que deseja remover?\n"))
        if RRN <= 0 or RRN > quantRegistros:
            print(f"índice inválido, fora do limite de 0 a {quantRegistros} registros\nTente Novamente\n")
            
        else:
            deslocamento = tamHeader + (RRN-1)*tamRegistro  #valor para ser deslocado e encontrar o registro solicitado

            with open(saida, 'r+') as output:
                output.seek(deslocamento)
                linha = output.read(2)
                if '*' in linha:   #se tiver * significa que já foi removido 
                    print("Registro já removido\nTente Novamente\n")
                else:                       #caso for um registro valido para retirar
                    output.seek(tamHeader -3)   #o valor do last tá no ultimo tópico do cabeçalho
                    
                    #necessário ler o valor do last para colocar na linha removida
                    last = output.readline()
                    last = last.strip('\n')
                    output.seek(tamHeader -3)
                    
                    #caso seja menor que dois digitos
                    if RRN < 10:
                        output.write(str(RRN) + " ")  
                    else:   #caso contrário
                        output.write(str(RRN))

                    #desloca para a linha que será removida
                    output.seek(deslocamento)
                    linha = output.readline()
                    
                    #adequa esteticamente para manter todos os registros alinhados apesar da remoção
                    if int(last) < 0 or int(last) > 9:      #se o last tiver dois dígitos
                        if RRN == maiorLinha:               #tratar a maior linha diferente das outras
                            linha = f"*{last}" + linha[3:-2]
                        else:
                            linha = f"*{last}" + linha[2:-2]
                    else:                                   #se tiver um dígito
                        if RRN == maiorLinha:
                            linha = f"*{last}" + linha[3:-2]
                        else:
                            linha = f"*{last}" + linha[2:-3]
                    
                    output.seek(deslocamento)       #desloca novamente para o lugar do registro
                    output.write(linha)             #escreve no arquivo o registro removido

                    print("Registro Removido")
                    #caso queira remover mais algum registro
                    recebe = 2
                    while recebe != 1 and recebe != 0:
                        recebe = int(input("Gostaria de remover mais algum registro?\n1- Sim\n0-Não\n"))
                        if recebe != 1 and recebe != 0:
                            print("Número inválido\nTente Novamente:\n")
                    if recebe == 0:
                        return    #sai da função
                
                
def reorganizaArquivo(novoRegistro, tamHeader, tamRegistro):
    with open(saida, "r+") as output:
        if len(novoRegistro) < tamRegistro:
            dif = tamRegistro - len(novoRegistro) -1
            novoRegistro = novoRegistro + '*' * dif + '\n'
            maior = False
        else:
            tamRegistro = len(novoRegistro)
            maior = True
            output.seek(tamHeader)
            regs = output.readlines()
            output.seek(tamHeader)
            for linha in regs:
                linha = linha.strip('\n')
                newDif = tamRegistro - len(linha)
                linha = linha + '*' * newDif + '\n'
                output.write(linha)
        return tamRegistro, maior

def insereNovoRegistro(tamHeader, tamRegistro, quantRegistros): 
    with open(saida, 'r+') as output:
        #condições para realmente inserir o novo registro
        output.seek(tamHeader)
        linha = output.readline()
        num = 0
        num2 = 0
        igual = 1
        for i in range(len(linha)):
            if linha[i] == "|":     #conta quantos campos tem um registro
                num += 1
        
        while (num > num2 or igual == 1):
            igual = 0
            num2 = 0

            novoRegistro = str(input("Insira o novo registro a ser inserido:\n"))
            #verifica quantos campos tem o registro inserido
            for i in range(len(novoRegistro)):
                if novoRegistro[i] == ",":      
                    num2 += 1
            if num2 < num:#se for menor que o contador de registros, não entra
                print("Registro inválido\nTente Novamente\n")

            else:
                #verifica se o registro já foi inserido ou não
                registro_sep = novoRegistro.split(sep=",")
                output.seek(tamHeader)
                arq = output.readlines()
                for linha in arq:
                    linha_sep = linha.split(sep="|")
                    if registro_sep[0] == linha_sep[0]:
                        igual = 1
                if igual == 1:#se já foi inserido, não entra
                    print("Registro já inserido\nTente novamente\n")

                else:
                    #insere o registro no arquivo
                    novoRegistro = novoRegistro.replace(",", "|")
                        
                    tamRegistro, maior = reorganizaArquivo(novoRegistro, tamHeader, tamRegistro)

                    output.seek(tamHeader -3)
                    last = int(output.readline().strip('\n'))
                    if(last == -1):
                        #significa que nao temos posicoes disponiveis para reuso
                        print("Registro sendo inserido no final do arquivo\n")
                        output.seek(0, 2)
                        output.write(novoRegistro + "\n")
                        if maior == True:
                            maiorLinha = quantRegistros + 1
                    else:
                        #insere na ultima posição removida
                        output.seek(tamHeader + (last-1)*tamRegistro + 1)   #chegando aonde ta o numero do last, +1 para pular o *
                        newLast = output.read(2)                            #recebe o novo valor de last
                        print(newLast)
                        print(f"Registro sendo inserido na linha {last}\n")
                        output.seek(tamHeader + (last-1)*tamRegistro)       #desloca novamente para o inicio dessa linha
                        output.write(novoRegistro)                          #escreve o novo registro
                        output.seek(tamHeader -3)                           #desloca para o lugar que está escrito o valor do last
                        output.write(newLast)                               #atualiza o valor do last
                        if maior == True:
                            maiorLinha = last

                    if maior == False:
                        maiorLinha = 0
                    return tamRegistro, maiorLinha  #retorna tamanho e o índice da maior linha


if __name__ == "__main__":
    #abre o arquivo de entrada
    with open(entrada, 'r') as f:
        registros = f.readlines()
        quantidadeRegistros = len(registros) - 1
        if registros == '':
            print('O arquivo está vazio\n')
            exit(1)

    #alinha os registros
    #retorna o tamanho do cabeçalho, o tamanho de cada registro e o índice da maior linha
    tamanhoHeader, tamRegistro, maiorLinha = escritaTamanhoFixo(registros)

    menu = 1
    #menu de opções
    tamanhoRegistro = 0
    while menu != 0:#enquanto não quiser sair do código
        menu = int(input("O que gostaria de fazer?\n1- Remover\n2- Inserir\n0- Sair\n"))
        if menu == 1:#caso queira remover algum registro
            removeRegistro(tamanhoHeader, tamRegistro, maiorLinha, quantidadeRegistros)
        if menu == 2:#caso queira inserir algum registro
            tamanhoRegistro, Linha = insereNovoRegistro(tamanhoHeader, tamRegistro, quantidadeRegistros)
            if tamanhoRegistro > tamRegistro:
                tamRegistro = tamanhoRegistro
            if Linha != 0:
                maiorLinha = Linha

        if menu != 0 and menu != 1 and menu != 2:#caso insira algum valor fora das opções
            print("valor incorreto\nTente novamente:\n")
    
    if menu == 0:#caso queira a opcao de sair
        print("o programa será finalizado\n")
        exit()