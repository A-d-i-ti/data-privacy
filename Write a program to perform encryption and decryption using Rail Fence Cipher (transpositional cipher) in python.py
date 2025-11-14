'''row → tells which rail we are currently on. (Start at rail 0)
step → direction of movement
1 means go down
-1 means go up'''

def encrypt(text, key):
    rail = [''] * key
    row, step = 0, 1
    for ch in text:
        rail[row] += ch
        if row == 0: step = 1
        elif row == key - 1: step = -1
        row += step
    return ''.join(rail)


def decrypt(cipher, key):
    L = len(cipher)
    pattern = [['' for _ in range(L)] for _ in range(key)]
    
    # Mark zigzag pattern
    row, step = 0, 1
    for i in range(L):
        pattern[row][i] = '*'
        if row == 0: step = 1
        elif row == key - 1: step = -1
        row += step

    # Fill pattern
    idx = 0
    for r in range(key):
        for c in range(L):
            if pattern[r][c] == '*':
                pattern[r][c] = cipher[idx]
                idx += 1

    # Read plaintext
    result, row, step = '', 0, 1
    for i in range(L):
        result += pattern[row][i]
        if row == 0: step = 1
        elif row == key - 1: step = -1
        row += step

    return result


msg = input("Message: ")
key = int(input("Rails: "))

enc = encrypt(msg, key)
print("Encrypted:", enc)

dec = decrypt(enc, key)
print("Decrypted:", dec)
