from projeto import Projeto
from elemento import Elemento
from cabo import Cabo
from poste import Poste
from math import sqrt


cabo = Cabo('Projeto.kml')
# t = cabo.sco()
print(cabo.plaqueta)
# poste = Poste('Projeto.kml')
# elemento = Elemento('Projeto.kml')
# print(elemento.poste_por_elemento('CEO'))
# style = Style('Projeto.kml')
# projeto = Projeto('Projeto.kml')
# reserva = Reserva('Projeto.kml')
for i in cabo.somador(cabo.tipo_fibras(),cabo.comprimento_cabo()):
    print(i,cabo.somador(cabo.tipo_fibras(),cabo.comprimento_cabo())[i])
for i in cabo.somador(cabo.tipo_fibras(),cabo.alca):
    print(i,cabo.somador(cabo.tipo_fibras(),cabo.alca)[i])
for i in cabo.somador(cabo.tipo_fibras(),cabo.laco):
    print(i,cabo.somador(cabo.tipo_fibras(),cabo.laco)[i])
# print(t)
# print(cabo.sco())