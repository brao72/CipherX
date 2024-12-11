import string

def vigenere_encrypt(plaintext, password):
    alphabets = string.ascii_lowercase
    ans = []
    p_len = len(password)
    for i, ch in enumerate(plaintext):
        if ch.lower() in alphabets:
            shift = alphabets.index(password[i % p_len].lower())
            # Encrypt
            new_idx = (alphabets.index(ch.lower()) + shift) % 26
            new_char = alphabets[new_idx]
            # Preserve case if needed, but here we assume lowercase
            ans.append(new_char)
        else:
            # Non-alphabetic characters are appended as is
            ans.append(ch)
    return "".join(ans)

def vigenere_decrypt(ciphertext, password):
    alphabets = string.ascii_lowercase
    ans = []
    p_len = len(password)
    for i, ch in enumerate(ciphertext):
        if ch.lower() in alphabets:
            shift = alphabets.index(password[i % p_len].lower())
            # Decrypt
            new_idx = (alphabets.index(ch.lower()) - shift) % 26
            new_char = alphabets[new_idx]
            ans.append(new_char)
        else:
            ans.append(ch)
    return "".join(ans)
