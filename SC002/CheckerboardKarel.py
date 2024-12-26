"""
File: CheckerboardKarel.py
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
    put_beeper()
    while front_is_clear():
        fill_one_line()
        move_to_next_line()
    fill_one_line() # 當最後一行填完時，Karel 不需要再移動了

def fill_one_line():
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()  # 每兩格放置一個 beeper

def move_to_next_line():
    if facing_east():
        if on_beeper():  # 情況一：當最後一格放置了 beeper
            turn_left()
            if front_is_clear():
                move()  # 先移動一格
                turn_left()
                if front_is_clear():
                    move()
                    put_beeper()
        else:  # 情況二：當最後一格沒有放置 beeper
            turn_left()
            if front_is_clear():
                move()
                put_beeper()  # 在進入新行後立刻放置 beeper
                turn_left()
    else:
        if on_beeper():  # 情況三：當最後一格放置了 beeper
            turn_right()
            if front_is_clear():
                move()
                turn_right()
                if front_is_clear():
                    move()
                    put_beeper()
        else:  # 情況四：當最後一格沒有放置 beeper
            turn_right()
            if front_is_clear():
                move()
                put_beeper()
                turn_right()


def turn_right():
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    execute_karel_task(main)
