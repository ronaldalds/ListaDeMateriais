from projeto import Projeto
from elemento import Elemento
from cabo import Cabo
from poste import Poste
from math import sqrt

cabo = Cabo('Projeto.kml')
# poste = Poste('Projeto.kml')
# elemento = Elemento('Projeto.kml')
# style = Style('Projeto.kml')
# projeto = Projeto('Projeto.kml')
# reserva = Reserva('Projeto.kml')

fibra = {}
alca = {}
# print(cabo.comprimento_cabo())
# print(cabo.tipo_fibras())
# print(cabo.nome)
# cto = cabo.cto
# cto_hub = cabo.cto_hub
# print(cabo.ceo)
# reserva = cabo.reserva
# print(ceo)
for i in cabo.somador(cabo.tipo_fibras(),cabo.comprimento_cabo()):
    print(i,cabo.somador(cabo.tipo_fibras(),cabo.comprimento_cabo())[i])
for i in cabo.somador(cabo.tipo_fibras(),cabo.alca):
    print(i,cabo.somador(cabo.tipo_fibras(),cabo.alca)[i])
print(len(cabo.bap))

# for i in fibra:
#     print(i, fibra[i])

# print(projeto._coordenada_fibra)
# print(elemento.style)
# print(elemento._coordenada_pop)
# print(elemento.nome_pop())
# print(cabo.comprimento_cabo())
# print(cabo.ceo)
# print(cabo.reserva)
# print(cabo._nome_fibra)
# print(cabo.cto_hub)
# print(cabo.cto)
# print(cabo.laco)
# print(cabo.alca)
# print(cabo.bap)
# print(cabo.nome)
# print(elemento.nome)
# print(cabo.contador('Reserva'))