def grepSimulation(arquivo, palavra):
    linha_corrente = 0
    linha_encontrada = []
    try:
        with open(arquivo, 'r') as f:
            for linha in f:
                linha = linha.strip('\n')
                linha_sep = linha.split(sep='|')
                
                if palavra in linha_sep:
                    linha_encontrada.append(linha)
                    linha_corrente = linha_corrente + 1
                
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado")
        exit(1)
        
    if linha_corrente == 0:
        print(f"A palavra '{palavra}' não foi encontrada no arquivo '{arquivo}'")
    else:
        return linha_encontrada
        
        
registros = grepSimulation("teste.txt", "Arapongas")
print("Registro encontrado:")
for i in range(len(registros)):
    print(f"{registros[i]}")
    