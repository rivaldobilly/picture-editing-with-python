import numpy as np

# ------------------------------

# Imported Features

from blur_effect import *
from change_brightness import *
from change_contrast import *
from compute_edge import *
from display_image import *
from edge_detection import *
from embossed import *
from grayscale import *
from load_image import *
from magic_wand_select import *
from rectangle_select import *
from save_image import *


def menu():
    while True:
        input_user = input('What do you want to do?'
                           '\n e - exit'
                           '\n l - load a picture'
                           '\n'
                           '\n Your choice: ')
        if input_user == 'e':
            print('Thank you for using our program!')
            break
        elif input_user == 'l':
            file_name = input('Enter the filename of image you want to edit:'
                              '\n')
            image = load_image(file_name)
            display_image(image, mask)
            break
        else:
            print('Please type the right input.')

    while input_user != 'e':
        input_user = input('What do you want to do?'
                           '\n e - exit'
                           '\n l - load a picture'
                           '\n s - save the current picture'
                           '\n 1 - adjust brightness'
                           '\n 2 - adjust contrast'
                           '\n 3 - apply grayscale'
                           '\n 4 - apply blur'
                           '\n 5 - edge detection'
                           '\n 6 - embossed'
                           '\n 7 - rectangle select'
                           '\n 8 - magic wand select'
                           '\n'
                           '\n Your choice: ')

        if input_user == 'e':
            print('Thank you for using our program!')

        elif input_user == 'l':
            file_name = input('Enter the filename of image you want to edit:'
                              '\n')
            image, mask = load_image(file_name)
            display_image(image, mask)

        elif input_user == 's':
            file_name = input('Enter the file name of image you want to save:'
                              '\n')
            save_image(file_name, image)

        elif input_user == '1':
            val = int(input('Enter the amount of brightness you want to apply:'
                            '\n'))
            image = change_brightness(image, val)
            display_image(image, mask)

        elif input_user == '2':
            val = input('Enter the amount of contrast you want to apply:'
                        '\n')
            image = change_contrast(image, val)
            display_image(image, mask)

        elif input_user == '3':
            image = grayscale(image)
            display_image(image, mask)

        elif input_user == '4':
            image = blur_effect(image)
            display_image(image, mask)

        elif input_user == '5':
            image = edge_detection(image)
            display_image(image, mask)

        elif input_user == '6':
            image = embossed(image)
            display_image(image, mask)

        elif input_user == '7':
            while True:
                x_left = input('Enter leftmost x-coordinate: ')
                x_right = input('Enter rightmost x-coordinate: ')
                if 0 <= x_left <= x_right < len(image[0]):
                    break
                print('Please enter the correct amount.')
            while True:
                y_bottom = input('Enter lowest y-coordinate: ')
                y_top = input('Enter upmost y-coordinate: ')
                if 0 <= y_bottom <= y_top < len(image):
                    break
                print('Please enter the correct amount.')
            mask = rectangle_select(image, [y_top, x_left], [
                y_bottom, x_right])
            display_image(image, mask)

        elif input_user == '8':
            while True:
                x = input('Enter x-coordinate: ')
                if 0 <= x < len(image[0]):
                    break
                print('Please enter the correct amount.')
            while True:
                y = input('Enter y-coordinate: ')
                if 0 <= y < len(image):
                    break
                print('Please enter the correct amount.')
            threshold = input('Enter threshold: ')
            mask = magic_wand_select(image, [x, y], threshold)
            display_image(image, mask)
        else:
            print('Please type the right input.')


if __name__ == "__main__":
    menu()
