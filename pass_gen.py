import random
import string
import pyperclip

def generate_password(length, type_passowrd):
    if type_passowrd == "n":
        characters = string.ascii_letters + string.digits 
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(int(length)))


def input_arguments():
    length_of_password = input('Length of Password[12]: ')
    if len(length_of_password) == 0 :
        length_of_password = 16
    symbols_of_password = input('Type of Password, with special symbol[n]: ')
    if len(symbols_of_password) == 0:
        symbols_of_password = "n"
#     print(f"Generated Password: {generate_password(length_of_password, symbols_of_password)}")
    Password = generate_password(length_of_password, symbols_of_password)
    print (f"Generated Password: {Password}")
    pyperclip.copy(Password)


if __name__ == "__main__":
    input_arguments()
    

