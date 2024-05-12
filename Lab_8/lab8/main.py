import random
import hashlib

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise Exception('Модульне обернене число не існує')
    else:
        return x % m

def is_prime(num, k=5):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        d = num - 1
        r = 0
        while d % 2 == 0:
            d //= 2
            r += 1
        for _ in range(k):
            a = random.randint(2, num - 2)
            x = pow(a, d, num)
            if x == 1 or x == num - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, num)
                if x == num - 1:
                    break
            else:
                return False
        return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Обидва числа повинні бути простими.')
    elif p == q:
        raise ValueError('p і q не можуть бути рівними.')

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    key, n = public_key
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    key, n = private_key
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

def sign(private_key, message):
    key, n = private_key
    hashed_message = int.from_bytes(hashlib.sha256(message.encode()).digest(), byteorder='big')
    signature = pow(hashed_message, key, n)
    return signature

def verify(public_key, message, signature):
    key, n = public_key
    hashed_message = int.from_bytes(hashlib.sha256(message.encode()).digest(), byteorder='big')
    decrypted_signature = pow(signature, key, n)
    return decrypted_signature == hashed_message

if __name__ == "__main__":
    p = 1451
    q = 2027
    public, private = generate_keypair(p, q)

    with open("original_message.txt", "r") as f:
        message = f.read().strip()

    encrypted_msg = encrypt(public, message)
    decrypted_msg = decrypt(private, encrypted_msg)

    signature = sign(private, message)
    verification = verify(public, message, signature)

    with open("encrypted_message.txt", "w") as f:
        f.write(' '.join(map(str, encrypted_msg)))

    with open("decrypted_message.txt", "w") as f:
        f.write(decrypted_msg)

    print("Підпис перевірено:", verification)
