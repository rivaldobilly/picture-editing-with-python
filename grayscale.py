def grayscale(image):
    for row in image:
        for column in row:
            temp_value = int(0.3 * column[0] +
                             0.59 * column[1] + 0.11 * column[2])
            for i in range(3):
                column[i] = temp_value
    return image
