from PIL import Image
import random

MAX_COLOR_VALUE = 256
MAX_BIT_VALUE = 8

def make_image(data, resolution):
    image = Image.new("RGB", resolution)
    image.putdata(data)
    return image

def tint(image_to_hide,dred,dgreen,dblue):
    width, height = image_to_hide.size
    hide_image = image_to_hide.load()
    data = []

    for y in range(height):
        for x in range(width):
            rgb_hide = hide_image[x, y]
            r_hide = rgb_hide + dred
            g_hide = rgb_hide + dgreen
            b_hide = rgb_hide + dblue
            data.append((r_hide,g_hide,b_hide))
    return make_image(data, image_to_hide.size)

def blur(image_to_hide):
    width, height = image_to_hide.size
    hide_image = image_to_hide.load()
    data = []

    for y in range(height):
        for x in range(width):
            rgb_hide = hide_image[x, y]
            if ((x<width-5) and (x != 0) and (y!=0) and (y<width-10)):
                rgb_new = hide_image[x-5,y-5]
                r_hide = int((rgb_hide[0] + rgb_new[0])/2)
                g_hide = int((rgb_hide[1] + rgb_new[1])/2)
                b_hide = int((rgb_hide[2] + rgb_new[2])/2)
            else:
                r_hide = rgb_hide[0]
                g_hide = rgb_hide[1]
                b_hide = rgb_hide[2]
            data.append((r_hide,g_hide,b_hide))
    return make_image(data, image_to_hide.size)


def noise(image_to_hide):
    width, height = image_to_hide.size
    hide_image = image_to_hide.load()
    data = []

    for y in range(height):
        for x in range(width):
            rgb_hide = hide_image[x, y]
            if (x%2 ==0) and (y%2 == 0):
                r_hide = random.randint(10, 250)
                g_hide = random.randint(10, 250)
                b_hide = random.randint(10, 250)
            else:

                r_hide = rgb_hide[0]
                g_hide = rgb_hide[1]
                b_hide = rgb_hide[2]
            data.append((r_hide,g_hide,b_hide))
    return make_image(data, image_to_hide.size)

def stripes(image_to_hide):
    width, height = image_to_hide.size
    hide_image = image_to_hide.load()
    data = []

    for y in range(height):
        for x in range(width):
            rgb_hide = hide_image[x, y]
            r_hide = (x+y) % 255
            g_hide = rgb_hide[1]
            b_hide = rgb_hide[2]
            data.append((r_hide,g_hide,b_hide))
    return make_image(data, image_to_hide.size)

#mainline
#open images
image_to_hide_path = "./example.tiff"
encoded_image_path = "./encoded.tif"
image_to_hide = Image.open(image_to_hide_path)

#menu
print("------ Image Processing Menu -------")
print("1. Tint")
print("2. Blur")
print("3. Noise")
print("4. Stripes")
choice = int(input("What option?"))
if choice == 1:
    r = int(input("Enter red tint .."))
    g = int(input("Enter green tint .."))
    b = int(input("Enter blue tint.."))
    tint(image_to_hide,r,g,b).save(encoded_image_path)
if choice == 2:
    blur (image_to_hide).save(encoded_image_path)
if choice == 3:
    noise(image_to_hide).save(encoded_image_path)
if choice == 4:
    stripes(image_to_hide).save(encoded_image_path)

