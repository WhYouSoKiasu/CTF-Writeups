from Crypto.Util.number import long_to_bytes

# The ciphertext from the challenge
ct = 0x756b45c7f89ef9544e4fa53bce87946c0b17df562cec738e89562e01a9bda7916785b16a3eee9d3b53c060bfa051851d6c4c9d85ee0a2be1e624d632569e7ec65fd48e632e25b71a44f08f8d9f7fa4e7f5833bec9f865

# Function to calculate integer cube root
def integer_cube_root(n):
    low = 0
    high = n
    while low < high:
        mid = (low + high) // 2
        if mid**3 < n:
            low = mid + 1
        else:
            high = mid
    return low


# 1. Calculate the cube root of the ciphertext to get the message integer (m)
m_int = integer_cube_root(ct)

# 2. Convert the integer back to bytes
flag = long_to_bytes(m_int)

print(flag.decode())