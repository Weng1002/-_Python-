"""
File: mirror_lake.py
Name: 
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    根據原圖生成一個上下鏡像排列的影像
    上半部是原圖，下半部是原圖的上下翻轉
    """
    original = SimpleImage(filename)
    width = original.width
    height = original.height

    # 建立與原圖同寬、兩倍高的新影像
    reflected_image = SimpleImage.blank(width, height * 2)

    # 將原圖的像素複製到新影像的上半部
    for y in range(height):
        for x in range(width):
            pixel = original.get_pixel(x, y)
            reflected_image.set_rgb(x, y, pixel.red, pixel.green, pixel.blue)

    # 將原圖的像素鏡像複製到新影像的下半部
    for y in range(height):  # y = 0 到 y = height - 1
        for x in range(width): # x = 0 到 x = width - 1
            # 從原圖的最底部（height - 1 - y）開始，複製到新影像的下半部（height + y）
            pixel = original.get_pixel(x, height - 1 - y)
            # 當 y = 0 時，height - 1 - y = height - 1，即原圖的最底部像素。
            # 當 y = 1 時，height - 1 - y = height - 2，即原圖倒數第二行。
            reflected_image.set_rgb(x, height + y, pixel.red, pixel.green, pixel.blue)
            # 當 y = 0 時，height + y = height，即新影像的下半部分第一行。
            # 當 y = 1 時，height + y = height + 1，即新影像的下半部分第二行。

    return reflected_image

def main():
   # 生成鏡像圖片並顯示
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


#  DO NOT EDIT THE CODE BELOW THIS LINE  #
if __name__ == '__main__':
    main()
