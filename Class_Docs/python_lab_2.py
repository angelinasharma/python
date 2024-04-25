import math

'''
Declare these variables (x, y and z) as integers. Assign a value of 9 to x, Assign a
value of 7 to y, perform addition, multiplication, division and subtraction on these
two variables and Print out the result.
'''

x = 9
y = 7
print("x =",x)
print("y =",y)
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)

'''
Write a Program where the radius is taken as input to compute the area of a circle.
'''

radius = int(input("Enter the radius of the circle"))
area = (3.14 * radius**2)
print(f'The area of the circle is',area)

'''
Write a Python program to solve (x+y)*(x+y)
'''

a = int(input("Enter the first value"))
b = int(input("Enter the second value"))
value = ((a+b)*(a+b))
print("The value is",value)

'''
Write a program to compute the length of the hypotenuse (c) of a right triangle
using Pythagoras theorem
'''

p = int(input("Enter the value of the perpendicular"))
b = int(input("Enter the value of the base"))

c = math.sqrt((p**2)+(b**2))
print(c)

'''
Write a program to find simple interest.
'''

principal = float(input("Enter the principal: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time period in years: "))

interest = (principal * rate * time) / 100
print("Simple interest:", interest)

'''
Program to find area of a triangle when length of sides are given
'''

a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))

s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("Area of the triangle:", area)

'''
Program to swap two numbers without taking additional variable
'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a + b
b = a - b
a = a - b

print("After swapping:")
print("First number:", a)
print("Second number:", b)

'''
Program to find sum of first n natural numbers
'''

n = int(input("Enter the value of n: "))
sum_natural_numbers = (n * (n + 1)) // 2
print("Sum of first", n, "natural numbers:", sum_natural_numbers)

'''
Program to print truth table for bitwise operators (&, |, and ^ operators)
'''

print("Truth table for AND operator:")
print("0 & 0 =", 0 & 0)
print("0 & 1 =", 0 & 1)
print("1 & 0 =", 1 & 0)
print("1 & 1 =", 1 & 1)

print("\nTruth table for OR operator:")
print("0 | 0 =", 0 | 0)
print("0 | 1 =", 0 | 1)
print("1 | 0 =", 1 | 0)
print("1 | 1 =", 1 | 1)

print("\nTruth table for XOR operator:")
print("0 ^ 0 =", 0 ^ 0)
print("0 ^ 1 =", 0 ^ 1)
print("1 ^ 0 =", 1 ^ 0)
print("1 ^ 1 =", 1 ^ 1)

''' 
Program to find left shift and right shift values of a given number
'''

num = int(input("Enter a number: "))
shift = int(input("Enter number of bits to shift: "))

left_shifted = num << shift
right_shifted = num >> shift

print("Left shifted value:", left_shifted)
print("Right shifted value:", right_shifted)

''' 
Using membership operator find whether a given number is in sequence (10,20,56,78,89)
'''

sequence = [10, 20, 56, 78, 89]
number = int(input("Enter a number to check: "))

if number in sequence:
    print(number, "is in the sequence.")
else:
    print(number, "is not in the sequence.")

'''
Using membership operator find whether a given character is in a string
'''
string = input("Enter a string: ")
character = input("Enter a character to check: ")

if character in string:
    print(character, "is present in the string.")
else:
    print(character, "is not present in the string.")
