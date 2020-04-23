import bpy
import json
import os
import sys
argv = sys.argv
argv = argv[argv.index("--") + 1:]

dir = os.path.dirname(bpy.data.filepath)
testDir = os.path.join(dir, argv[0]) #eye colour
testDir2 = os.path.join(dir, argv[1]) #gender and age
testDir3 = os.path.join(dir, argv[2]) #skin and hair colour

with open(testDir, "r") as readFile:
    data = json.load(readFile)

with open(testDir2, "r") as rFile:
    data2 = json.load(rFile)
    
with open(testDir3, "r") as skinHair:
    data3 = json.load(skinHair)
    
data1 = data["eye"]
dataG = data2["gender"]  
dataAge = data2["age"] 
dataSkin = data3["skin"]
dataHair = data3["hair"]

dataSkin[:] = [x / 255 for x in dataSkin]
dataHair[:] = [x / 255 for x in dataHair]

if dataAge == '(0-2)' or dataAge == '(3-6)' or dataAge == '(8-12)':
    bpy.data.collections['newfteen'].hide_viewport = True
    bpy.data.collections['newfteen'].hide_render = True
    bpy.data.collections['fold'].hide_viewport = True
    bpy.data.collections['fold'].hide_render = True
    bpy.data.collections['mteen'].hide_viewport = True
    bpy.data.collections['mteen'].hide_render = True
    bpy.data.collections['mold'].hide_viewport = True
    bpy.data.collections['mold'].hide_render = True
    bpy.data.collections['baby'].hide_viewport = False
    bpy.data.collections['baby'].hide_render = False
    
    
else:
    if dataG == 'Male':
        if dataAge == '(15-20)' or dataAge == '(25-32)':
            bpy.data.collections['newfteen'].hide_viewport = True
            bpy.data.collections['newfteen'].hide_render = True
            bpy.data.collections['fold'].hide_viewport = True
            bpy.data.collections['fold'].hide_render = True
            bpy.data.collections['mteen'].hide_viewport = False
            bpy.data.collections['mteen'].hide_render = False
            bpy.data.collections['mold'].hide_viewport = True
            bpy.data.collections['mold'].hide_render = True
            bpy.data.collections['baby'].hide_viewport = True
            bpy.data.collections['baby'].hide_render = True
    
        if dataAge == '(38-43)' or dataAge == '(48-53)' or dataAge == '(60-100)': 
            bpy.data.collections['newfteen'].hide_viewport = True
            bpy.data.collections['newfteen'].hide_render = True
            bpy.data.collections['fold'].hide_viewport = True
            bpy.data.collections['fold'].hide_render = True
            bpy.data.collections['mteen'].hide_viewport = True
            bpy.data.collections['mteen'].hide_render = True
            bpy.data.collections['mold'].hide_viewport = False
            bpy.data.collections['mold'].hide_render = False
            bpy.data.collections['baby'].hide_viewport = True
            bpy.data.collections['baby'].hide_render = True
            
    elif dataG == 'Female':
        if dataAge == '(15-20)' or dataAge == '(25-32)': 
            bpy.data.collections['newfteen'].hide_viewport = False
            bpy.data.collections['newfteen'].hide_render = False
            bpy.data.collections['fold'].hide_viewport = True
            bpy.data.collections['fold'].hide_render = True
            bpy.data.collections['mteen'].hide_viewport = True
            bpy.data.collections['mteen'].hide_render = True
            bpy.data.collections['mold'].hide_viewport = True
            bpy.data.collections['mold'].hide_render = True
            bpy.data.collections['baby'].hide_viewport = True
            bpy.data.collections['baby'].hide_render = True
