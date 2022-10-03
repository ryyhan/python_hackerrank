import sys
import csv
from os.path import splitext
from PIL import Image, ImageOps


def main():
    validity()
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit(1)

    shirtfile = Image.open("shirt.png")

    size = shirtfile.size

    cs50 = ImageOps.fit(imagefile, size)

    Image.open("shirt.png")
    cs50.paste(shirtfile, shirtfile)

    cs50.save(sys.argv[2])


def validity():

    if len(sys.argv) < 3:
        sys.exit(1)
    if len(sys.argv) > 3:
        sys.exit(1)

    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])

    if check(file1[1]) == False:
        sys.exit(1)
    if check(file2[1]) == False:
        sys.exit(1)

    if file1[1].lower() != file2[1].lower():
        sys.exit(1)



def check(file):
    if file in [".png",".jpg", ".jepg"]:
        return True
    return False



if __name__ == "__main__":
    main()


"""
import sys
from PIL import Image,ImageOps

file_name=""
new_file_name=""

def validity():
    if(len(sys.argv) <2 ):
        sys.exit("Too few command-line arguments")

    elif(len(sys.argv) >3 ):
        sys.exit("Too many command-line arguments")

    elif((len(sys.argv) == 3) and (sys.argv[1][int(sys.argv[1].index(".")):] != sys.argv[2][int(sys.argv[2].index(".")):] )):
        sys.exit("Input and output have different extensions")

    else:
        file_name=sys.argv[1]
        new_file_name=sys.argv[2]
        overlay(file_name)


def overlay(file_name):
    image=Image.open(file_name)
    cImage=ImageOps.fit(image, size=image.size, bleed=0.0, centering=(0.5, 0.5))
    pImage=cImage.paste(cImage,box=None, mask=None)
    Image.save(pImage.new_file_name)

validity()

"""
