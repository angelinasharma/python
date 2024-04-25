# Write a Python function to find the maximum and minimum numbers from a sequence of numbers:

def find_max_min(numbers):
    if not numbers:
        return None, None
    max_num = min_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
    return max_num, min_num

# Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number:

def sum_of_cubes(n):
    if n <= 0:
        return 0
    return sum([i**3 for i in range(1, n)])

#Write a Python function to print 1 to n using recursion:

def print_numbers(n):
    if n <= 0:
        return
    print_numbers(n - 1)
    print(n)

#Write a recursive function to print Fibonacci series up to n terms:

def fibonacci(n, a=0, b=1):
    if n <= 0:
        return
    print(a, end=" ")
    fibonacci(n-1, b, a+b)

# Write a lambda function to find the volume of a cone:

volume_of_cone = lambda radius, height: (1/3) * 3.14159 * (radius**2) * height

# Write a lambda function which gives a tuple of max and min from a list:

max_min_tuple = lambda lst: (max(lst), min(lst))


# Write functions to explain mentioned concepts:

#a. Keyword argument:

def greet(name, message="Hello"):
    print(message, name)

# Usage:
greet(name="John")  
greet(message="Hi", name="Alice")  

# b. Default argument:

def greet(name, message="Hello"):
    print(message, name)

# Usage:
greet("John")  
greet("Alice", "Hi") 

#c. Variable length argument:

def sum_values(*args):
    total = 0
    for num in args:
        total += num
    return total

# Usage:
print(sum_values(1, 2, 3)) 
print(sum_values(1, 2, 3, 4, 5))  
