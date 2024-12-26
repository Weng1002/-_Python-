import math

print("stanCode Quadratic Solver:")
num_a = int(input("Enter a:"))  
while num_a <= 0:
    print("錯誤，a不能等於或小於0，請重新輸入。")
    num_a = int(input("Enter a:")) 
num_b = int(input("Enter b:"))
num_c = int(input("Enter c:"))

discriminant = (num_b**2) - (4*num_a*num_c)

if discriminant > 0:
    root_1 = ((-num_b) + math.sqrt(discriminant)) / (2 * num_a)
    root_2 = ((-num_b) - math.sqrt(discriminant)) / (2 * num_a)
    print("Two roots:", root_1, ",", root_2)
elif discriminant == 0:  
    root = (-num_b) / (2 * num_a)
    print("One root:", root)
else:
    print("No real roots")
