class Pessoa:
    #delimitando máximos de valores
    TAM_MAX_NOME = 10
    TAM_MAX_SOBRENOME = 10
    TAM_MAX_ENDERECO = 25
    TAM_MAX_CIDADE = 15
    TAM_MAX_ESTADO = 2
    TAM_MAX_CEP = 9
    
    #define classe de Pessoa para receber parâmetros
    def __init__(self, nome, sobrenome, endereco, cidade, estado, cep): #inicializa todos esses parametros recebidos
        self.nome = nome
        self.sobrenome = sobrenome
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        
    def __str__(self):
        return f'nome={self.nome}, endereco={self.endereco}, cep={self.cep}' #retorna todos esses dados formatados
    
    
        
p1 = Pessoa("Mantova", "Gomes", "Rua dos Pombos", "Arapongas", "PR", "86800-000")

with open("cadastro.txt","w") as f:
    #caso a quantidade de caracteres de nome recebidos for maior que a quantidade 
    if len(p1.nome) > p1.TAM_MAX_NOME:
        temp = p1.nome[0:p1.TAM_MAX_NOME]
        f.write(temp)
    
    #caso for menor que o máximo
    else:
        f.write('{0:<{TAM_MAX_NOME}}'.format(p1.nome, TAM_MAX_NOME = p1.TAM_MAX_NOME))
        
    #caso a quantidade de caracteres de sobrenome recebidos for maior que a quantidade     
    if len(p1.sobrenome) > p1.TAM_MAX_SOBRENOME:
        temp = p1.sobrenome[0:p1.TAM_MAX_SOBRENOME]
        f.write(temp)
    
    #caso for menor que o máximo
    else:
        f.write('{0:<{TAM_MAX_SOBRENOME}}'.format(p1.sobrenome, TAM_MAX_SOBRENOME = p1.TAM_MAX_SOBRENOME))