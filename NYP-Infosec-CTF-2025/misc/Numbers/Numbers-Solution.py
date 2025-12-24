import tiktoken

enc = tiktoken.get_encoding("o200k_base")

tokens = [
    200264, 17360, 200266, 3575, 553, 261, 10297, 29186, 11, 484, 59641, 290,
    9641, 25, 15522, 47, 90, 40, 20555, 83558, 119232, 1228, 191039, 20468,
    85940, 6829, 1099, 16255, 1608, 553, 625, 316, 26477, 495, 9641, 306,
    1062, 9591, 503, 1625, 306, 3322, 290, 1825, 13782, 11, 3463, 56334,
    290, 9641, 306, 3611, 2220, 503, 26157, 41096, 11526, 13, 1843, 290,
    1825, 27747, 316, 26477, 11, 11915, 503, 38654, 1062, 7881, 328, 290,
    9641, 11, 503, 290, 6508, 9641, 8807, 11, 9570, 483, 25, 392, 33680,
    11, 357, 6284, 1652, 483, 484, 1, 200265, 200264, 1428, 200266, 200265,
    200264, 173781, 200266
]

decoded_message = []

for t in tokens:
    try:
        # decode_single_token_bytes returns the bytes for a specific token
        token_bytes = enc.decode_single_token_bytes(t)
        decoded_message.append(token_bytes.decode('utf-8', errors='replace'))
    except KeyError:
        # If it's a special token (like 200264), we skip it or mark it
        # This prevents the crash
        decoded_message.append(" [SPECIAL] ")

print("".join(decoded_message))