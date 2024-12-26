"""
File: MidpointKarel.py
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
    place_beepers_along_wall()
    find_wall()
    find_middle()

def place_beepers_along_wall():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()
    turn_around()

def find_wall():
    pick_beeper()
    while front_is_clear():
        move()
    turn_around()

def find_middle():
    pick_beeper()
    while True:
        if not is_beeper_ahead():
            pick_beeper()
            turn_around()
            break
        else:
            while front_is_clear():
                move()
                if not is_beeper_ahead():
                    pick_beeper()
                    turn_around()
                    move()
                    break


def is_beeper_ahead():
    move()
    if on_beeper():
        turn_around()
        move()
        turn_around()
        return True
    else:
        turn_around()
        move()
        turn_around()
        return False


def turn_around():
    turn_left()
    turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    execute_karel_task(main)
