def change_brightness(image, value):
    for row in image:
        for column in row:
            for color in column:
                if color + value > 255:
                    color = 255
                elif color + value < 0:
                    color = 0
                else:
                    color += value
    return image

    # temp_image = image.copy()
    # for a in range(len(temp_image)):
    #     for b in range(len(temp_image[0])):
    #         for c in range(3):
    #             temp_image[a, b, c] = temp_image[a, b, c] + value

    #             # Error Check for the RGB values
    #             if temp_image[a, b, c] > 255:
    #                 temp_image[a, b, c] = 255
    #             elif temp_image[a, b, c] < 0:
    #                 temp_image[a, b, c] = 0

    # return temp_image
