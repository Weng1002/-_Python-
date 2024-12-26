def encipher():
    secret_num = int(input("Enter the secret number: "))
    secret_message = input("What's the ciphered string? ").upper()
    deciphered_message = ""

    for i in secret_message:
        if i.isalpha():  
            # chr() converts ASCII to character
            # ord() converts character to ASCII

            # 65 is the ASCII value for 'A', so we want to subtract 65 to get the index of the letter in the alphabet from 0-25,
            # then add the secret number, then mod 26 to wrap around the alphabet, then add 65 to get the ASCII value of the new letter.
            deciphered_message += chr((ord(i) - 65 + secret_num) % 26 + 65)
        else:
            deciphered_message += i
    return deciphered_message

def encipher_re():
    secret_num = int(input("Enter the secret number: "))
    secret_message = input("What's the ciphered string? ").upper()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    deciphered_message = ""

    for i in secret_message:
        if i.isalpha():
            old_index = alphabet.index(i)
            new_index = (old_index + secret_num) % 26
            deciphered_message += alphabet[new_index]
        else:
            deciphered_message += i
    return deciphered_message


def main():
    print(encipher_re())

if __name__ == "__main__":
    main()