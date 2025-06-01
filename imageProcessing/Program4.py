# Title: Program #4
# Author: Ethan Reed
# Class: Programming I: Java
# Professor Jonathan Zderad

"""
Program #4
Create a program that allows the user to select from one of at least three filters.
The filters must be different from the one's done in class and at least one of the filters must be a convolution.
The program will display the original image and the filtered image.
"""

import os.path
import traceback
from PIL import Image
from random import randint


# From "Image_Processing_008" in Moodle
def make_image(data, resolution):
    image = Image.new("RGB", resolution)
    image.putdata(data)
    return image


# Fast clamp function, found here:
# https://stackoverflow.com/questions/18609360/get-a-value-between-min-and-max-values-in-python
def clamp(val, min_val, max_val):
    return min_val if val < min_val else max_val if val > max_val else val


# Modified from "Convolution_13" in Moodle
def convolve(list1, list2):
    answer = 0
    for x in range(3):
        for y in range(3):
            answer = answer + int(list1[x][y] * list2[x][y])
    return clamp(answer, 0, 255)


def exit_program(image):
    image.close()
    print("Exiting...")
    exit()


# This is a better implementation than what's found in "Image_Processing_008" in Moodle
def noise(image):
    width, height = image.size
    image_data = image.load()
    return_data = []

    intensity = int(input("(Ideally 0-255) Intensity:"))

    for y in range(height):
        for x in range(width):
            rgb = image_data[x, y]
            r = (rgb[0] + randint(-intensity, intensity))
            g = (rgb[1] + randint(-intensity, intensity))
            b = (rgb[2] + randint(-intensity, intensity))
            r = clamp(r, 0, 255)
            g = clamp(g, 0, 255)
            b = clamp(b, 0, 255)
            return_data.append((r, g, b))

    return make_image(return_data, image.size)


def invert(image):
    width, height = image.size
    image_data = image.load()
    return_data = []

    for y in range(height):
        for x in range(width):
            rgb = image_data[x, y]
            r = (255 - rgb[0])
            g = (255 - rgb[1])
            b = (255 - rgb[2])
            return_data.append((r, g, b))

    return make_image(return_data, image.size)


# Adapted from "Convolution_13" in Moodle
def convolution(image):
    width, height = image.size
    image_data = image.load()
    return_data = []

    # my_convolution = [[0.2, -1.6, 0.4], [0.3, 0.7, 0.2], [-1, 0.8, 0.9]]

    my_convolution = []
    print("Enter 3x3 convolution matrix: ")
    for y in range(3):
        line = []
        for x in range(3):
            try:
                response = float(input("Enter value for [x,y] " + str([x + 1, y + 1]) + " :"))
            except ValueError:
                print("Error with input, assuming 0...")
                response = 0
            line.append(response)
        my_convolution.append(line)

    print("Using convolution:")
    print(my_convolution)

    for y in range(height):
        for x in range(width):
            # Test border
            is_border = (x == 0) or (y == 0) or (y == height - 1) or (x == width - 1)

            if not is_border:
                pixel_a = image_data[x - 1, y - 1]
                pixel_b = image_data[x, y - 1]
                pixel_c = image_data[x + 1, y - 1]
                pixel_d = image_data[x - 1, y]
                pixel_e = image_data[x, y]
                pixel_f = image_data[x + 1, y]
                pixel_g = image_data[x - 1, y + 1]
                pixel_h = image_data[x, y + 1]
                pixel_i = image_data[x + 1, y + 1]

                rgb = []
                for j in range(3):
                    a = pixel_a[j]
                    b = pixel_b[j]
                    c = pixel_c[j]
                    d = pixel_d[j]
                    e = pixel_e[j]
                    f = pixel_f[j]
                    g = pixel_g[j]
                    h = pixel_h[j]
                    i = pixel_i[j]
                    patch = [[a, b, c], [d, e, f], [g, h, i]]
                    rgb.append(convolve(my_convolution, patch))
                r = rgb[0]
                g = rgb[1]
                b = rgb[2]
            else:
                r = g = b = 0
            return_data.append((r, g, b))

    return make_image(return_data, image.size)


def main():
    # path = "./example.tiff"
    path = input("Path to file: ")

    # Load image file
    try:
        original_image = Image.open(path)
        print("Loaded.")
    except FileNotFoundError:
        print("File not found, quitting...")
        return

    # Create copy of data to manipulate.
    edited_image = original_image
    filename, file_extension = os.path.splitext(path)
    edited_path = filename + "_edited" + file_extension
    original_image.show(title="Original Image")

    # List of functions.
    # Used to create a pseudo case structure.
    options = [exit_program,
               noise,
               invert,
               convolution
               ]

    # Mainloop
    while True:
        print()
        print("Resolution: " + str(edited_image.size))

        # Formatted display of functions in options.
        # Example output of example_function():
        # 0. Example-Function
        print("Options:")
        for i in range(len(options)):
            print(f"{i: >2}. " + options[i].__name__.title().replace("_", "-"))

        # Get user's choice and run the according function.
        # Print errors reported from function.
        # Uses a pseudo case structure.
        try:
            choice = int(input("Choice:"))
            edited_image = options[choice](edited_image)
        except Exception as exc:  # Pass error to console, but don't crash
            print(traceback.format_exc())
            print(exc)

        edited_image.save(edited_path)
        edited_image.show(edited_path)


# Call the main func
if __name__ == '__main__':
    main()
