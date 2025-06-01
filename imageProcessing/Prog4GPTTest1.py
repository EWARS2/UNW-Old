from PIL import Image, ImageFilter, ImageOps
import numpy as np

def emboss_filter(image):
    # Apply an emboss convolution filter
    kernel = [
        [-2, -1,  0],
        [-1,  1,  1],
        [ 0,  1,  2]
    ]
    emboss_image = image.filter(ImageFilter.Kernel((3, 3), sum(kernel, []), scale=1))
    return emboss_image

def sepia_filter(image):
    # Apply a sepia tone to the image
    sepia_image = ImageOps.colorize(image.convert("L"), "#704214", "#FFC0A8")
    return sepia_image

def negative_filter(image):
    # Apply a negative effect by inverting the image colors
    negative_image = ImageOps.invert(image.convert("RGB"))
    return negative_image

def apply_filter(image, filter_choice):
    # Choose the filter based on user input
    if filter_choice == 1:
        return emboss_filter(image)
    elif filter_choice == 2:
        return sepia_filter(image)
    elif filter_choice == 3:
        return negative_filter(image)
    else:
        print("Invalid choice. Defaulting to original image.")
        return image

def main():
    # Load the image
    image_path = input("Enter the path to your image: ")
    try:
        image = Image.open(image_path)
    except IOError:
        print("Unable to open image. Please check the path.")
        return

    # Show original image
    image.show(title="Original Image")

    # Display filter options
    print("Choose a filter to apply:")
    print("1 - Emboss")
    print("2 - Sepia")
    print("3 - Negative")

    # Get user input for filter selection
    try:
        filter_choice = int(input("Enter filter number (1, 2, or 3): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Apply chosen filter
    filtered_image = apply_filter(image, filter_choice)

    # Show the filtered image
    filtered_image.show(title="Filtered Image")

if __name__ == "__main__":
    main()
