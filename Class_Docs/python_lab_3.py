import math

'''
Check whether given number is divisible by 3 and 5 both
'''

num1 = int(input("Enter a number: "))

if num1 % 3 == 0 and num1 % 5 == 0:
    print(number, "is divisible by both 3 and 5.")
else:
    print(num1, "is not divisible by both 3 and 5.")

''' 
Check whether a given number is a multiple of five or not
'''

num2 = int(input("Enter a number: "))

if num2 % 5 == 0:
    print(num2, "is a multiple of 5.")
else:
    print(num2, "is not a multiple of 5.")

'''
Find the greatest among two numbers. If numbers are equal than print “numbers are equal"
'''

num3 = float(input("Enter first number: "))
num4 = float(input("Enter second number: "))

if num3 > num4:
    print(num1, "is the greatest.")
elif num4 > num3:
    print(num4, "is the greatest.")
else:
    print("Numbers are equal.")

''' 
Find the greatest among three numbers assuming no two values are the same
'''

num5 = float(input("Enter first number: "))
num6 = float(input("Enter second number: "))
num7 = float(input("Enter third number: "))

if num5 > num6 and num5 > num7:
    print(num5, "is the greatest.")
elif num6 > num5 and num6 > num7:
    print(num6, "is the greatest.")
elif num7 > num5 and num7 > num6:
    print(num7, "is the greatest.")
else:
    print("Numbers are equal.")

''' 
Check whether the quadratic equation has real roots or imaginary roots. Display the roots
'''

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

d = (b ** 2) - (4 * a * c)

if d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Real roots:", root1, "and", root2)
elif d == 0:
    root = -b / (2 * a)
    print("Real and equal roots:", root)
else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(abs(d)) / (2 * a)
    print("Complex roots:", real_part, "+", imaginary_part,"i and", real_part, "-", imaginary_part,"i")

''' 
Find whether a given year is a leap year or not
'''

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

''' 
Write a program which takes any date as input and display the next date of the calendar
'''
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))


if day < 30:
    day += 1
elif month < 12:
    day = 1
    month += 1
else:
    day = 1
    month = 1
    year += 1

print("Next date:", "day =", day, "month =", month, "year =", year)

''' 
Print the grade sheet of a student for the given range of cgpa. Scan marks of five subjects and calculate the percentage.
'''

marks_PDS = int(input("Enter marks obtained in PDS: "))
marks_Python = int(input("Enter marks obtained in Python: "))
marks_Chemistry = int(input("Enter marks obtained in Chemistry: "))
marks_English = int(input("Enter marks obtained in English: "))
marks_Physics = int(input("Enter marks obtained in Physics: "))

total_marks = marks_PDS + marks_Python + marks_Chemistry + marks_English + marks_Physics
percentage = (total_marks / 500) * 100

cgpa = percentage / 10

if cgpa >= 0 and cgpa <= 3.4:
    grade = "F"
elif cgpa <= 5.0:
    grade = "C+"
elif cgpa <= 6.0:
    grade = "B"
elif cgpa <= 7.0:
    grade = "B+"
elif cgpa <= 8.0:
    grade = "A"
elif cgpa <= 9.0:
    grade = "A+"
else:
    grade = "O"

print("Sample Gradesheet")
print("Name: Rohit Sharma")
print("Roll Number: R17234512")
print("Sem: 1")
print("SAPID: 50005673")
print("Course: B.Tech. CSE AI&ML")
print("Subject name: Marks")
print("PDS:", marks_PDS)
print("Python:", marks_Python)
print("Chemistry:", marks_Chemistry)
print("English:", marks_English)
print("Physics:", marks_Physics)
print("Percentage:", percentage, "%")
print("CGPA:", cgpa)
print("Grade:", grade)
