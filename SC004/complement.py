def build_complement():
    Word = input("Please give me a DNA strand and I'll find the complement: ")
    Complement = ""
    for i in Word:
        if i == "A" or i == "a":
            Complement += "T"
        elif i == "T" or i == "t":
            Complement += "A"
        elif i == "C" or i == "c":
            Complement += "G"
        elif i == "G" or i == "g":
            Complement += "C"
        else:
            print(f"Invalid DNA strand: '{i}' is not a valid DNA nucleotide.")
            return
        
    print("The complement of", Word, "is", Complement)
    return Complement

def main():
    build_complement()

if __name__ == "__main__":
    main()