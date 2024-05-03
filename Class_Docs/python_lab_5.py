# 1. Write a program to count and display the number of capital letters in a given string.

string = input("Enter a string: ")
count = 0
for char in string:
    if char.isupper():
        count += 1
print("Number of capital letters:", count)

# 2. Count total number of vowels in a given string

string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print("Number of vowels:", count)


#3. Program to input a sentence and print words in separate lines

sentence = input("Enter a sentence: ")
words = sentence.split()
for word in words:
    print(word)


''' 4. WAP to enter a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
Sample Input
ABCDCDC
CDC
Sample Output
2 
'''

string = input("Enter a string: ")
substring = input("Enter a substring: ")
count = string.count(substring)
print("Number of times the substring occurs:", count)


''' 
5. Given a string containing both upper and lower case alphabets. Write a Python program to count the number of occurrences of each alphabet (case insensitive) and display the same.
Sample Input
ABaBCbGc
Sample Output
2A
3B
2C
1G
'''

string = input("Enter a string: ")
count_dict = {}
for char in string:
    if char.isalpha():
        char = char.upper()
        count_dict[char] = count_dict.get(char, 0) + 1

for char, count in count_dict.items():
    print(f"{count}{char}")


# 6. Program to count number of unique words in a given sentence using sets.

sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = set()
for word in words:
    unique_words.add(word)
print("Number of unique words:", len(unique_words))


''' 
7. Program to create 2 sets s1 and s2 of n fruits each by taking input from the user and find:
    a) Fruits which are in both sets s1 and s2
    b) Fruits only in s1 but not in s2
    c) Count of all fruits from s1 and s2:
'''


n = int(input("Enter the number of fruits: "))
s1 = set()
s2 = set()

print("Enter fruits for set s1:")
for _ in range(n):
    fruit = input()
    s1.add(fruit)

print("Enter fruits for set s2:")
for _ in range(n):
    fruit = input()
    s2.add(fruit)

print("Fruits in both sets:", s1.intersection(s2))
print("Fruits only in s1 but not in s2:", s1.difference(s2))
print("Count of all fruits from s1 and s2:", len(s1.union(s2)))

# 8. Program to apply various set operations on two sets


S1 = {"Red", "yellow", "orange", "blue"}
S2 = {"violet", "blue", "purple"}

print("Union of S1 and S2:", S1 | S2)
print("Intersection of S1 and S2:", S1 & S2)
print("Difference of S1 and S2:", S1 - S2)
print("Symmetric difference of S1 and S2:", S1 ^ S2)
