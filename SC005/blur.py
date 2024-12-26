"""
File: blur.py
Name:
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    將給定的圖片進行模糊處理，返回模糊後的圖片。
    每個像素的顏色取自身與周圍像素的平均值。
    """
    width = img.width
    height = img.height
    new_img = SimpleImage.blank(width, height)

    for y in range(height):
        for x in range(width):
            red_sum = 0
            green_sum = 0
            blue_sum = 0
            count = 0

            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    new_x = x + dx
                    new_y = y + dy
                    # 檢查新位置是否在影像邊界內
                    if 0 <= new_x < width and 0 <= new_y < height:
                        pixel = img.get_pixel(new_x, new_y)
                        red_sum += pixel.red
                        green_sum += pixel.green
                        blue_sum += pixel.blue
                        count += 1
            
            new_pixel = new_img.get_pixel(x, y)
            new_pixel.red = red_sum // count
            new_pixel.green = green_sum // count
            new_pixel.blue = blue_sum // count

    return new_img

def main():
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(4):  
        blurred_img = blur(blurred_img)
    blurred_img.show()


#  DO NOT EDIT THE CODE BELOW THIS LINE  #
if __name__ == '__main__':
    main()
