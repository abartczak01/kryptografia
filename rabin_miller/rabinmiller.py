import random
from math import gcd
import sys

# Agata Bartczak 285755

def fermat(n):
    with open("wyjscie.txt", "w+") as f:
        for _ in range(40):
            a = random.randint(2, n - 1)
            # sprawdzam czy a ma wspólny dzielnik z n
            gcd_val = gcd(a, n)
            if gcd_val == 1:
            # jeśli a nie ma wspólnego dzielnika z n, sprawdzam czy a jest świadkiem pierwszości, czyli a^(n-1) = 1 (mod n)
                if not pow(a, n-1, n) == 1:
                    print(f"znaleziono liczbę a, która nie jest świadkiem pierwszości")
                    print("liczba jest na pewno złożona")
                    f.write("na pewno złożona")
                    return False

        f.write("prawdopodobnie pierwsza")
        return True


def rabin_miller(n, r=None):
    with open("wyjscie.txt", "w+") as f:
        for _ in range(40):
            k = 0
            b_before = 0
            first = True
            a = random.randint(2, n - 1)
            if gcd(a, n) != 1:
                ret = gcd(a, n)
                f.write(str(ret))
                exit()

            m = r if r else n - 1

            while m % 2 != 1:
                k += 1
                m //= 2
            bj = pow(a, m, n)

            if bj == 1 or bj == n - 1:
                continue

            for _ in range(k):
                bj_before = bj
                bj = pow(bj, 2, n)
                if bj == 1 and first:
                    b_before = bj_before
                    first = False
                    break
            ret = gcd(b_before - 1, n)
            if ret != 1:
                f.write(str(ret))
                exit()
        print("liczba jest pierwsza lub podano niewłaściwy wykładnik uniwersalny")
        f.write("prawdopodobnie pierwsza")


def main():
    with open("wejscie.txt", "r") as input_file:
        number1_line = input_file.readline().strip()
        number2_line = input_file.readline().strip()
        number3_line = input_file.readline().strip()

        number1 = int(number1_line) if number1_line else None
        number2 = int(number2_line) if number2_line else None
        number3 = int(number3_line) if number3_line else None

        if len(sys.argv) > 1:
            if sys.argv[1] == "-f":
                if number1:
                    fermat(number1)
                else:
                    print("brak liczby w pierwszej linii pliku")
            else:
                print("zły parametr")
        else:
            r = None
            if number3:
                r = number2 * number3 - 1
            elif number2:
                r = number2
            rabin_miller(number1, r)


main()