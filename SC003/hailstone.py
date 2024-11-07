print("This program computes Hailstone sequences.\n")

steps = 0
num = int(input("Enter a number:"))
if num == 1:
    print("it took 0 steos to reach 1.")
else:
    while num != 1:
        if num % 2 != 0: #odd
            re_num = int(num * 3 + 1)
            print(f"{num} is odd, so I make 3n+1:{re_num}")
            num = re_num
            steps += 1
        elif num % 2 == 0: #even
            re_num = int(num / 2)
            print(f"{num} is even, so I take half:{re_num}")
            num = re_num
            steps += 1
    print(f"It took {steps} steps to reach 1.")