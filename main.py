from upload_file import UploadFile

project = UploadFile('FTT.kml') # open file project

# project.extractor_style() # upload style all project

data = project.fiber_rede() # extractor data file


for i in data:

    print(i, data[i].name, data[i].length)
    # print(i, data[i].stored, data[i].type, data[i].style)

# print(data)