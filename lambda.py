class Objet:
    def __init__(self, x):
        self.at1 = x
        self.at2 = x / 2


lista1 = []
for x in range(30):
    lista1.append(Objet(x))

lista2 = [x.at1 for x in lista1 if x.at1 % 2 == 0]

print(lista2)