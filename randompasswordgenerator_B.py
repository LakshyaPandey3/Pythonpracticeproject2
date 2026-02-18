import random
import math
import string

alpha = string.ascii_letters
num = string.digits
special = string.punctuation

while True:

    more = input("\n Do you want to generate more passwords (y/n) ?  : ").lower()

    if more == 'y':

        pass_len = int(input("Enter the length of the password: "))

        alpha_len = pass_len // 2
        num_len = math.ceil(pass_len * 0.3)
        special_len = pass_len - (alpha_len + num_len)

        password = []

        for _ in range(alpha_len):
            char = random.choice(alpha)
            if random.choice([True, False]):
                char = char.upper()
            password.append(char)

        for _ in range(num_len):
            password.append(random.choice(num))

        for _ in range(special_len):
            password.append(random.choice(special))

        generated_pwd = ''.join(password)

        print(generated_pwd)

    elif more == 'n':

        print("Exiting the program.....")
        break

    else:
        print("Invalid choice try again.....")