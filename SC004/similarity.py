def find_sequence():
    long_sequence = input("Please give me a DNA sequence to search : ").upper()
    short_sequence = input("What DNA sequence would you like to match? ").upper()

    if len(short_sequence) > len(long_sequence):
        print("Error: The short sequence is longer than the long sequence.")
        return

    best_match = ""
    best_similarity = 0

    for i in range(len(long_sequence) - len(short_sequence) + 1):
        sub_sequence = ""
        for j in range(len(short_sequence)):
            sub_sequence += long_sequence[i + j]

        similarity = 0
        for j in range(len(short_sequence)):
            if sub_sequence[j] == short_sequence[j]:
                similarity += 1

        if similarity > best_similarity:
            best_similarity = similarity
            best_match = sub_sequence
            
    print("The best match is ",best_match)

def main():
    find_sequence()

if __name__ == "__main__":
    main()
