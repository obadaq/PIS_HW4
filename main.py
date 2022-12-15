import os
from PIL import Image
import numpy as np


def read_images_paths(folder_name):
    # reading all images paths
    im_paths = []
    data_folder = os.path.join(os.getcwd(), folder_name)
    for root, folder, files in os.walk(data_folder):
        for file in files:
            path = os.path.join(root, file)
            im_paths.append(path)
    return im_paths


def rms(ary1, ary2):
    # compute rms values for two arrays representing each side
    subb = np.subtract(ary1, ary2)
    rms_val = np.sqrt(np.mean(np.power(subb, 2)))
    return rms_val


def test_sides(img1, img2):
    # test al possible sides in two images to find MIN RMS ( MAX similarity )
    (width1, height1) = img1.size
    (width2, height2) = img2.size
    rms_lis = []
    img1_array = np.asarray(img1.convert('L'))
    img2_array = np.asarray(img2.convert('L'))

    if width1 == width2:
        side1 = img1_array[0, :]
        side2 = img2_array[height2 - 1:, :]
        rms_lis.append(rms(side1, side2))

        side1 = img1_array[height1 - 1, :]
        side2 = img2_array[0, :]
        rms_lis.append(rms(side1, side2))
    else:
        rms_lis.append(1000000)
        rms_lis.append(1000000)

    if height1 == height2:
        side1 = img1_array[:, 0]
        side2 = img2_array[:, width2 - 1]
        rms_lis.append(rms(side1, side2))

        side1 = img1_array[:, width1 - 1]
        side2 = img2_array[:, 0]
        rms_lis.append(rms(side1, side2))
    else:
        rms_lis.append(1000000)
        rms_lis.append(1000000)

    min_rms_pos = rms_lis.index(min(rms_lis))

    return min_rms_pos


def merge_images(image1, image2, pos):
    (width1, height1) = image1.size
    (width2, height2) = image2.size

    if pos == 0 or pos == 1:
        result_width = max(width1, width2)
        result_height = height1 + height2
    else:
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
