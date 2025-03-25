# 2025.03.22
# Mavzu: Checking the number if it is prime or not
# Muallif: Muhammadsodiq

import math

def check_number(a):
    if a % 2 == 0:
        print(f"Your {a} is an even number")
    else:
        print(f"Your {a} number is an odd number")

number = int(input('Enter a number >>> '))
print(check_number(number))