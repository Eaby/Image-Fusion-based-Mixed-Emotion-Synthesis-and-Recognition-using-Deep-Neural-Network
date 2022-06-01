# THIS PROGRAM CAN BE USED TO CONVERT IMAGE DATASET FOLDER TO CSV FILE FOR TRAINING PURPOSES
from PIL import Image
import numpy as np
import sys
import os
import csv


# Useful function
def createFileList(myDir, format='.tiff'):
    fileList = []
    print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    return fileList


# load the original image
myFileList = createFileList(
    '"UPDATE YOUR FOLDER NAME HERE"/MESR_ProjectCODE/mxfer2022-master/mxfer2022-master/our_JAFFE_dataset')

for file in myFileList:
    print(file)
    img_file = Image.open(file)
    newsize = (48, 48)
    img_file = img_file.resize(newsize)
    # img_file.show()

    # get original image parameters...
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode

    # Make image Greyscale
    img_grey = img_file.convert('L')
    # img_grey.save('result.png')
    # img_grey.show()

    # Save Greyscale values
    value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
    value = value.flatten()
    print(value)
    with open("img_pixels.csv", 'a', newline='') as F:
        writer = csv.writer(F, delimiter=' ')
        writer.writerow(value)
