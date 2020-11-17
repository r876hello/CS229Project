import os
from PIL import Image
import os, sys

path = "./test/t2/"
dirs = os.listdir(path)

def resize():
    counter = 0
    for item in dirs:
        print(counter)
        
        if (os.path.isfile(path+item)):
            counter += 1
            im=Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((240, 240), Image.ANTIALIAS)
            imResize.save(f + e, "PNG", quality = 90)

resize()