#             
#            
        if dataAge == '(38-43)' or dataAge == '(48-53)' or dataAge == '(60-100)':    
            bpy.data.collections['newfteen'].hide_viewport = True
            bpy.data.collections['newfteen'].hide_render = True
            bpy.data.collections['fold'].hide_viewport = False
            bpy.data.collections['fold'].hide_render = False
            bpy.data.collections['mteen'].hide_viewport = True
            bpy.data.collections['mteen'].hide_render = True
            bpy.data.collections['mold'].hide_viewport = True
            bpy.data.collections['mold'].hide_render = True
            bpy.data.collections['baby'].hide_viewport = True
            bpy.data.collections['baby'].hide_render = True
            
    
    
    #nodes["ColorRamp"].color_ramp.elements[0].color
    
    
hairMat = bpy.data.materials.get("Material.021")
hairNode = bpy.data.node_groups["NodeGroup.006"].nodes["Mix"]
hairNode.inputs[1].default_value = (dataHair[0], dataHair[1], dataHair[2], 1)
hairNode.inputs[2].default_value = (0.0, 0.0, 0.0, 1)
    
#eye1=bpy.data.objects['Sphere.000']
mat = bpy.data.materials.get("iris.006")
eyeNode = bpy.data.node_groups["NodeGroup.007"].nodes["ColorRamp"]
mat2 = bpy.data.materials.get("Material.004")
eyeNode2 =  bpy.data.node_groups["NodeGroup.008"].nodes["Principled BSDF"]

skinNode = bpy.data.node_groups["NodeGroup"].nodes["Mix"]
if (dataSkin[0] < 100/255):
    skinNode.inputs[2].default_value = (dataSkin[0], dataSkin[1], dataSkin[2], 1)
else:
    skinNode.inputs[1].default_value = (dataSkin[0], dataSkin[1], dataSkin[2], 1)
#skinNode.inputs[2].default_value = (dataSkin[0] + 0.1, dataSkin[1] - 0.2, dataSkin[2] + 0.1, 1)


if data1 == "Brown":
    #bottom colour
    eyeNode.color_ramp.elements[0].color = (0.7, 0.2, 0.0, 1)
    #top colour
    eyeNode2.inputs[0].default_value = (0.6, 0.15, 0.0, 1)
if data1 == "Brown Black":
    eyeNode.color_ramp.elements[0].color = (0.1, 0.02, 0, 1)
    eyeNode2.inputs[0].default_value = (0, 0, 0.0, 1)
if data1 == "Brown Gray":
    eyeNode.color_ramp.elements[0].color = (0.2, 0.1, 0.1, 1)
    eyeNode2.inputs[0].default_value = (0.1, 0.02, 0.02, 1)
if data1 == "Green":
    eyeNode.color_ramp.elements[0].color = (0.1, 0.9, 0.0, 1)
    eyeNode2.inputs[0].default_value = (0.0, 0.8, 0.0, 1)
if data1 == "Green Gray":
    eyeNode.color_ramp.elements[0].color = (0.3, 0.9, 0.3, 1)
    eyeNode2.inputs[0].default_value = (0.1, 0.8, 0.1, 1)
if data1 == "Blue":
    eyeNode.color_ramp.elements[0].color = (0.0, 0.2, 0.8, 1)
    eyeNode2.inputs[0].default_value = (0.0, 0.1, 0.8, 1)
if data1 == "Blue Gray":
    eyeNode.color_ramp.elements[0].color = (0.4, 0.6, 0.8, 1)
    eyeNode2.inputs[0].default_value = (0.2, 0.4, 0.9, 1)
if data1 == "Other":
    eyeNode.color_ramp.elements[0].color = (0.53, 0.78, 0.87, 1)   
    eyeNode2.inputs[0].default_value = (0.25, 0.68, 0.76, 1)  
          
          
bpy.context.scene.render.filepath = os.path.join(dir, 'newPic', str(argv[3]) + ".png") 
#bpy.context.scene.render.resolution_x = w #perhaps set resolution in code
#bpy.context.scene.render.resolution_y = h
bpy.ops.render.render(write_still = True)
