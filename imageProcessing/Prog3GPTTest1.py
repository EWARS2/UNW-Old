from PIL import Image, ImageEnhance, ImageOps
import sys


def display_images(original, enhanced, title):
    original.show(title="Original Image")
    enhanced.show(title=title)


def crop_image(image):
    width, height = image.size
    cropped = image.crop((width // 4, height // 4, 3 * width // 4, 3 * height // 4))
    display_images(image, cropped, "Cropped Image")


def resize_image(image):
    resized = image.resize((image.width // 2, image.height // 2))
    display_images(image, resized, "Resized Image")


def rotate_image(image):
    rotated = image.rotate(90)
    display_images(image, rotated, "Rotated Image")


def convert_to_bw(image):
    bw_image = image.convert("L")
    display_images(image, bw_image, "Black & White Image")


def adjust_brightness(image):
    enhancer = ImageEnhance.Brightness(image)
    bright_image = enhancer.enhance(1.5)
    display_images(image, bright_image, "Brightness Enhanced Image")


def main():
    image_path = input("Enter the path to your image file: ")
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit()

    while True:
        print("\nImage Enhancement Menu:")
        print("1. Crop Image")
        print("2. Resize Image")
        print("3. Rotate Image")
        print("4. Convert to Black & White")
        print("5. Adjust Brightness")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            crop_image(image)
        elif choice == '2':
            resize_image(image)
        elif choice == '3':
            rotate_image(image)
        elif choice == '4':
            convert_to_bw(image)
        elif choice == '5':
            adjust_brightness(image)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
