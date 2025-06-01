#this illustrates image processing with PIL
from PIL import Image
from PIL import ImageEnhance
import matplotlib.pyplot as plt
import numpy as np
import time

#1 create images and get info
image = Image.open("example.tiff")
another_image = Image.open("filter.tiff")
#image.show()
#print (image.size)
#print (image.format)
#print (image.mode)
#print (another_image.size)
#print (another_image.format)
#print (another_image.mode)


#2 crop image
left = 100
right = 550
top = 50
bottom = 380
crop_image = image.crop((left,top,right,bottom))
#crop_image.show()

#3 Transpose Image
transpose_image = image.transpose(Image.ROTATE_90)
#transpose_image.show()

#4 Resize Image
newsize = (200,200)
resized_image = image.resize(newsize, Image.BICUBIC)
#resized_image.show()

#5 Rotate Image
angle = 30
rotated_image = image.rotate(angle)
#rotated_image.show()

#6 B&W Image
bw_image = image.convert('L')
#bw_image.show()

#7 Image Enhancement
image1 = ImageEnhance.Color(image).enhance(0.1)
image2 = ImageEnhance.Contrast(image).enhance(7)
image3 = ImageEnhance.Sharpness(image).enhance(2.3)
image4 = ImageEnhance.Brightness(image).enhance(1)
#image1.show()
#image2.show()
#image3.show()
#image4.show()

#8 image blending // does not work
image5=image.copy()
image6=another_image.copy()
image6=image6.resize(image5.size)
print (image5.size)
print (image6.size)
#image_blend = Image.blend(image5, image6, 0.5)
#image_blend.show()

#9 transform
image7 = image.copy()
xsz = image7.size[0]/2
ysz = image7.size[1]/2
image7 = image7.transform(image7.size, Image.AFFINE,(1,-0.5, xsz,0,1,0))
#image7.show()
image8=image.copy()
image8 = image8.transform(image8.size, Image.EXTENT,(50,50,xsz,ysz))
#image8.show()

#10 channel splitting
image9 = image.copy()
rgb = image9.split()
image9 = Image.merge("RGB", (rgb[1],rgb[0],rgb[2]))
#image9.show()

