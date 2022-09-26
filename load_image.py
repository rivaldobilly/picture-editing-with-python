import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def load_image(filename):
    img = mpimg.imread(filename)
    if len(img[0][0]) == 4:  # if png file
        img = np.delete(img, 3, 2)
    # if stored as float in [0,..,1] instead of integers in [0,..,255]
    if type(img[0][0][0]) == np.float32:
        img = img*255
        img = img.astype(np.uint8)
    # create a mask full of "1" of the same size of the laoded image
    mask = np.ones((len(img), len(img[0])))
    img = img.astype(np.int32)
    return img, mask
