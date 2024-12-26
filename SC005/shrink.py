"""
File: shrink.py
Name:
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    original = SimpleImage(filename)
    width = original.width
    height = original.height
    new_img = SimpleImage.blank(width // 2, height // 2)

    for y in range(height // 2):
        for x in range(width // 2):
            # 取原圖中對應的像素 (2*x, 2*y)
            pixel = original.get_pixel(2 * x, 2 * y)
            
            # 將原圖像素值設置到新影像中
            new_pixel = new_img.get_pixel(x, y)
            new_pixel.red = pixel.red
            new_pixel.green = pixel.green
            new_pixel.blue = pixel.blue

    return new_img

def main():
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


#  DO NOT EDIT THE CODE BELOW THIS LINE  #
if __name__ == '__main__':
    main()
