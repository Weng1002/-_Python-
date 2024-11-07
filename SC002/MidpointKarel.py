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


# from karel.stanfordkarel import *
#
# def main():
#     place_beepers_along_wall()
#     find_middle()
#
# def place_beepers_along_wall():
#     put_beeper()
#     while front_is_clear():
#         move()
#         put_beeper()
#     turn_around()
#
# def find_middle():
#     while True:
#         move_to_last_beeper()
#         pick_beeper()
#         turn_around()
#         if front_is_clear():
#             move_to_last_beeper()
#             if on_beeper():
#                 pick_beeper()
#             turn_around()
#         else:
#             break  # 當前方不再有beeper時，表示已經到達中點
#
# def move_to_last_beeper():
#     while front_is_clear():
#         move()
#     # 當前方沒有牆並且腳下有beeper時，這就是此行的最後一個beeper
#     while not on_beeper() and front_is_clear():
#         move()
#
# def turn_around():
#     turn_left()
#     turn_left()
#
# # DO NOT EDIT CODE BELOW THIS LINE #
# if __name__ == '__main__':
#     execute_karel_task(main)

