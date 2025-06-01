# Title: Program #3
# Author: Ethan Reed
# Class: Programming I: Java
# Professor Jonathan Zderad

"""
Program #3
Consider various image enhancements (crop, transpose, resize, rotate,
B&W, color, contrast, sharpness, brightness, transform, channel splitting).
Write a program with a simple menu that allow a user to select from one of at least five image enhancements.
The program should display the original image and the enhanced image.
"""

import os.path
import traceback
from PIL import Image


# From "Image_Processing_008" in Moodle
def make_image(data, resolution):
    image = Image.new("RGB", resolution)
    image.putdata(data)
    return image


# Fast clamp function, found here:
# https://stackoverflow.com/questions/18609360/get-a-value-between-min-and-max-values-in-python
def clamp(val, min_val, max_val):
    return min_val if val < min_val else max_val if val > max_val else val


def exit_program(image):
    image.close()
    print("Exiting...")
    exit()


def crop(image):
    left = int(input("Crop coordinate for left:"))
    top = int(input("Crop coordinate for top:"))
    right = int(input("Crop coordinate for right:"))
    bottom = int(input("Crop coordinate for bottom:"))
    return image.crop((left, top, right, bottom))


def transpose(image):
    print("Flip options:")
    print("1. Vertical")
    print("2. Horizontal")
    print("3. Transpose")
    print("4. Transverse")
    choice = int(input("Choice:"))
    edit = None  # TODO: Cleanup choice implementation
    if choice == 1:
        edit = Image.Transpose.FLIP_TOP_BOTTOM
    elif choice == 2:
        edit = Image.Transpose.FLIP_LEFT_RIGHT
    elif choice == 3:
        edit = Image.Transpose.TRANSPOSE
    elif choice == 4:
        edit = Image.Transpose.TRANSVERSE

    return image.transpose(edit)


def resize(image):
    width = int(input("Width:"))
    height = int(input("Height:"))
    return image.resize([width, height])


def rotate(image):
    angle = float(input("Angle:"))
    return image.rotate(angle)


def black_white(image):
    return image


def color(image):
    return image


def contrast(image):
    return image


def sharpness(image):
    return image


def brightness(image):
    width, height = image.size
    image_data = image.load()
    return_data = []

    intensity = int(input("(Ideally 0-255) Intensity:"))

    for y in range(height):
        for x in range(width):
            rgb = image_data[x, y]
            r = (rgb[0] + intensity)
            g = (rgb[1] + intensity)
            b = (rgb[2] + intensity)
            r = clamp(r, 0, 255)
            g = clamp(g, 0, 255)
            b = clamp(b, 0, 255)
            return_data.append((r, g, b))

    return make_image(return_data, image.size)


# TODO: I don't understand how Pillow transform works. This is broken right now.
def transform(image):
    width = int(input("Width:"))
    height = int(input("Height:"))
    print("Method options:")
    print("1. Affine")
    print("2. Extent")
    print("3. Perspective")
    print("4. Quad")
    print("5. Mesh")
    choice = int(input("Choice:"))
    method = None  # TODO: Cleanup choice implementation
    if choice == 1:
        method = Image.Transform.AFFINE
    elif choice == 2:
        method = Image.Transform.EXTENT
    elif choice == 3:
        method = Image.Transform.PERSPECTIVE
    elif choice == 4:
        method = Image.Transform.QUAD
    elif choice == 5:
        method = Image.Transform.MESH

    return image.transform((width, height), method)


def channel_splitting(image):
    return image


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
               crop,
               transpose,
               resize,
               rotate,
               # black_white,
               # color,
               # contrast,
               # sharpness,
               brightness
               # transform,
               # channel_splitting
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
