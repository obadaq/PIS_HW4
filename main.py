# stitching HW "image processing
import os
from PIL import Image
import numpy as np


# reading all images paths
imPaths =[]
data_folder = os.path.join(os.getcwd(), 'test_images')
for root, folder, files in os.walk(data_folder):
        for file in files:
            path = os.path.join(root, file)
            imPaths.append(path)

img1 = Image.open(imPaths[0])
img2 = Image.open(imPaths[1])

img1_size = img1.size
img2_size = img2.size
print(img1_size,img2_size)
w1 = img1_size[0]
h1 = img1_size[1]

w2 = img2_size[0]
h2 = img2_size[1]

px1 = img1.load()
px2 = img2.load()

cpx1 = []
cpx2 = []
for i in range(0,w1):
    cpx1.append(px1[i,h1-1])
    cpx2.append(px2[i,0])

ary1 = np.array(cpx1)
ary2 = np.array(cpx2)

subbb = np.subtract(ary1, ary2)

print(subbb)

rms = np.sqrt(np.mean(subbb**2))
print(rms)



