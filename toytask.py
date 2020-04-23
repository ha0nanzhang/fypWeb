#Reference: https://github.com/Knio/dominate 

import dominate
import glob
from dominate.tags import *
import os
import json
import time

tableHeaders = ['id', 'original photo', 'parameters', 'model']
noRows = 24

inputPhotos = glob.glob('img/*.png')

doc = dominate.document(title = "example")

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
                        os.system('blender.exe -b model.blend -P alterModel.py -- eyeColour.json ageGender.json skinHair.json ' + str(i))
                        
                        with open('eyeColour.json', "r") as readFile:
                            data = json.load(readFile)

                        with open('ageGender.json', "r") as rFile:
                            data2 = json.load(rFile)
                            
                        with open('skinHair.json', "r") as skinHair:
                            data3 = json.load(skinHair)
                        
                        skinRgb = tuple(data3['skin'])
                        hairRgb = tuple(data3['hair'])

                        eyePatch = div(_class='circle', style = "background-color:" + str(data['eye']))
                        skinPatch = div(_class='circle', style = "background-color:rgb" + str(skinRgb))
                        hairPatch = div(_class='circle', style = "background-color:rgb" + str(hairRgb))

                        td('Eye colour: ' + str(data['eye']), eyePatch, br(), 'Gender: ' + str(data2['gender']), br(), br(),'Age: ' + str(data2['age']), br(), br(), 'Skin colour: ' + str(data3['skin']), skinPatch, br(), 'hair colour: ' + str(data3['hair']), hairPatch)
                        # + str(data2) +  str(data3), _class = 'body')))
                        outputPhotos = glob.glob('newPic/' + str(i) + '.png')
                        #print('files {}'.format(outputPhotos))

                        td(div(img(src=outputPhotos[0]), _class = 'img'))        


with open('index.html', 'w') as f:
    f.write(doc.render())
