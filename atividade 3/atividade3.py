import sys

#receber os parâmetros via linha de comando
entrada = ''
if(len(sys.argv) != 3):
	print("Quantidade de argumentos inválida. Tente novamente")
else:
	entrada = sys.argv[1]
#---------------------------------------------------------------------------------------------
#define a forma com que será organizado os dados
def defineTipoOrdenacao(arquivo):
    with open(arquivo, "r") as f:
        linha1 = f.readlines(200)           #verifica se tem algo no arquivo
        if len(linha1) < 3:
            print("arquivo inválido\nO programa será finalizado")
            exit(1)
        f.seek(0)                           #se tiver dados no arquivo, desloca para o começo
        
        linha1 = f.readline()               
        linha1 = linha1.strip("\n")         
        linha1_sep = linha1.split(sep=",")  #separa em uma lista com as duas condições

        sort = linha1_sep[0]                #o primeiro é o método de ordenação
        order = linha1_sep[1]               #o segundo é a forma com que seja ordenado

        sort = sort[len(sort)-1]            #recebe a letra do método
        order = order[len(order)-1]         #recebe a letra 

        if sort != 'Q' and sort != 'H' and  sort != 'M' and sort != 'I':
            print(f"opção {sort} de sort inválida\no programa será finalizado")
            exit(1)
        if order != 'C' and order != 'D':
            print(f"opção {order} de order inválida\no programa será finalizado")
            exit(1)
            
    return sort, order
#---------------------------------------------------------------------------------------
#
#função principal
if __name__ == "__main__":
    metodoBusca, ordenacao = defineTipoOrdenacao(entrada)
    print(metodoBusca, ordenacao)
