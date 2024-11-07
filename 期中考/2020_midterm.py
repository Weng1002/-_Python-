# Problem 2: Python Expression and Functions 
# A.
# A: str(1010*2) + "37*3" + str(2) = 202037*32
# B: 7 // (-2) != -3 and int( 5 – 1.7 ) == 3.0 = True
# C: (17 % 7 + 5 / 1) // 2 = 4.0

# B.
# Answer1: 2.0
# Answer2: 80.0
# Answer3: 4
# Answer4: 0

# Problem 3: String and Nested For Loop
def name_diamond(name):
    for i in range(1, len(name) + 1):
        print(name[:i])
    for i in range(1, len(name)):
        print(" " * (i) + str(name[i:]))

# Problem 4: Python Random Generator
import random
def main( ): 
    print('Welcome to stanCode shi-ba-la!') 
    user_num = int(input('Number of players: '))
    random_dice(user_num)
    print('Thanks for playing!')


def random_dice(user_num):
    for i in range(user_num):
        while True:
            dice = []
            for j in range(4):
                dice.append(random.randrange(1, 7))
            if check_no_shi_ba_la(dice):
                print(f'Player {i+1}:', dice)
                break


def check_no_shi_ba_la(dice):
    unique_count = 0
    for i in range(len(dice)):
        count = 0
        for j in range(len(dice)):
            if dice[i] == dice[j]:
                count += 1
        if count == 1:
            unique_count += 1
    if unique_count == 4:  
        return False  

    for i in range(len(dice)):
        count = 0
        for j in range(len(dice)):
            if dice[i] == dice[j]:
                count += 1
        if count == 3:  
            return False 

    return True


if __name__ == "__main__":
    main()
