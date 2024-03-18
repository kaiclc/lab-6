def encode(num_string):
    encoded_string = ""
    for digit in num_string:
        new_digit = (int(digit)+3) % 10
        encoded_string += str(new_digit)
    return encoded_string


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
            print(f"The encoded password is {stored}")
        elif selection == "3":
            break

        print()


if __name__ == "__main__":
    main()
