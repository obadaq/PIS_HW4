# stitching HW "image processing
import os
from PIL import Image
import numpy as np

def read_images_paths(folder_name):
    # reading all images paths
    imPaths =[]
    data_folder = os.path.join(os.getcwd(), folder_name)
    for root, folder, files in os.walk(data_folder):
        for file in files:
             path = os.path.join(root, file)
             imPaths.append(path)
    return imPaths

def rms(lis1,lis2):

    ary1 = np.array(lis1)
    ary2 = np.array(lis2)
    subb = np.subtract(ary1, ary2)
    rms = np.sqrt(np.mean(np.power(subb,2)))
    return rms

def test_sides(w1,w2,h1,h2,img1px,img2px):
    cpx1 = []
    cpx2 = []
    rms_list = []

    if w1 == w2:
        for i in range(0,w1):
            cpx1.append(img1px[i,0])
            cpx2.append(img2px[i,h2-1])
        rms_list.append(rms(cpx1,cpx2))

        for i in range(0,w1):
            cpx1.append(img1px[i,h1-1])
            cpx2.append(img2px[i,0])
        rms_list.append(rms(cpx1,cpx2))
    else: 
        rms_list.append(1000000)
        rms_list.append(1000000)

    if h1 == h2:
        for i in range(0,h1):
            cpx1.append(img1px[0,i])
            cpx2.append(img2px[w2-1,i])
        rms_list.append(rms(cpx1,cpx2))
    
        for i in range(0,h1):
            cpx1.append(img1px[w1-1,i])
            cpx2.append(img2px[0,i])
        rms_list.append(rms(cpx1,cpx2))
    else: 
        rms_list.append(1000)
        rms_list.append(1000)
    print(rms_list)
    min_rms_pos = rms_list.index(min(rms_list))
    return min_rms_pos

def merge_images(image1, image2,pos):

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    if pos == 0 or pos ==1:
        result_width = max(width1, width2)
        result_height = height1 + height2
    elif pos == 2 or pos ==3:
        result_width = width1 + width2
        result_height = max(height1, height2)
    
    result = Image.new('RGB', (result_width, result_height))
    if pos == 0:
        result.paste(im=image1, box=(0, height2))
        result.paste(im=image2, box=(0, 0))
    elif pos == 1:
        result.paste(im=image1, box=(0, 0))
        result.paste(im=image2, box=(0, height1))
    elif pos == 2:
        result.paste(im=image1, box=(width2, 0))
        result.paste(im=image2, box=(0, 0))        
    elif pos == 3:
        result.paste(im=image1, box=(0, 0))
        result.paste(im=image2, box=(width1, 0))

    return result



paths = read_images_paths('test_images')
i=1
for path in paths:
    print( i , '. ', path)
    i += 1

user_ch = int(input('Select an Image path to find and stitch the other half ::: ')) 

path1 = paths[user_ch - 1]

if user_ch % 2:
    path2 = paths[user_ch]
else :
    path2 = paths[user_ch - 2]

img1 = Image.open(path1)
img2 = Image.open(path2)

img1.show()
img2.show()
(width1, height1) = img1.size
(width2, height2) = img2.size

print(width1,width2,height1,height2)

rrr = test_sides(width1,width2,height1,height2,img1.load(),img2.load())
merge_images(img1,img2,rrr).show()

print(rrr)


