import string
import random


def generator(size: int, digits=True, lower=True, upper=True, punctuation=False, user=""):
    """size (integer): length of password
    digits (bool): include digits
    lower (bool): inclide lowercase letters
    upper (bool): include uppercase letters
    punctuation (bool): include punctuation
    user (string): include symbols, selected by user"""
    symbols = string.digits * digits + string.ascii_lowercase * lower + string.ascii_uppercase * upper + string.punctuation * punctuation + user
    password = ""
    for i in range(size):
        password += random.choice(symbols)
    print(password)
    return password


generator(4, True, False, False)  # 4 digit pin
generator(10)  # 10 symbol digits and letters
generator(16, punctuation=True)  # 16 symbols and punctuation
generator(40, punctuation=True)  # ridiculously long password
generator(10, True, False, False, user="ABCDEF")
