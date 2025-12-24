# Cracking

**Difficulty: easy**  
**Points: 500 --> 416**  
**Solves: 14**  

---

## Hints
- This is a type of homophonic encryption. If the encrypted word is 2 letters long, the decrypted word is also 2 letters long.
- The flag always starts with 'NYP{' and ends with '}'. You can probably use that to figure out some letters

---

## Challenge Description

I found this while spring cleaning and remembered that it had some kind of secret on it. Unfortunately, I haven't been able to crack it. Another piece of paper that came with it says that only a letter to number substitution was used, and the same number always corresponds to the same letter. Perhaps you can crack it? The flag is all in lower case, with no spaces

---

## Solve

In the famous song and lyrics, the previous challenge at Note to self has a rick roll, so I guessed the song is Never Gonna Give You Up as it is also a famous internet song, which fits the numbers. By doing substitution cipher, the text can be decrypted.

- Line 1: 8 22 7 7 15_ E L L O --> HELLO (So 8 = H)
- Line 2: 10 8 22 24 22 .T H E R E . --> THERE.
- Line 3-4: 16 17 / 6 15 20I _ / Y O U --> IF YOU (So 17 = F)
- Line 5-6: 12 24 22 / 24 22 12 13 16 25 18A R E / R E A D I N G --> ARE READING
- Line 7: 10 8 16 11 ,T H I _ , --> THIS, (So 11 = S)
- Line 8-9: 6 15 20 / 26 16 18 8 10Y O U / _ I G H T --> YOU MIGHT (So 26 = M)
- Line 10-11: 8 12 9 22 / 17 16 18 20 24 22 13H A V E / F I G U R E D --> HAVE FIGURED
- Line 12-14: 15 20 10 / 10 8 22 / 19 15 13 22 .O U T / T H E / _ O D E . --> OUT THE CODE. (So 19 = C)
- Line 15-16: 1 22 7 7 / 13 15 25 22 ,W E L L / D O N E , --> WELL DONE,
- Line 17-21: 16 / 19 22 24 10 12 16 25 7 6 / 8 15 4 22 / 6 15 20 / 22 25 14 15 6 22 13I / C E R T A I N L Y / H O P E / Y O U / E N _ O Y E D --> I CERTAINLY HOPE YOU ENJOYED (So 14 = J)
- Line 22-23: 10 8 16 11 / 4 20 21 21 7 22 .T H I S / P U _ _ L E . --> THIS PUZZLE. (So 21 = Z)
- Line 24-25: 12 25 6 1 12 6 11 , / 10 8 22A N Y W A Y S , / T H E --> ANYWAYS, THE
- Line 26-27: 17 7 12 18 / 16 11F L A G / I S --> FLAG IS
- Line 28 (The Flag):25 6 4 { 19 24 12 19 2 22 24 11 _ 17 15 24 _ 6 15 20 }.N Y P { C R A C _ E R S _ F O R _ Y O U }Context tells us the missing letter _ (2) is K.

Flag: NYP{CRACKERS_FOR_YOU}