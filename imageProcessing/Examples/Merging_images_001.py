from PIL import Image

#mainline
#open images
image_path = "./example.tiff"
second_image_path = "./filter.tiff"
merged_path = "./encoded.tiff"
image_open = Image.open(image_path)
second_image_open = Image.open(second_image_path)

#menu

image_load = image_open.load()
second_image_load = second_image_open.load()
width, height = second_image_open.size
resolution = (width,height)

data = []

for y in range(height):
    for x in range(width):
        rgb_first = image_load[x, y]
        rgb_second = second_image_load[x,y]
        r_hide = int((rgb_first[0] + rgb_second[0])/2)
        g_hide = int((rgb_first[1] + rgb_second[1])/2)
        b_hide = int((rgb_first[2] + rgb_second[2])/2)
        data.append((r_hide,g_hide,b_hide))
print(data)
image_filter = Image.new("RGB", resolution)
image_filter.putdata(data)
image_filter.save(merged_path)
