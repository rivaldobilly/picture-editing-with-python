
import matplotlib.image as mpimg
import numpy as np


def save_image(filename, image):
    img = image.astype(np.uint8)
    mpimg.imsave(filename, img)
