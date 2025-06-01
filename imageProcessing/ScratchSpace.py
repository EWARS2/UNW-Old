float("Bob")

def crop(image):
    pass


def transpose(image):
    pass


def resize(image):
    pass


def rotate(image):
    pass


def black_white(image):
    pass


def color(image):
    pass


def contrast(image):
    pass


def sharpness(image):
    pass


def brightness(image):
    pass


def transform(image):
    pass


def channel_splitting(image):
    pass

def exit_program(Junk):
    print("Exiting")
    exit()

def main():

    options = {1: crop,
               2: transpose,
               3: resize,
               4: rotate,
               5: black_white,
               6: color,
               7: contrast,
               8: sharpness,
               9: brightness,
               10: transform,
               11: channel_splitting
               }

    options2 = [exit_program,
                crop,
                transpose,
                resize,
                rotate,
                black_white,
                color,
                contrast,
                sharpness,
                brightness,
                transform,
                channel_splitting
                ]



    for i in range(len(options2)):
        print(f"{i: >2}. " + options2[i].__name__)


    choice = int(input("Choice:"))
    options2[choice]("This is spam")

    print("Do stuff unless exiting")

main()