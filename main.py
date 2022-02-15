# MIT License @ Ali Vorobiev (https://github.com/avcomps).

#!/usr/bin/env python3

from typing import Any
from PIL import Image

def main() :
    img_pixels = Any; img_size = ()
    colors_repeated = []

    with Image.open("example_1.jpg") as img: img_pixels = img.load(); img_size = img.size
    
    print(img_size)
    print(img_pixels[4, 4])


if __name__ == "__main__":
    try :
        main()
    except(KeyboardInterrupt) :
        print("\nERROR: KeyboardInterrupt")