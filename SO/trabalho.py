def defineLetras():
    letras =[]

    for i in range(ord('A'), ord('Z')+1):
        letras.append(chr(i))
    
    return letras


if __name__ == '__main__':
    alfabeto = defineLetras()
    i = 0

    processo = []
    while(i < len(alfabeto)):
        nome = alfabeto[i]
        horaChegada = input("Digite o horário de chegada: ")
        quantCPU = input("Digite quanto de CPU vai precisar: ")

        processo.append(f"{nome}, {horaChegada}, {quantCPU}")

        i+=1
    
    print(processo)