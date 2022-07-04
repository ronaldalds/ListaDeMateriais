from upload_file import UploadFile

project = UploadFile('FTT.kml') # open file project

# project.extractor_style() # upload style all project

data = project.fiber_rede() # extractor data file
pole = project.data_pole() # extractor pole file

print(data)
print(pole)

# for p in pole:
#     print(p, pole[p].coordinates, pole[p].height)


for i in data:

    print(i, data[i].type, data[i].length)
    # print(i, data[i].stored, data[i].type, data[i].style)

# print(data)