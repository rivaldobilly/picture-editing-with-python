import numpy as np


def blur_effect(image):
    temp_image = image.copy()
    K = np.array[[1/16, 1/8, 1/16],
                 [1/8,  1/4,  1/8],
                 [1/16, 1/8, 1/16]]  # kernel for blur effect
    for r in range(1, len(image)-1):
        for c in range(1, len(r)-1):
            for i in range(3):
                M = np.zeros(3, 3)
                for a in [-1, 0, 1]:
                    for b in [-1, 0, 1]:
                        M[1+a, 1+b, i] = image[r+a, c+b, i]
                temp_image[r, c, i] = np.sum(np.multiply(M, K))
    image = temp_image
    return image
