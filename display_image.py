import matplotlib.pyplot as plt
from compute_edge import *


def display_image(image, mask):
    # if using Spyder, please go to "Tools -> Preferences -> IPython console -> Graphics -> Graphics Backend" and select "inline"
    tmp_img = image.copy()
    edge = compute_edge(mask)
    for r in range(len(image)):
        for c in range(len(image[0])):
            if edge[r][c] == 1:
                tmp_img[r][c][0] = 255
                tmp_img[r][c][1] = 0
                tmp_img[r][c][2] = 0

    plt.imshow(tmp_img)
    plt.axis('off')
    plt.show()
    print("Image size is", str(len(image)), "x", str(len(image[0])))
