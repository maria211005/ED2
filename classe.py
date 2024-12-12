class Heroi:
    def __init__(self, linha_sep):
            self.key = linha_sep[0]
            self.Name = linha_sep[1]
            self.Alignment = linha_sep[2]
            self.Gender = linha_sep[3]
            self.EyeColor = linha_sep[4]
            self.Race = linha_sep[5]
            self.HairColor = linha_sep[6]
            self.Publisher = linha_sep[7]
            self.SkinColor = linha_sep[8]
            self.Height = linha_sep[9]
            self.Weight = linha_sep[10]
            self.Intelligence = linha_sep[11]
            self.Strength = linha_sep[12]
            self.Speed = linha_sep[13]
            self.Durability = linha_sep[14]
            self.Power = linha_sep[15]
            self.Combat = linha_sep[16]
            self.Total = linha_sep[17]


if __name__ == '__main__':
    with open('input01.txt', 'r') as entrada:
        linha = entrada.readline()
        linha2 = entrada.readline()
        registro = entrada.readlines()
        arq = []
        for linha in registro:
            linha_sep = linha.split(sep='|')
            resultado = Heroi(linha_sep)
            arq.append(resultado.key)
            arq.append(resultado.Name)
            arq.append(resultado.Alignment)
            arq.append(resultado.Gender)
            arq.append(resultado.EyeColor)
            arq.append(resultado.Race)
            arq.append(resultado.HairColor)
            arq.append(resultado.Publisher)
            arq.append(resultado.SkinColor)
            arq.append(resultado.Height)
            arq.append(resultado.Weight)
            arq.append(resultado.Intelligence)
            arq.append(resultado.Strength)
            arq.append(resultado.Speed)
            arq.append(resultado.Durability)
            arq.append(resultado.Power)
            arq.append(resultado.Combat)
            arq.append(resultado.Total)
    
    print(arq)

    with open('saida.txt', 'w') as output:
        output.write(linha2)
        for i in range(len(arq)):
            if '\n' in arq[i]:
                output.write(arq[i])
            else:
                output.write(arq[i] + "|")