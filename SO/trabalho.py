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
    q = Queue()
    qProcessados = []

    dict = {'Processo': 0, 'Tempo': 1, 'Chegada': 2, 'Prioridade': 3}
    arq = []
    with open('processos.csv', 'r') as arquivo:
        for linha in arquivo:
            processo = linha.strip().split(',')
            tamanho = len(processo)
            arq.append(processo)

    processo = []
    for i in range(1, tamanho):
        processo.append([])
        processo[i-1].append(arq[dict['Processo']][i])
        processo[i-1].append(arq[dict['Tempo']][i])
        processo[i-1].append(arq[dict['Chegada']][i])
        processo[i-1].append(arq[dict['Prioridade']][i])


    for i in range(len(processo)):
        print(processo[i][dict['Processo']]+" ", end='')