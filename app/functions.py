import random
import string
 
# def generate_activation_code(len=8, n=2):
#     '' 'Genera n códigos de secuencia aleatoria de longitud len' ''
#     random.seed()
#     chars = '!@#$%&*()' + string.ascii_letters + string.digits
#     return [''.join([random.choice(chars) for _ in range(len)]) for _ in range(n)]
 
 
# if __name__ == '__main__':
#     for index, code in enumerate(generate_activation_code(), 1):
#         print(index, code)
 

def pass_gen():
    chars = '!@#$%&*()' + string.ascii_letters + string.digits
    password = []

    for i in range(16):
        chars_random = random.choice(chars)
        password.append(chars_random)

    password = ''.join(password)
    return password
