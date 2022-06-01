# By Eaby Kollonoor Babu
# import pandas as pd
#
# data= pd.read_csv("filenames.csv")
# A1=data.loc[:,"A1"]
# A2=data.loc[:,"A2"]
# B1=data.loc[:,"B1"]
# B2=data.loc[:,"B2"]
# C1=data.loc[:,"C1"]
# C2=data.loc[:,"C2"]
# D1=data.loc[:,"D1"]
# D2=data.loc[:,"D2"]
# E1=data.loc[:,"E1"]
# E2=data.loc[:,"E2"]
# F1=data.loc[:,"F1"]
# F2=data.loc[:,"F2"]
# G1=data.loc[:,"G1"]
# G2=data.loc[:,"G2"]
# H1=data.loc[:,"H1"]
# H2=data.loc[:,"H2"]
# I1=data.loc[:,"I1"]
# I2=data.loc[:,"I2"]
# J1=data.loc[:,"J1"]
# J2=data.loc[:,"J2"]
# print(A1[5])

import cv2
from PIL import Image
import numpy as np

s = 256


def apply_brightness_contrast(input_img, brightness=0, contrast=0):
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow) / 255
        gamma_b = shadow

        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()

    if contrast != 0:
        f = 131 * (contrast + 127) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127 * (1 - f)

        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    return buf

image = cv2.imread('C:/Users/Dell/Desktop/My Northumbria University Documents/Academic data/My Research Data/IJCNN_Project/JAFFE/For process/KA.NE1.tiff')

font = cv2.FONT_HERSHEY_SIMPLEX
fcolor = (0, 0, 0)

blist = [0, -127, 127, 0, 0, 64]  # list of brightness values
clist = [0, 0, 0, -64, 64, 64]  # list of contrast values

out = np.zeros((s * 2, s * 3, 3), dtype=np.uint8)

for i, b in enumerate(blist):
    c = clist[i]
    print('b, c:  ', b, ', ', c)
    row = s * int(i / 3)
    col = s * (i % 3)

    print('row, col:   ', row, ', ', col)

    out[row:row + s, col:col + s] = apply_brightness_contrast(image, b, c)
    msg = 'b %d' % b
    cv2.putText(out, msg, (col, row + s - 22), font, .7, fcolor, 1, cv2.LINE_AA)
    msg = 'c %d' % c
    cv2.putText(out, msg, (col, row + s - 4), font, .7, fcolor, 1, cv2.LINE_AA)

    cv2.putText(out, 'OpenCV', (260, 30), font, 1.0, fcolor, 2, cv2.LINE_AA)

cv2.imwrite('out.tiff', out)

