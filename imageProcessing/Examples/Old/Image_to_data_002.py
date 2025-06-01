from PIL import Image
#this program converts a .tiff file to rgb data
#mainline
path = "../example.tiff"  #location of image
file = Image.open(path)      #file to be opened

width, height = file.size
memory = file.load()         #file loaded into memory
data = []                    #data structure to store image information
for y in range(height):
    for x in range(width):
        pixel = memory[x,y]
        data.append((pixel[0],pixel[1],pixel[2]))
print(data[0:20])
