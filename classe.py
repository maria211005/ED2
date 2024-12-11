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
    with open('saida2.txt', 'r') as entrada:
        linha = entrada.readline()
        registro = entrada.readlines()
        key = []
        for linha in registro:
            linha_sep = linha.split(sep='|')
            resultado = Heroi(linha_sep)
            key.append(resultado.key)

        print(key)
            