import random
import string

# function that returns a password
def generate_password(length = 8, upper = True, low = True, num = True, special_char = True):
    caracter = ""

    if upper:
        caracter += string.ascii_uppercase
    if low:
        caracter += string.ascii_lowercase
    if num:
        caracter += string.digits
    if special_char:
        caracter += string.punctuation

    password = []

    while (len(password) < length):
        caracteres=random.choice(caracter)    
        password.append(caracteres)

    password = "".join(password)
    return password

def run():
    try:
        pass_length = int(input("Password length: "))
        pass_upper = bool(input("Uppercase? (default false): "))
        pass_low = bool(input("Lowercase? (default false): "))
        pass_num = bool(input("Numbers? (default false): "))
        pass_special = bool(input("Special Character? (default false): "))
        password = generate_password(pass_length, pass_upper, pass_low, pass_num, pass_special)
        print('Your new password is: '+ password)
    except ValueError as er:
        print("Wrong data type: " + str(er))
    except IndexError as er:
        print("At least choose one option: " + str(er))

if __name__ == "__main__":
    run()