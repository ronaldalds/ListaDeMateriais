from flask import Flask, render_template
from equipamento import Equipamento

app = Flask(__name__)
equipamento = Equipamento('Projeto.kml')

@app.route('/inicio')
def ola():
    return render_template('lista.html', titulo='Lista de Materiais', equipamento = equipamento)

app.run()

# for i in equipamento.cabo():
#     print(f'{i} - {equipamento.cabo()[i]:.2f} m')
# # for i in equipamento.somador(equipamento.tipo_fibras(), equipamento.alca):
#     print(f'Alça {i} - {equipamento.somador(equipamento.tipo_fibras(), equipamento.alca)[i]} und')
# for i in equipamento.somador(equipamento.tipo_fibras(), equipamento.laco):
#     print(f'Laço {i} - {equipamento.somador(equipamento.tipo_fibras(), equipamento.laco)[i]} und')
# print(f'BRAÇADEIRA AJUSTÁVEL BAP4 (1000MM) C/ PARAFUSO - {equipamento.bap_lancamento()} und')
# print(f'SUPORTE PARA CABOS ÓPTICOS SCO1 - {len(set(equipamento.sco()))} und')
# print(f'PLAQUETA DE IDENTIFICAÇÃO DE CABO ÓPTICO ONLINE TELECOM - {equipamento.plaqueta_lancamento} und')
# print(f'FIO DE ESPINAR ISOLADO FEI-125 - {equipamento.fio_lancamento()} RL')
# print(f'RESERVA TÉCNICA - {equipamento.contador("Reserva")} und')
# print(f'DERIVAÇÃO PREFORMADA P/ CORDOALHA DIELÉTRICA (6,4MM) - 0 und') # falta cálculos
# print('==============================================================================')
# print(f'CAIXA DE EMENDA ÓPTICA AÉREA 24F C/ SUPORTE RESERVA DPR - {equipamento.contador("CEO") + equipamento.contador("HUB-DPR")}')
# print(f'CAIXA DE DISTRIBUIÇÃO ÓPTICA CTO PRESLEY - {equipamento.contador("CTO-HUB")}')
# print(f'BANDEJA PARA CAIXA DE EMENDA ÓPTICA DPR - {(equipamento.contador("CEO") + equipamento.contador("HUB-DPR"))*2} und')
# print(f'BANDEJA INFERIOR PARA CTO PRESLEY - {equipamento.bandeja_cto_hub()} und')
# print(f'KIT DE DERIVAÇÃO PARA CAIXA DE EMENDA ÓPTICA - {equipamento.derivacao_ceo()} und')
# print(f'CAIXA DE DISTRIBUIÇÃO OPTICA CTO MINI PRESLEY - {equipamento.contador("CTO")}')
# print(f'DIVISOR DE SINAL (SPLITTER) OPTICO PLC 1X8 G.657A NC-NC 250UM 2M/2M - {len(equipamento.spliter_con_1x8())} und')
# print(f'DIVISOR DE SINAL (SPLITTER) OPTICO PLC 1X16 G.657A NC-SC/APC 900UM 0.9M/0.6M - {len(equipamento.spliter_con_1x16())} und')
# print(f'DIVISOR DE SINAL (SPLITTER) OPTICO PLC 1X2 G.657A NC-NC 250UM 2M/2M - {len(equipamento.spliter_nc_1x2())} und')
# print(f"DIVISOR DE SINAL (SPLITTER) OPTICO PLC 1X8 G.657A NC-NC 250UM 2M/2M - {len(equipamento.spliter_nc_1x8())} und")
# print(f"DIVISOR DE SINAL (SPLITTER) OPTICO PLC 1X16 G.657A NC-NC 250UM 2M/2M - {len(equipamento.spliter_nc_1x16())} und")
# print(f'ADAPTADOR ÓPTICO SM SIMPLEX SC/APC - {len(equipamento.spliter_con_1x8())*8} und')
# print(f'CAIXA TERMINAL ÓPTICA INDOOR CONECTORIZADA C/ SPLITTER 1X8 SMAP - {equipamento.contador("CTO-Indoor")}')
# print(f'BRAÇADEIRA AJUSTÁVEL BAP4 (1000MM) C/ PARAFUSO - {equipamento.bap_fusao()} und')
# print(f'PLAQUETA DE IDENTIFICAÇÃO DE CABO ÓPTICO ONLINE TELECOM - {equipamento.plaqueta_fusao} und')
# print(f'FIO DE ESPINAR ISOLADO FEI-125 - {equipamento.fio_fusao()} RL')
# print(f'PRENSA CABO POLIMERICO P/ CORDOALHA DIELÉTRICA - {equipamento.prensa_cabo()} und')
# print(f'PROTETOR DE EMENDA PE-04 45MM 3,4MM - {equipamento.tubete_45()} und')
# print(f'PROTETOR DE EMENDA PE-05 60MM 3,4MM - {equipamento.tubete_60()} und')

# final = time.time()
# print(final - inicial)
