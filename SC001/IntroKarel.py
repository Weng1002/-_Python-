#!/usr/bin/env python3

"""
This is a stanCode PyCharm intro project.
"""

from karel.stanfordkarel import *


def draw_side():
    # put_beeper()
    move()
    # put_beeper()
    # move()
    # put_beeper()
    # move()
    # turn_left()


def draw_square():
    draw_side()
    draw_side()
    draw_side()
    draw_side()


def main():
    draw_square()


if __name__ == "__main__":
    print("Hello, it's me, Karel! You're done with the PyCharm setup process! "
          "Now press the run button to see me draw a square. ")
    execute_karel_task(main)
