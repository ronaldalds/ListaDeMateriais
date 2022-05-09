from projeto import Projeto
from elemento import Elemento
from cabo import Cabo
from poste import Poste
from style import Style
from reserva import Reserva
from math import sqrt

cabo = Cabo('Rede FTTh.kml')
poste = Poste('Coreaú Rede FTTh.kml')
elemento = Elemento('Rede FTTh.kml')
style = Style('Coreaú Rede FTTh.kml')
projeto = Projeto('Coreaú Rede FTTh.kml')
reserva = Reserva('Rede FTTh.kml')


# print(poste.coordenada_pop)
# print(poste.coordenada_pop_poste)
# print(poste.tipo_poste)
# print(poste.altura_poste)
# print(poste.esforco_poste)
# print(poste.rede_eletrica)
# print(poste.quantidade_casa)
# print(poste.quantidade_comercio)
# print(poste.quantidade_apartamento)
# print(poste.tipo_equipamento)
# print(poste.codigo_poste)
# print(poste.ocupacao)
# print(poste.foto)
print(elemento.coordenada_elemento)
print(elemento.nome_elemento)
print(elemento.tipo_elemento)
print(reserva.coordenada_reserva())

# print(caixa.contador('CEO'))
# print(caixa.contador('Reserva'))
# print(caixa.contador('CTO-HUB'))
# print(caixa.contador('CTO'))
# print(caixa.contador('CTO-Futura'))
# print(style.tipo_style)
# print(cabo.tratamento(poste.coordenada_pop_poste))
# print(cabo.nome)
# print(cabo.percuso)
# print(cabo.comprimento(poste.coordenada_pop_poste))
# print(elemento.tratamento(poste.coordenada_pop_poste))
