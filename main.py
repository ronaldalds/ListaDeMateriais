from upload_file import UploadFile

project = UploadFile('FTT.kml') # open file project 3.203,76

style = project.extractor_style() # upload style all project

data = project.fiber_rede() # extractor data file
pole = project.data_pole() # extractor pole file

print(style)

# print(data)
# print(pole)

# for p in pole:
#     print(p, pole[p].coordinates, pole[p].height)


# for i in data:

    # print(i, data[i].route_fiber, data[i].length)
    # print(i, data[i].stored, data[i].type, data[i].style)

# print(data)