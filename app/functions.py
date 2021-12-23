import random
import string
 

def pass_gen():
    chars = str('!@#$%&*()') + string.ascii_letters + string.digits
    password = []

    for i in range(16):
        chars_random = random.choice(chars)
        password.append(chars_random)

    password = ''.join(password)
    return password
