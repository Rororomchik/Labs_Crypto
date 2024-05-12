def main():
    print("Оберіть функцію для виклику:")
    print("1. Розширений алгоритм Евкліда")
    print("2. Бінарне піднесення до степеня")
    print("3. Функція Ейлера")
    choice = int(input("Введіть свій вибір (1/2/3): "))

    if choice == 1:
        call_euclid_function()
    elif choice == 2:
        call_binary_exponentiation()
    elif choice == 3:
        call_euler_totient()
    else:
        print("Невірний вибір. Будь ласка, оберіть дійсну опцію.")


def call_euclid_function():
    a = int(input("Введіть значення a: "))
    b = int(input("Введіть значення b: "))

    gcd, x, y = extended_euclid(a, b)
    print(f"НСД({a}, {b}) = {gcd}")
    print(f"Константи: x = {x}, y = {y}")


def call_binary_exponentiation():
    base_number = int(input("Введіть базове число: "))
    exponent = int(input("Введіть степінь: "))
    result = binary_exponentiation(base_number, exponent)
    print(f"{base_number}^{exponent} = {result}")


def call_euler_totient():
    n = int(input("Введіть значення n: "))
    print(f"Функція Ейлера для {n} = {euler_totient(n)}")


def binary_exponentiation(base_number, exponent):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base_number
        base_number *= base_number
        exponent //= 2
    return result


def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_euclid(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y


def euler_totient(n):
    if n == 1:
        return 1

    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1

    if n > 1:
        result -= result // n

    return result


if __name__ == "__main__":
    main()
