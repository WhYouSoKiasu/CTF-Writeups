from random import seed, randint

seed(914)

wheel = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_{}'
EncryptedFlag = 'OELXFGQPYRI}C}DPKGOCASGPZVNJ'
DecryptedFlag = ''

for i in EncryptedFlag:
    DecryptedFlag += wheel[(wheel.find(i) - randint(0, len(wheel) - 1)) % len(wheel)]

print(DecryptedFlag)
