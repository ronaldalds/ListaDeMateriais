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
# print(elemento.coordenada_elemento)
# print(elemento.nome_elemento)
# print(elemento.tipo_elemento)
# print(reserva.coordenada_reserva())
# print(elemento.contador('CEO'))
# print(elemento.contador('Reserva'))
# print(elemento.contador('CTO-HUB'))
# print(elemento.contador('CTO'))
# print(elemento.contador('CTO-Futura'))
# print(style.tipo_style)
# print(cabo.nome)
# print(cabo.percuso)
# print(cabo.tratamento(poste.coordenada_pop_poste))
print(cabo.comprimento_cabo(poste.coordenada_pop_poste))
# print(cabo.ceo(poste.coordenada_pop_poste))
# print(cabo.reserva(poste.coordenada_pop_poste))
print(cabo.cto_hub(poste.coordenada_pop_poste))
# print(cabo.cto(poste.coordenada_pop_poste))
# print(cabo.cto_futura(poste.coordenada_pop_poste))
