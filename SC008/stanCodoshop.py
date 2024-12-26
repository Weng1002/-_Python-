"""
File: stanCodoshop.py
Name:
----------------------------------------------
Assignment7 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    c_d = ((pixel.red - red) ** 2 + (pixel.green - green) ** 2 + (pixel.blue - blue) ** 2) ** 0.5
    return c_d


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    sigma_red = 0
    sigma_blue = 0
    sigma_green = 0
    for i in range(len(pixels)):
        pixel = pixels[i]
        sigma_red += pixel.red
        sigma_green += pixel.green
        sigma_blue += pixel.blue
    rgb = [int(sigma_red/(len(pixels))), int(sigma_green/len(pixels)), int(sigma_blue/(len(pixels)))]
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the
     average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    """
    best_pixel = None
    avg = get_average(pixels)
    h = []
    for i in range(len(pixels)-1):
        pixel1 = pixels[i]
        distance = get_pixel_dist(pixel1, avg[0], avg[1], avg[2])
        h.append(distance)
    for pixel in pixels:
        if get_pixel_dist(pixel, avg[0], avg[1], avg[2]) == min(h):
            best_pixel = pixel
    return best_pixel
    """


    best_pixel = None
    min_dist = float('inf')  # 設定為無限大，方便找到最小值
    avg = get_average(pixels)
    avg_red, avg_green, avg_blue = avg[0], avg[1], avg[2]
    
    for pixel in pixels:
        distance = get_pixel_dist(pixel, avg_red, avg_green, avg_blue)
        if distance < min_dist:  # 更新最小距離和最佳像素
            min_dist = distance
            best_pixel = pixel

    return best_pixel



def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    # ----- YOUR CODE STARTS HERE ----- #
    
    for x in range(width):
        for y in range(height):
            pixels = []
            for image in images:
                pixel = image.get_pixel(x, y)
                pixels.append(pixel)

            # now s is a list consist pf the rgb values of a point(x,y) of the pics
            best_pixel = get_best_pixel(pixels)
            
            result_pixel  = result.get_pixel(x, y)
            result_pixel.red = best_pixel.red
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue
    

    # Write code to populate image and create the 'ghost' effect
    """
    green_im = SimpleImage.blank(20, 20, 'green')
    green_pixel = green_im.get_pixel(0, 0)
    print(get_pixel_dist(green_pixel, 5, 255, 10))
    """

    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # best1 = get_best_pixel([green_pixel, green_pixel,green_pixel,blue_pixel])
    # print(best1.red, best1.green, best1.blue)

    """
    green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    print(get_average([green_pixel, green_pixel, green_pixel, blue_pixel]))
    """
    """
    1. py stanCodoshop.py clock-tower
    2. py stanCodoshop.py hoover
    3. py stanCodoshop.py math-corner
    4. py stanCodoshop.py monster
    """
    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()