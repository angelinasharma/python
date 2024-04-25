num = 5

if num > 0:
    print("The number is positive")

#if-else

num2 = -5

if num2 > 0:
    print("The number is positive")
else:
    print("The number is negative")

#elif condition

num3 = 0

if num3 > 0:
    print("The number is positive")
elif num3 == 0:
    print("The number is zero")
else:
    print("The number is negative")


num4 = 5

if num4 > 0:
    print("The number is positive")
elif num4 == 0:
    print("The number is zero")
else:
    print("The number is negative")


#nested if-else

num5 = 5

if num5 >= 0:
    if num5 == 0:
        print("The number is zero")
    else:
        print("The number is positive")
else:
    print("The number is negative")


num6 = 0

if num6 >= 0:
    if num6 == 0:
        print("The number is zero")
    else:
        print("The number is positive")
else:
    print("The number is negative")

num7 = -4

if num7 >= 0:
    if num7 == 0:
        print("The number is zero")
    else:
        print("The number is positive")
else:
    print("The number is negative")

num8 = 4

if num8 % 2 == 0:
    print("The input is even")
else:
    print("The input is odd")


score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 50:
    grade = "E"
else:
    grade = "F"

print(f'The grade is {grade}')


score2 = 63

if score2 >= 90:
    grade = "A"
elif score2 >= 80:
    grade = "B"
elif score2 >= 70:
    grade = "C"
elif score2 >= 60:
    grade = "D"
elif score2 >= 50:
    grade = "E"
else:
    grade = "F"

print(f'The grade is {grade}')



year = 2000

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} is a leap year')
        else:
            print(f'{year} is not a leap year')
    else:
        print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')


year2 = 2065

if year2 % 4 == 0:
    if year2 % 100 == 0:
        if year2 % 400 == 0:
            print(f'{year2} is a leap year')
        else:
            print(f'{year2} is not a leap year')
    else:
        print(f'{year2} is a leap year')
else:
    print(f'{year2} is not a leap year')


year3 = 2084

if year3 % 4 == 0:
    if year3 % 100 == 0:
        if year3 % 400 == 0:
            print(f'{year3} is a leap year')
        else:
            print(f'{year3} is not a leap year')
    else:
        print(f'{year3} is a leap year')
else:
    print(f'{year3} is not a leap year')


year4 = -2000

if year4 % 4 == 0:
    if year4 % 100 == 0:
        if year4 % 400 == 0:
            print(f'{year4} is a leap year')
        else:
            print(f'{year4} is not a leap year')
    else:
        print(f'{year4} is a leap year')
else:
    print(f'{year4} is not a leap year')


year5 = 2024

if year5 % 4 == 0:
    if year5 % 100 == 0:
        if year5 % 400 == 0:
            print(f'{year5} is a leap year')
        else:
            print(f'{year5} is not a leap year')
    else:
        print(f'{year5} is a leap year')
else:
    print(f'{year5} is not a leap year')

year6 = 2024

if year6 % 4 == 0:
    if year6 % 100 == 0:
        print(f'{year} is a leap year')
    else:
        print(f'{year6} is not a leap year')
else:
    print(f'{year6} is not a leap year')

'''
if a is divisible by 4 it is a leap year 
if a is not divisible by 400 but is divisible by 100 it is not a leap year
if the year is not divisible by 100 but divisible by 4 it is a leap year
if the year is not divisible by 4 it is not a leap year
'''

string = "hello, world"
char = "w"

if char in string:
    print(f'The string contains the character {char}')
else:
    print(f'The string does not contain the character {char}')

char2 = "c"

if char2 in string:
    print(f'The string contains the character {char2}')
else:
    print(f'The string does not contain the character {char2}')

