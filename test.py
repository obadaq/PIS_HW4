# stitching HW "image processing"
# the code runs in three steps
# 1.read images     2. make the user select an image from the test_images folder
# 3.test images sides to find the similarities  4. merge in order of max similarities (min RMS)
# main.py have the functions that satisfies the previous steps

from main import read_images_paths, test_sides, merge_images
from PIL import Image


paths = read_images_paths('test_images')

i = 1
for path in paths:
    print(i, '. ', path)
    i += 1

user_ch = int(input('Select an Image path to find and stitch the other half ::: '))
path1 = paths[user_ch - 1]

if user_ch % 2:
    path2 = paths[user_ch]
else:
    path2 = paths[user_ch - 2]


img1 = Image.open(path1)
img2 = Image.open(path2)

common_side = test_sides(img1, img2)
merge_images(img1, img2, common_side).show()
