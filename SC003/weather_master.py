# Constants
Quit_value = -100

def main():
    print("stanCode \"Weather Master 4.0\"!")

    count = 0
    total = 0
    cold_days = 0
    highest = None
    lowest = None

    while True:
        temp = int(input(f"Next Temperature: (or {Quit_value} to quit)? "))
        if temp == Quit_value:
            break

        count += 1
        total += temp
        
        if highest is None or temp > highest:
            highest = temp
        if lowest is None or temp < lowest:
            lowest = temp       
        if temp < 16:
            cold_days += 1

    if count > 0:
        average = total / count
        print(f"Highest temperature = {highest}")
        print(f"Lowest temperature = {lowest}")
        print(f"Average = {average}")
        print(f"{cold_days} cold day(s)")
    else:
        print("No temperatures were entered.")

if __name__ == '__main__':
    main()
