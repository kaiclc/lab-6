# Marvin Gao
# UF ID: 97640683

def encode(num_string):
    encoded_string = ""
    for digit in num_string:
        new_digit = (int(digit)+3) % 10
        encoded_string += str(new_digit)
    return encoded_string

# Jonathan Groberg
# Decodes the encoded string
def decode(encoded_string):
    decoded_string = ""
    for digit in encoded_string:
        new_digit = int(digit)-3

        # if the number goes below 0, add 10 (-3+10 = 7) this is inverse of 7+3 =10 (mod 10 is 0)
        new_digit = 10+new_digit if new_digit < 0 else new_digit
        decoded_string += str(new_digit)
    return decoded_string


def main():
    stored = ""
    while True:

        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        selection = input("Please enter an option: ")
        if selection == "1":
            original_password = input("Please enter your password to encode: ")
            stored = encode(original_password)
            print("Your password has been encoded and stored!")
        elif selection == "2":
            # work in progress!
            print(
                f"The encoded password is {stored}, and the original password is {decode(stored)}'")
        elif selection == "3":
            break

        print()


if __name__ == "__main__":
    main()
