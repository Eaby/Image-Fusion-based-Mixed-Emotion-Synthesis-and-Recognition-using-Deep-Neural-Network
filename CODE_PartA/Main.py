from PIL import Image #We use Python Imaging Library for image processing capabilities to your Python interpreter
image = Image.open('KL.SU3.166.tiff')   # assigning the image to image variable
#image.show()   # viewing the image in a new window
#print(image.size) # printing the image size
new_image1 = image.resize((128, 128))  # Resizing the image size to 128x128
new_image1.save('KL.SU3.166_128_128.jpg')   # saving the new image of size 128x128
# print(new_image.size)                  # printing the new image of size 128x128
image = Image.open('KL.SA3.163.tiff')
new_image2 = image.resize((128, 128))  # Resizing the image size to 128x128
new_image2.save('KL.SA3.163_128_128.jpg')   # saving the new image of size 128x128
image_SU_128_128 = Image.open('KL.SU3.166_128_128.jpg')
image_SA_128_128 = Image.open('KL.SA3.163_128_128.jpg')
Canvas_copy_256_256 = Image.open('256_256_blank_canvas.jpg')
box1 = (0, 0, 127, 80)
box2 = (127,64,64,127)
cropped_image1 = image_SU_128_128.crop(box1)
cropped_image1.save('cropped_image_FE_128_128.jpg')
image_HA_32_32_copy = image_SA_128_128.copy()
position = (0,0)
position1 = (0,127)
position2 = (127,0)
position3 = (127,127)
image_HA_32_32_copy.paste(cropped_image1, position)
Canvas_copy_256_256.paste(new_image1, position)
Canvas_copy_256_256.paste(new_image2, position2)
Canvas_copy_256_256.paste(cropped_image1, position1)
Canvas_copy_256_256.paste(image_HA_32_32_copy, position3)
Canvas_copy_256_256.save('Canvas_copy_256_256.jpg')
Canvas_copy_256_256.show()

