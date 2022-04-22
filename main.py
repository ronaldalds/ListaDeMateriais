from projeto import Projeto
from caixa import Caixa
from cabo import Cabo
from poste import Poste
from math import sqrt

test = Cabo('Rede FTTh.kml')
test2 = Poste('Coreaú.kml')
test3 = Caixa('Rede FTTh.kml')

# n = 259
# print(test.nome[n],test.tratamento[n],test.percuso[n])
# print(test3.nome_caixa)
# print(test3.coordenada_caixa)

print(test.tratamento(test2.coordanada_poste,test.percuso))