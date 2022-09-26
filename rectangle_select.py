import numpy as np


def rectangle_select(image, x, y):
    mask = np.zeros(len(image), len(image[0]))
    for r in range(x[0], x[1]+1):
        for c in range(y[0], y[1]+1):
            mask[r, c] = 1
    return mask
