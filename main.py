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

    contrasena = []

    while (len(contrasena) < length):
        caracteres=random.choice(caracter)    
        contrasena.append(caracteres)

    contrasena = "".join(contrasena)
    return contrasena

def run():

    contrasena = generate_password()
    print('Tu nueva contraseña es: '+ contrasena)

if __name__ == "__main__":
    run()