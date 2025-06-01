#this create AI generated art
from PIL import Image
import math

#mainline
width = 600
height = 400
resolution = (width,height)
data = []
for y in range(height):
    for x in range(width):
        #here we choose an algorithm for determining color
        r_intensity = int(math.sin(x/20)*120+120)
        g_intensity = int(math.sin(y/20)*120+120)
        b_intensity = int(math.sin((x+y)/20)*120+120)
        data.append((r_intensity,g_intensity,b_intensity))

#prepare new file to store filtered pixel list
filter_path = "./filter.tiff"
image_filter = Image.new("RGB", resolution)
image_filter.putdata(data)
image_filter.save(filter_path)
