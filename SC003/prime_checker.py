constant = -100

def main():
    print("Welcome to the prime checker!")
    num_n = int(input("n:"))
    while num_n != constant:
        if is_prime(num_n):
            print(f"{num_n} is a prime number.")
            num_n = int(input("n:"))
        else:
            print(f"{num_n} is not a prime number.")
            num_n = int(input("n:"))
    print("Have a good one!")

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    main()