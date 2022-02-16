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
                list_colors.append(img_pixels[x, y])
                pass
    
    # print(list_colors)

    img_res_size_x, img_res_size_y = 800, 800
    img_res = Image.new("RGB", (img_res_size_x, img_res_size_y))
    i = 0; j = 0
    for color in list_colors :
        for x in range(15) :
            if i == img_res_size_x :
                j += 1; i = 0
            else :
                img_res.putpixel((i, j), color)
                print(i, j)
            i += 1
    
    img_res.save("./output_image.jpg", "JPEG")

if __name__ == "__main__":
    try :
        main()
    except(KeyboardInterrupt) :
        print("\nERROR: KeyboardInterrupt")