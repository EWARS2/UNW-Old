#this program accomplishes convolution!
from PIL import Image
#this performs the multiplication on patches
def convolve (list1,list2):
    answer = 0
    for x in range(3):
        for y in range(3):
            answer = answer + int(list1[x][y]*list2[x][y])
    if answer > 255:
        answer = 255
    if answer <0:
        answer = 0
    return answer
#mainline
# define convolution
conv = [[0.2, -1.6, 0.4], [0.3, 0.7, 0.2], [-1, 0.8, 0.9]]

# user pick channels
print('Channel Options are: R, G, B, RG, GB, RB, RGB')
channels = input('Enter the channel(s)')
c_test = [False,False,False]
c_test[0] = (channels == 'R') or (channels == 'RG') or (channels == 'RB') or (channels == 'RGB')
c_test[1] = (channels == 'G') or (channels == 'RG') or (channels == 'GB') or (channels == 'RGB')
c_test[2] = (channels == 'B') or (channels == 'RB') or (channels == 'GB') or (channels == 'RGB')

# read in image
path = "example.tiff"  # location of image
file = Image.open(path)  # file to be opened
width, height = file.size
m = file.load()  # file loaded into memory
data = []  # data structure to store image information
for y in range(height):
    for x in range(width):
        pixel = m[x, y]
        data.append((pixel[0], pixel[1], pixel[2]))
print("Testing Original Image Data...")
print(data[0:20])

# perform convolution
new_data = []
for y in range(height):
    for x in range(width):
        border_test = (x == 0) or (y == 0) or (y == height - 1) or (x == width - 1)
        pixel = m[x, y]
        r_intensity = 0
        g_intensity = 0
        b_intensity = 0
        # convolve the r channel
        if border_test==False:
            pixela = m[x-1,y-1]
            pixelb = m[x,y-1]
            pixelc = m[x+1,y-1]
            pixeld = m[x-1,y]
            pixele = m[x,y]
            pixelf = m[x+1,y]
            pixelg = m[x-1,y+1]
            pixelh = m[x,y+1]
            pixeli = m[x+1,y+1]
        for q in range(3):
            if (border_test == False) and c_test[q]:
                a = pixela[q]
                b = pixelb[q]
                c = pixelc[q]
                d = pixeld[q]
                e = pixele[q]
                f = pixelf[q]
                g = pixelg[q]
                h = pixelh[q]
                i = pixelh[q]
                patch = [[a,b,c], [d, e, f], [g, h, i]]
                if q == 0:
                    r_intensity = convolve(conv,patch)
                if q == 1:
                    g_intensity = convolve(conv,patch)
                if q == 2:
                    b_intensity = convolve(conv,patch)
        new_data.append((r_intensity, g_intensity, b_intensity))
# display new image
print("Testing New Image Data")
print(new_data[0:20])
resolution = (width,height)
image_filter = Image.new("RGB", resolution)
image_filter.putdata(new_data)
#image_filter.show()
image_filter.save("edited.tiff")
