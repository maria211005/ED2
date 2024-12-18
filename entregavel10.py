#só abri o arquivo pra dizer q fiz algo agora KKKKKKKKKKKKKKKKKKKKKKKKKKK

#PESQUISA
#1) Procurar a chave na tabela de índices
#--> busca binária
#--> se achou ---> (chave, RRN)
#--> calcular offset
#--> leitura usando o RRN
#--> retorna registro para o usuário

#INSERÇÃO
#1) gerar una chave para o novo registro
#2) realizar uma pesquisa (chamar a função anterior)
#--> verifica se o novo registro ja existe (tem que retornar vazio)
#3) leitura do cabeçalho (last)
#--> se for last == -1:
#    RRN + 1
#    adicionar o registro no fim do arquivo 
#    adicionar na tabela de índices (chave, RRN)
#    ordenar a tabela de índices

