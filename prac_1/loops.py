# Odd numbers between 1 and 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a. count in 10s from 0 to 100
for j in range(0, 110, 10):
    print(j, end=' ')
print()

# b. count down from 20 to 1
for k in range(20, 0, -1):
    print(k, end=' ')
print()

# c. print n stars based on user input
user_number = int(input("Enter Number: "))
for n in range(user_number):
    print('*', end=' ')
print()

# d. print n lines of increasing stars
for x in range(1, user_number + 1):
    print('*' * x)
print()
