# Find a factorial of a given number

num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("The factorial of", num, "is", factorial)
print()


# Check whether the given number is an Armstrong number:

num = int(input("Enter a number: "))
sum = 0
temp = num
order = len(str(num))
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
print()

# Print Fibonacci series up to a given term

nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1, end=', ')
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
print()

# Check if the given number is a prime number or not:

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
print()


# Check whether the given number is a palindrome or not

num = int(input("Enter a number: "))
temp = num
reverse_num = 0
while temp != 0:
    reverse_num = reverse_num * 10 + temp % 10
    temp //= 10
if num == reverse_num:
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")
print()


# Write a program to print the sum of digits

num = int(input("Enter a number: "))
sum = 0
while num > 0:
    sum += num % 10
    num //= 10
print("The sum of digits is:", sum)
print()


# Count and print all numbers divisible by 5 or 7 between 1 to 100:

print("Numbers divisible by 5 or 7 between 1 to 100:")
for i in range(1, 101):
    if i % 5 == 0 or i % 7 == 0:
        print(i, end=" ")
print()

# Convert all lower cases to upper case in a string:

string = input("Enter a string: ")
upper_string = ""
for char in string:
    if char.islower():
        upper_string += char.upper()
    else:
        upper_string += char
print("String in upper case:", upper_string)
print()

# Print all prime numbers between 1 and 100

print("Prime numbers between 1 and 100:")
for num in range(1, 101):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, end=" ")
print()

# Print the table for a given number:

num = int(input("Enter a number: "))
print("Multiplication Table for", num)
for i in range(1, 11):
    print(num, "*", i, "=", num * i)
print()