from projeto import Projeto
from caixa import Caixa
from cabo import Cabo
from poste import Poste
from style import Style
from math import sqrt

test = Cabo('Rede FTTh.kml')
test2 = Poste('Coreaú Rede FTTh.kml')
test3 = Caixa('Rede FTTh.kml')
test4 = Style('Coreaú Rede FTTh.kml')
test5 = Projeto('Coreaú Rede FTTh.kml')

# print(test2.coordanada_poste)
# print(test2.tipo_poste)
# print(test2.altura_poste)
# print(test2.esforco_poste)
# print(test2.rede_eletrica)
# print(test2.quantidade_casa)
# print(test2.quantidade_comercio)
# print(test2.quantidade_apartamento)
# print(test2.tipo_equipamento)
# print(test2.codigo_poste)
print(test2.ocupacao)
# print(test5._ext_poste('POSTE'))
# print(test2.coordenada_pop_poste)
# print(test3.nome_caixa)
# print(test3.tipo)
# print(test3.contador('CEO'))
# print(test3.contador('Reserva'))
# print(test3.contador('CTO-HUB'))
# print(test3.contador('CTO'))
# print(test4.tipo_style)
# print(test3.coordenada_caixa)
# print(test.nome)
# print(test.tratamento(test2.coordenada_pop_poste))
# print(test3.tratamento(test2.coordanada_poste))