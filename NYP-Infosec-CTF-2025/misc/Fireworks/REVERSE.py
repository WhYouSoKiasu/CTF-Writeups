from random import seed, randint

# 1. Set the exact same seed to reproduce the "random" sequence
seed(914)

wheel = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_{}'
# The encrypted text found in the comments
encrypted_string = 'OELXFGQPYRI}C}DPKGOCASGPZVNJ'

decrypted_flag = ''

for char in encrypted_string:
    # 2. Generate the SAME random shift used during encryption
    shift = randint(0, len(wheel) - 1)

    # 3. Find the current position of the encrypted character
    current_index = wheel.find(char)

    # 4. Reverse the math
    # Encryption was: (original + shift) % length
    # Decryption is:  (current - shift) % length
    original_index = (current_index - shift) % len(wheel)

    decrypted_flag += wheel[original_index]

print("The Flag is:", decrypted_flag)