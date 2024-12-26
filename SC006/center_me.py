"""
File: center_me.py
Name: Jerry Liao
--------------------------------
This program shows how to center a GRect
on windows where the width and the height are
randomly chosen
"""

from campy.graphics.gobjects import GRect
from campy.graphics.gwindow import GWindow

# It controls the width and height of the rect
SIZE = 100
# Control the dimension of our windows!
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 300


def main():
    """
    Center a magenta rect on the canvas
    where the width and height are SIZE
    """
    rect = GRect(SIZE, SIZE)
    rect.filled = True
    rect.color = 'magenta'
    rect.fill_color = 'magenta'
    window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    rect_x = (window.width-rect.width)/2
    rect_y = (window.height-rect.height)/2
    window.add(rect, x=rect_x, y=rect_y)


if __name__ == '__main__':
    main()
