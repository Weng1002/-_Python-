"""
File: green_screen.py
Name:
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    將綠幕圖像中的人物合成到背景圖像中，去除綠幕部分。
    :param background_img: 背景圖像
    :param figure_img: 含綠幕的圖像
    :return: 合成後的新圖像
    """

    width = background_img.width
    height = background_img.height

    for y in range(height):
        for x in range(width):
            figure_pixel = figure_img.get_pixel(x, y)
            background_pixel = background_img.get_pixel(x, y)

            # 判斷是否為綠幕像素
            bigger = max(figure_pixel.red, figure_pixel.blue)
            if figure_pixel.green > 2 * bigger:
                # 綠幕像素，使用背景圖像的像素
                figure_pixel.red = background_pixel.red
                figure_pixel.green = background_pixel.green
                figure_pixel.blue = background_pixel.blue

    return figure_img


def main():
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


#  DO NOT EDIT THE CODE BELOW THIS LINE  #
if __name__ == '__main__':
    main()
