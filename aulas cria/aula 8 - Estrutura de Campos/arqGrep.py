def grepSimulation(arquivo, palavra):
    lista_indice = []
    linha_corrente = 1
    try:
        with open(arquivo, 'r') as f:
            for linha in f:
                linha = linha.strip('\n')
                linha_sep = linha.split(sep='|')
                
                if palavra in linha_sep:
                    lista_indice.append(linha_corrente)
                linha_corrente = linha_corrente + 1
                
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado")
        exit(1)
        
    if len(lista_indice) == 0:
        print(f"A palavra '{palavra}' não foi encontrada no arquivo '{arquivo}'")
    else:
        return lista_indice
        
        
resultado = grepSimulation("teste.txt", "Arapongas")

if type(resultado) == str:
    print(resultado)
else:
    print(f"o resultado está na linha: {resultado}")