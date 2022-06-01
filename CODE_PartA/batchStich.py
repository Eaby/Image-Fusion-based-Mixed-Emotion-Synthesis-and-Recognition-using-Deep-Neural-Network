# developed by Eaby Kollonoor Babu
import pandas as pd
from PIL import Image, ImageDraw, ImageFont #We use Python Imaging Library for image processing capabilities to your Python interpreter
import os
import sys

data= pd.read_csv("filenames.csv")
A1=data.loc[:,"A1"]
A2=data.loc[:,"A2"]
B1=data.loc[:,"B1"]
B2=data.loc[:,"B2"]
C1=data.loc[:,"C1"]
C2=data.loc[:,"C2"]
D1=data.loc[:,"D1"]
D2=data.loc[:,"D2"]
E1=data.loc[:,"E1"]
E2=data.loc[:,"E2"]
F1=data.loc[:,"F1"]
F2=data.loc[:,"F2"]
G1=data.loc[:,"G1"]
G2=data.loc[:,"G2"]
H1=data.loc[:,"H1"]
H2=data.loc[:,"H2"]
I1=data.loc[:,"I1"]
I2=data.loc[:,"I2"]
J1=data.loc[:,"J1"]
J2=data.loc[:,"J2"]
#A=A1[5]+('.tiff')  # testing line
#image = Image.open((os.path.join("C:/Users/Dell/Desktop/My Northumbria University Documents/Academic data/My Research Data/MESR_Project/JAFFE/For process", A)))   # testing line
#image.show()
#print(A1[5])
box1 = (0, 0, 255, 160)
box2 = (255,127,127,255)
position = (0,0)
position2 = (127,0)
Canvas_copy_256_256 = Image.open('256_256_blank_canvas.jpg')
# T = A1[1] + ('.tiff')
# B = A2[1] + ('.tiff')
# print(T)
# print(B)
# imageT= Image.open((os.path.join("C:/Users/Dell/Desktop/My Northumbria University Documents/Academic data/My Research Data/MESR_Project/JAFFE/For process", T)))
# imageB= Image.open((os.path.join("C:/Users/Dell/Desktop/My Northumbria University Documents/Academic data/My Research Data/MESR_Project/JAFFE/For process", B)))
# cropped_imageT = imageT.crop(box1)
# imageB.paste(cropped_imageT, position)
# imageB.show()




i=0
for i in range(0,42):
    T = J1[i] + ('.tif')
    B = J2[i] + ('.tif')
    imageT= Image.open((os.path.join("C:/Users/Dell/Desktop/My Northumbria University Documents/Academic data/My Research Data/MESR_Project/JAFFE/For process/MonotoneImages", T)))
    imageB= Image.open((os.path.join("C:/Users/Dell/Desktop/My Northumbria University Documents/Academic data/My Research Data/MESR_Project/JAFFE/For process/MonotoneImages", B)))
    cropped_imageT = imageT.crop(box1)
   # cropped_imageB = imageB.crop(box2)
    imageB.paste(cropped_imageT, position)
   # Canvas_copy_256_256.paste(cropped_imageB, position2)
    fileName= 'C_'+J1[i]+'.'+J2[i]
    print(fileName)
    width, height = imageB.size
    draw = ImageDraw.Draw(imageB)
    text = fileName
    textwidth, textheight = draw.textsize(text)
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin
    draw.text((x, y), text)
   # imageB.show()
    imageB.save("C:/Users/Dell/Desktop/My Northumbria University Documents/Academic data/My Research Data/MESR_Project/JAFFE/For process/output"+fileName+'.tiff')