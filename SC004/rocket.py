SIZE = 10

def head(size):
    for i in range(size):
        print(" " * (size - i ) + "/" * (i + 1) + "\\" * (i + 1))

def belt(size):
    print("+" + "=" * (size * 2) + "+")

def upper(size):
    for i in range(size):
        print("|" + "." * (size - i - 1) + "/" * (i + 1) + "\\" * (i + 1) + "." * (size - i - 1) + "|")

def lower(size):
    for i in range(size):
        print("|" + "." * i + "\\" * (size - i) + "/" * (size - i) + "." * i + "|")

def main():
    head(SIZE)
    belt(SIZE)
    upper(SIZE)
    lower(SIZE)
    belt(SIZE)
    head(SIZE)

if __name__ == "__main__":
    main()