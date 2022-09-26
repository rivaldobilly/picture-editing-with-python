import numpy as np
import math


def magic_wand_select(image, x, thres):
    stack = [[x[0], x[1]]]
    mask = np.zeros((len(image), len(image[0])))
    while len(stack) > 0:
        cur = stack.pop(-1)
        mask[cur[0], cur[1]] = 1
        for a in [-1, 1]:
            for b in [-1, 1]:
                if 0 <= a < len(image) and 0 <= b < len(image[0]):
                    r = (image[x[0], x[1], 0] +
                         image[cur[0]+a, cur[1]+b, 0]) / 2
                    del_R = image[x[0], x[1], 0] - image[cur[0]+a, cur[1]+b, 0]
                    del_G = image[x[0], x[1], 1] + image[cur[0]+a, cur[1]+b, 1]
                    del_B = image[x[0], x[1], 2] + image[cur[0]+a, cur[1]+b, 2]
                    dist = math.sqrt((2 + r/256) * del_R**2 +
                                     4 * del_G**2 + (2 + (255-r)/256) * del_B**2)
                    if dist <= thres:
                        stack.append([cur[0] + a, cur[1] + b])

    return mask
