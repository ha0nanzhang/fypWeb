import dominate
import glob
from dominate.tags import *
import os
import json

tableHeaders = ['id', 'original photo', 'parameters', 'model']
noRows = 3

inputPhotos = glob.glob('img/*.png')
outputPhotos = glob.glob('newPic/*.png')

doc = dominate.document(title = "example")
#print(doc)

with doc.head:
    link(rel='stylesheet', href='style.css')

with doc:
    with div(cls = 'container'):
        h1("photo to model")
        with table(id='main', cls = 'gridtable'):
            with thead():
                with tr():
                    for tableHead in tableHeaders:
                        th(tableHead)
            with tbody():
                for i in range(noRows):
                    with tr():
                        td(i+1)
                        td(div(img(src=inputPhotos[i]), _class = 'img', style ="height:10%, width:10%"))

                        os.system('python3 main.py -- ' + str(inputPhotos[i]))
                        os.system('py.exe eye-color.py --input_path=' + str(inputPhotos[i]))
                        os.system('python3 gad.py --image ' + str(inputPhotos[i]))

                        with open('test.json', "r") as readFile:
                            data = json.load(readFile)

                        with open('test1.json', "r") as rFile:
                            data2 = json.load(rFile)
                            
                        with open('skinhair.json', "r") as skinHair:
                            data3 = json.load(skinHair)
                        
                        skinRgb = tuple(data3['skin'])
                        hairRgb = tuple(data3['hair'])

                        eyePatch = div(_class='circle', style = "background-color:" + str(data['eye']))
                        skinPatch = div(_class='circle', style = "background-color:rgb" + str(skinRgb))
                        hairPatch = div(_class='circle', style = "background-color:rgb" + str(hairRgb))

                        td('Eye colour: ' + str(data['eye']), eyePatch, br(), 'Gender: ' + str(data2['gender']), br(), br(),'Age: ' + str(data2['age']), br(), br(), 'Skin colour: ' + str(data3['skin']), skinPatch, br(), 'hair colour: ' + str(data3['hair']), hairPatch)
                        # + str(data2) +  str(data3), _class = 'body')))
                        
                        os.system('blender.exe -b finalmaybe.blend -P h.py -- test.json test1.json skinhair.json ' + str(i))

                        td(div(img(src=outputPhotos[i]), _class = 'img', style="height:10%, width:10%"))
                       
                        # td(div(_class='circle', style = "background-color:rgb" + colour))
                        # td(str(ci))

                     


with open('index.html', 'w') as f:
    f.write(doc.render())