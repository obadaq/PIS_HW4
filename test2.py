
import os
from PIL import Image
import numpy as np

img1 = Image.open('test_images\eifel.jpg')
img2 = Image.open('test_images\eifel02.jpg')


(width1, height1) = img1.size
(width2, height2) = img1.size

img1_array = np.asarray(img1.convert('L'))
img2_array = np.asarray(img2.convert('L'))
side1 = img1_array[0:1,:]
side2 = img2_array[height2-2:height2-1,:]

print(side1)

print(side2)