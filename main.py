from upload_file import UploadFile
import time

inicio = time.time()
project = UploadFile('FTT.kml')  # open file project
pole = project.data_pole()  # extractor pole
style = project.data_style()  # extractor style

fiber = project.element('REDE FTTH')  # extractor fiber
print(len(fiber[0]))
fiber_expansion = project.element('EXPANSION')  # extractor fiber

print(len(fiber_expansion[0]))

fim = time.time()
print(fim - inicio)

# inicio1 = time.time()
# for i in fiber[1]:
#     i.type(style), i.name, i.pole(pole)
# fim1 = time.time()
# print(fim1 - inicio1)

# inicio2 = time.time()
# for i in fiber[1]:
#     i.type(style), i.name, i.pole(pole)
# fim2 = time.time()
# print(fim2 - inicio2)
