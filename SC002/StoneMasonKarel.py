"""
File: StoneMasonKarel.py
Name: 
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    # 跑迴圈，確認非最後一根柱子的beepers
    while front_is_clear():
        fill_column()  # 填滿當前的柱子
        move_to_next_column()  # 移動到下一根柱子

    # 填滿最後一根柱子
    fill_column()

def no_beepers_present():
    return not on_beeper()

def fill_column():
    turn_left()
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        move()
    # 檢查最上面
    if no_beepers_present():
        put_beeper()

    turn_around()
    while front_is_clear():
        move()
    turn_left()

def move_to_next_column():
    for _ in range(4):  # 每次跨四步到下一根柱子
        move()


# 讓 Karel 向右轉
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# 讓 Karel 轉身（180度）
def turn_around():
    turn_left()
    turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
