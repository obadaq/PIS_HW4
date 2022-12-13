# stitching HW "image processing
import os
import cv2 as cv


# reading all images paths
imPaths =[]
data_folder = os.path.join(os.getcwd(), 'test_images')
for root, folder, files in os.walk(data_folder):
        for file in files:
            path = os.path.join(root, file)
            imPaths.append(path)

img1 = cv.imread(imPaths[0], cv.IMREAD_COLOR)
img2 = cv.imread(imPaths[1], cv.IMREAD_COLOR)

img1_size = img1.shape
img2_size = img2.shape

cv.imshow(img1)
print(img2_size)
'''
w1 = img1_size[0]
h1 = img1_size[1]

w2 = img2_size[0]
h2 = img2_size[1]

pxl = img1.getpixel(0, 0)
print(pxl)

'''
