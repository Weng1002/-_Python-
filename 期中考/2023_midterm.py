# Problem 2: Python Expression and methods
# A.
# A: 15.0/4+(8+3.0) = 14.75
# B: 6<12 and (10 >15) or 10>5 = True
# C: int(’10.8’)+1 = Error because ValueError

# B.
# Answer3: 4.0
# Answer5: 5.0
# Answer2: 3.0
# Answer4: 1.0

# Problem 3-1: String Manipulation  
def to_decimal(bits) : 
    decimal_value = 0
    for bit in bits : 
        decimal_value = decimal_value * 2 + int(bit)

    if bits[0] == '1':
        decimal_value -= 2 ** len(bits)

    return decimal_value

#Problem 3-2: String Manipulation
def twos_complement(bits):
    bits = list(bits)
    found_one = False
    result = ""

    for i in range(len(bits) - 1, -1, -1):
        if bits[i] == '1' :
            found_one = True
            result = "1" + result
        elif found_one :
            if bits[i] == '0':
                result = "1" + result
            else:
                result = "0" + result
        else:
            result = bits[i] + result
    return result

# Problem 3-3: File Reading
def main(): 
    decmal_num = 0
    legnth = 0

    with open("data.txt", "r") as file:
        for line in file:
            print("Original: ", line.strip())

            is_valid = True
            for bit in line:
                if bit not in "01":
                    is_valid = False
                    break

            if not is_valid:
                print("2's complement: illegal format")
                continue

            print("2's complement:",twos_complement(line.strip()))
            decmal_num = decmal_num + to_decimal(line.strip())
            legnth = legnth + 1

            print("Decimal:", decmal_num)
            print()
    
    print("the average is: ", decmal_num/legnth)
    file.close()

# Problem 4: Math Operations
def reverse(x): 
    INT_MAX = 2**31 - 1  
    INT_MIN = -2**31

    negative = False
    if x < 0:
        negative = True

    reversed_x = 0
    while x > 0:
        # 取 x 的最後一位數字
        digit = x % 10
        reversed_x = reversed_x * 10 + digit
        # 移除最後一位數字
        x //= 10

    if negative:
        reversed_x = -reversed_x

    if reversed_x < INT_MIN or reversed_x > INT_MAX:
        return 0

    return reversed_x

