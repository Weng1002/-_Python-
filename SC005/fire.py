"""
File: fire.py
Name:
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage

HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    偵測並標記圖片中的火災像素。
    當偵測到火災像素時，將該像素設為紅色；非火災像素則轉為灰階。
    """
    image = SimpleImage(filename)
    for pixel in image:
        avg = (pixel.red + pixel.green + pixel.blue) / 3
        # 若紅色值大於 RGB 平均值乘上 HURDLE_FACTOR，則視為火災像素
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            # 非火災像素轉為灰階
            gray_value = int(avg)
            pixel.red = gray_value
            pixel.green = gray_value
            pixel.blue = gray_value
    return image

def main():
    filepath = 'images/greenland-fire.png'
    img = SimpleImage(filepath)
    img.show()  # 顯示原始圖片

    # 標記後的圖片
    highlighted_fire = highlight_fires(filepath)
    highlighted_fire.show()  # 顯示標記後的圖片

if __name__ == '__main__':
    main()
