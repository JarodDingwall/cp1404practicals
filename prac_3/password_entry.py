"""Ah Jarod Dingwall"""

MINIMUM_PASSWORD_LENGTH = 5


def main():
    password = input("Enter a password of at least {} characters: ".format(MINIMUM_PASSWORD_LENGTH))

    while len(password) < MINIMUM_PASSWORD_LENGTH:
        password = input("Enter a password of at least {} characters: ".format(MINIMUM_PASSWORD_LENGTH))

    print("*" * len(password))


main()
