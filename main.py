# MIT License @ Ali Vorobiev (https://github.com/avcomps).

#!/usr/bin/env python3

from PIL import Image, ImageColor

def main() :
    img_size = (); img_pixels = None
    list_colors = []

    with Image.open("example_1.jpg") as img: img_pixels = img.load(); img_size = img.size
    
    max_size_x = img_size[0] - 1
    max_size_y = img_size[1] - 1

    for x in range(max_size_x) :
        for y in range(max_size_y) :
            if(img_pixels[x, y]) not in list_colors :
                # list_colors.append(ImageColor.getcolor(img_pixels[x, y], 'RGB'))
                pass
    
    print(list_colors)

if __name__ == "__main__":
    try :
        main()
    except(KeyboardInterrupt) :
        print("\nERROR: KeyboardInterrupt")