# Problem 2: Python Expression and Functions
# A.
# A: ”4 - 3” + 111 = Error because TypeError
# B: -0.5 < int(-0.9) and 8 / 4 != 8 // 4 = False
# C: 2.0 * -1.4 // 4 + 2 * 2 % 4 = −1.0

# B.
# Answer3: 9.0
# Answer4: 1.0
# Answer2: False

# Problem 3: String Manipulation
def secret(s):
    num_str = ''
    total = 0

    for char in s:
        if char.isdigit():
            num_str += char
        else:
            if num_str:
                total += int(num_str)
                num_str = ''

    # 因為字串結尾的字符是數字，所以要再加一次
    if num_str:
        total += int(num_str)

    return total

# Problem 4: Python Random Generator
import random

NUM_ROLLS = 15 
def main():
    run = 0
    in_run = False
    a = random.randrange(1, 7)
    print("Rolls:", a)
    
    for i in range(NUM_ROLLS-1):
        b = random.randrange(1, 7)
        print("Rolls:", b)
        if a == b:
            if not in_run:
                run += 1
                in_run = True
        else:
            in_run = False
        a = b

    print("Number of runs:", run)
        

if __name__ == "__main__":
    main()

# Problem 5: Python File Reading
FILEPATH = "romeojuliet.txt"

def get_num_tokens():
    total_tokens = 0

    with open(FILEPATH, "r") as file:
        for line in file:
            in_token = False
            for char in line:
                if char != ' ' and char != '\n':
                    if not in_token:
                        total_tokens += 1
                        in_token = True
                else:
                    in_token = False
    
    return total_tokens