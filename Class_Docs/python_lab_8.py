# 1. Add few names, one name in each row, in “name.txt file”.

# a.Count no of names
with open("name.txt", "r") as file:
    names = file.readlines()
    num_names = len(names)

# b. Count all names starting with vowel
vowel_start_count = sum(1 for name in names if name.strip()[0].lower() in 'aeiou')

# c. Find longest name
longest_name = max(names, key=lambda x: len(x.strip()))

print("Task 1:")
print("a. Number of names:", num_names)
print("b. Number of names starting with a vowel:", vowel_start_count)
print("c. Longest name:", longest_name.strip())

# 2. Store integers in a file.
with open("integers.txt", "r") as file:
    integers = [int(line.strip()) for line in file]

# a. Find the max number
max_number = max(integers)

# b. Find average of all numbers
average = sum(integers) / len(integers)

# c. Count number of numbers greater than 100
count_gt_100 = sum(1 for num in integers if num > 100)

print("\nTask 2:")
print("a. Max number:", max_number)
print("b. Average of all numbers:", average)
print("c. Count of numbers greater than 100:", count_gt_100)

'''    
3. Assume a file city.txt with details of 5 cities in given format (cityname population(in lakhs) area(in sq KM) ):
Example:
Dehradun 5.78 308.20
Delhi 190 1484
'''

# Open file city.txt and read to:
city_details = []
with open("city.txt", "r") as file:
    for line in file:
        city_details.append(line.strip().split())

# a. Display details of all cities
print("\nTask 3:")
print("a. Details of all cities:")
for city in city_details:
    print(city)

# b. Display city names with population more than 10Lakhs
print("\nb. City names with population more than 10 Lakhs:")
for city in city_details:
    if float(city[1]) > 10:
        print(city[0])

# c. Display sum of areas of all cities
total_area = sum(float(city[2]) for city in city_details)
print("\nc. Sum of areas of all cities:", total_area)

'''     
Input two values from user where the first line contains N, the number of test cases. The next N lines contain the space separated values of a and b. Perform integer division and print a/b. Handle exception in case of ZeroDivisionError or ValueError. 
Sample input
1 0
2 $
3 1 
Sample Output :
Error Code: integer division or modulo by zero 
Error Code: invalid literal for int() with base 10: '$' 3'''
def perform_integer_division(a, b):
    try:
        result = a // b
        print(result)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError:
        print("Error Code: invalid literal for int() with base 10:", b)

print("\nTask 4:")
# Sample Input
test_cases = [
    (1, 0),
    (2, "$"),
    (3, 1)
]

for test_case in test_cases:
    perform_integer_division(*test_case)

# 5. Create multiple suitable exceptions for a file handling program. 
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied to access the file!")
except IOError:
    print("An IO error occurred while handling the file!")
