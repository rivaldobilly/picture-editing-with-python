def change_contrast(image, value):
    F = 259 * (value + 255) / 255 / (259 - value)  # contrast correction factor
    for row in image:
        for column in row:
            for color in column:
                color = F * (color - 128) + 128
    return image
