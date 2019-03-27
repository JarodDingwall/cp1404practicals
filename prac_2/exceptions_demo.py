"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? ValueError occurs when entering a non-integer value
2. When will a ZeroDivisionError occur? ZeroDivisionError occurs when denominator input is zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
if denominator == 0 print("Can't divide by zero!")
    denominator = int(input("Enter the denominator: "))
    else print(fraction)
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

