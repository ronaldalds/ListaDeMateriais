from cabo import Cabo

cabo = Cabo('Projeto.kml')

# for i in cabo.somador(cabo.tipo_fibras(),cabo.comprimento_cabo()):
#     print(f'Cabo {i} - {cabo.somador(cabo.tipo_fibras(), cabo.comprimento_cabo())[i]:.2f} m')
# for i in cabo.somador(cabo.tipo_fibras(),cabo.alca):
#     print(f'Alça {i} - {cabo.somador(cabo.tipo_fibras(), cabo.alca)[i]} und')
# for i in cabo.somador(cabo.tipo_fibras(),cabo.laco):
#     print(f'Laço {i} - {cabo.somador(cabo.tipo_fibras(), cabo.laco)[i]} und')
# print(f'BRAÇADEIRA AJUSTÁVEL BAP4 (1000MM) C/ PARAFUSO - {len(cabo.bap_lancamento())} und')
# print(f'SUPORTE PARA CABOS ÓPTICOS SCO1 - {len(set(cabo.sco()))} und')
# print(f'PLAQUETA DE IDENTIFICAÇÃO DE CABO ÓPTICO ONLINE TELECOM - {cabo.plaqueta_lancamento} und')
# print(f'FIO DE ESPINAR ISOLADO FEI-125 - 0 RL') # falta cálculos
# print(f'RESERVA TÉCNICA - {cabo.contador("Reserva")} und')
# print(f'DERIVAÇÃO PREFORMADA P/ CORDOALHA DIELÉTRICA (6,4MM) - 0 und') # falta cálculos
# print('==============================================================================')
# print(f'CAIXA DE EMENDA ÓPTICA AÉREA 24F C/ SUPORTE RESERVA DPR - {cabo.contador("CEO")+cabo.contador("HUB-DPR")}')
# print(f'CAIXA DE DISTRIBUIÇÃO ÓPTICA CTO PRESLEY - {cabo.contador("CTO-HUB")}')
# print(f'BANDEJA PARA CAIXA DE EMENDA ÓPTICA DPR - 0 und')# falta cálculos
# print(f'BANDEJA INFERIOR PARA CTO PRESLEY - 0 und')# falta cálculos
# print(f'KIT DE DERIVAÇÃO PARA CAIXA DE EMENDA ÓPTICA - 0 und')# falta cálculos
# print(f'CAIXA DE DISTRIBUIÇÃO OPTICA CTO MINI PRESLEY - {cabo.contador("CTO")}')
# print(f'CAIXA TERMINAL ÓPTICA INDOOR CONECTORIZADA C/ SPLITTER 1X8 SMAP - {cabo.contador("CTO-Indoor")}')
print(cabo.spliter())
