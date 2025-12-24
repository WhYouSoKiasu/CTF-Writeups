# Fireworks

**Difficulty: very easy**  
**Points: 500 --> 300**  
**Solves: 21**  

---

## Hints
- The set seed ensure that you always get the same numbers from randint. just like setting a world seed in Minecraft.
- We need to undo what they have done to the flag
- One of the operations they did is reversible

---

## Challenge Description

Some hacker got into the fireworks system and made it need a password! Lucky for us, they left this here. Maybe this can help us get the password.

Flag is in all uppercase separated by underscores.

---

## Solve

The encryption looks random at first, but the code uses seed(914), which means the “random” numbers are actually predictable. If I use the same seed, Python will generate the exact same sequence of shifts.

Each character of the flag is encrypted by shifting it forward in a fixed character set (wheel) by a random amount. To reverse this, I reused the same seed and generated the same shifts, but subtracted the shift instead of adding it.

Since the encryption was:
![Encryption](screenshots/firework1.png)

I reversed the encryption using:
![Decryption](screenshots/firework2.png)


The decrypted flag output was: NYP{LET_THE_FIREWORKS_BEGIN}
