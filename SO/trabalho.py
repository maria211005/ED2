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
    #print(processo[i-1][dict['Processo']]+" ", end='')
    qProcessos = Queue()
    qTempos = Queue()

    qProcessados = []
    qTemposProcessados = []
    tempoTotal = 0
    tempo = 0
    duration = 0
    quantum = 5
    processando = False

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

    #comeca o processo propriamente dito    
    i = 0
    while tempo < tempoTotal:
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
                        time = str(int(time) - quantum)
                    else: duration += int(time)
        tempo+= 1
        i+= 1
        
    print(qTemposProcessados)