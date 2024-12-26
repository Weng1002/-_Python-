"""
File: CollectNewspaperKarel.py
Name: 
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    move_to_newspaper()
    bring_newspaper_home()

def move_to_newspaper():
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()

def bring_newspaper_home():
    pick_beeper()
    turn_around()
    move()
    move()
    move()
    turn_right()
    move()
    put_beeper()
    turn_right()

#  讓 Karel 轉向右方
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#  讓 Karel 轉身 (180 度)
def turn_around():
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
