#main
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
if __name__ == '__main__':
    print("SIMULADOR DE GERENCIADOR DE PROCESSOS")
    print("Política Round Robin (Quantum = 5)\n\n\n")
    
    qProcessos = Queue()
    qTempos = Queue()

    qProcessados = []
    qTemposProcessados = []
    tempoTotal = 0
    tempo = 0
    duration = 0
    quantum = 5
    processando = False
    time = 0

    dict = {'Processo': 0, 'Tempo': 1, 'Chegada': 2, 'Prioridade': 3}
    dict1 = {}
    arq = []
    with open('processos.csv', 'r') as arquivo:
        for linha in arquivo:
            processo = linha.strip().split(',')
            arq.append(processo)
            
    tamanho = len(processo)
    processo = []
    iteration = 0
    for i in range(1, tamanho):
        processo.append([])
        #adiciona cada processo no vetor completo
        processo[i-1].append(arq[dict['Processo']][i])
        processo[i-1].append(arq[dict['Tempo']][i])
        processo[i-1].append(arq[dict['Chegada']][i])
        processo[i-1].append(arq[dict['Prioridade']][i])

        #salva o valor total de tempo de processos
        tempoTotal += int(processo[i-1][dict['Tempo']])
        #verifica se tem prioridade entre os processos
        iteration += (int(processo[i-1][dict['Prioridade']]))
        if iteration > 0:
            print(f"Processo {processo[i-1][dict['Processo']]} tem prioridade {processo[i-1][dict['Prioridade']]}")
            dict1.update({processo[i-1][dict['Processo']]: processo[i-1][dict['Prioridade']]})
            iteration = 0
            
    print("Processos na fila do Round Robim:")
    for i in range(len(processo)):
        print(processo[i][dict['Processo']]+"  ", end='')
    
    print("\n\nTempo de CPU requerida pelos processos:")
    for i in range(len(processo)):
        print(processo[i][dict['Tempo']]+"  ", end='')
    
    print("\n\nTempo de Chegada dos processos:")
    for i in range(len(processo)):
        print(processo[i][dict['Chegada']]+"  ", end='')
        
    #---------------------------------------------------------------------------------------------------------------
    #comeca o processo propriamente dito    
    i = 0
    qTemposProcessados.append(time)
    while tempo <= tempoTotal:
        if tempo < len(processo):
            if tempo == int(processo[i][dict['Chegada']]):
                qProcessos.enqueue(processo[i][dict['Processo']])
                qTempos.enqueue(processo[i][dict['Tempo']])
            if processando == False:
                valor = qProcessos.dequeue()
                time = qTempos.dequeue()
                qProcessados.append(valor)
                processando = True
                if int(time) > quantum:
                    duration += quantum
                    time = str(int(time) - quantum)
                else: duration += int(time)
            if tempo == duration:
                qTemposProcessados.append(duration)
                if int(time) > 0:
                    qProcessos.enqueue(valor)
                    qTempos.enqueue(time)
                processando = False
        else:
            if tempo == duration:
                qTemposProcessados.append(duration)
                if int(time) > 0:
                    qProcessos.enqueue(valor)
                    qTempos.enqueue(time)
                processando = False
                if qProcessos.isEmpty() == False:
                    valor = qProcessos.dequeue()
                    time = qTempos.dequeue()
                    qProcessados.append(valor)
                    processando = True
                    if int(time) > quantum:
                        duration += quantum
                    else: 
                        duration += int(time)
                    time = str(int(time) - quantum)
                        
        tempo+= 1
        i+= 1

    #exibe o resultado do processo
    print("\n\n\n\n\nLINHA DO TEMPO:\n")
    print(f"|{qTemposProcessados[0]}|", end='')
    for i in range(len(qProcessados)):
        print(f"------{qProcessados[i]}------|{qTemposProcessados[i+1]}|", end='')
        

    TME = []
    TMR = []
    for j in range(len(processo)):
        tempoMedioEspera = 0
        auxEspera = 0
        apareceu = False
        for i in range(len(qProcessados)):
            if qProcessados[i] == processo[j][dict['Processo']]:
                if apareceu == False:
                    tempoMedioEspera += qTemposProcessados[i] - int(processo[j][dict['Chegada']])
                    apareceu = True
                else:
                    tempoMedioEspera+= qTemposProcessados[i] - auxEspera
                auxEspera = qTemposProcessados[i+1]
        TME.append(tempoMedioEspera)
        TMR.append(tempoMedioEspera + int(processo[j][dict['Tempo']]))
    
    print("\n\n\n\n\nTempo de Espera de cada processo:")
    for i in range(len(processo)):
        print(processo[i][dict['Processo']]+"  ", end='')
    print("")
    for i in range(len(TME)):
        print(str(TME[i]) + " ", end='')
        
    print("\n\n\nTempo de Resposta de cada processo:")
    for i in range(len(processo)):
        print(processo[i][dict['Processo']]+"  ", end='')
    print("")
    for i in range(len(TMR)):
        print(str(TMR[i]) + " ", end='')
    
    print("\n\n\n\n")    
    print(f"Tempo Médio de Espera: {sum(TME)/len(processo)}")
    
    print(f"\nTempo Médio de Resposta: {sum(TMR)/len(processo)}")
    