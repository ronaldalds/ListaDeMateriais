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


# print(cabo.tipo_fibras())
# print(cabo.nome)
for i in cabo.comprimento_cabo():
    print(cabo.tipo_fibras()[i],cabo.comprimento_cabo()[i])
# print(projeto._coordenada_fibra)
# print(cabo.percuso)
# print(cabo.comprimento_cabo)
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