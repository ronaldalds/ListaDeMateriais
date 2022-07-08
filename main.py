from upload_file import UploadFile
from processing import osnap, tp, list_fiber, list_sco, pole_user, load_file
import time

inicio = time.time()

project = load_file('FTT.kml')  # open file project
pole = project.data_pole()  # extractor pole
style = project.data_style()  # extractor style
element = project.element('REDE FTTH')  # extractor rede
element_expansion = project.element('EXPANSION')  # extractor expansion
osnap(value=element[1], pole=pole)
tp(value=element[1], style=style)
osnap(value=element[0], pole=pole)
pole_user()

for i in list_fiber(element[0]):
    print(i, list_fiber(element[0])[i])
# for i in element[1]:
#     print(i.length)
# print(pole_user(pole))
# for i in pole:
#     print(i.user)


# for i in element[0]:
#     print(i.sco)
# for i in pole:
#     if i.eq:
#         try:
#             print('==================================== ',i.eq[0].name, i.eq[1].name)
#         except:
#             print(i.eq[0].name)
#         print(i.eq, i.eq[0].name)

# for i in element[1]:
#     print(i.name, i.stored, i.type)

fim = time.time()
print(fim - inicio)
