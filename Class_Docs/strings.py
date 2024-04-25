# 1. capitalize() function (Makes the first letter in the sentence uppercase)
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(x)

# 2. casefold() function (Makes the whole string lowercase)
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

# 3. center() function (aligns the string)
txt = "banana"
x = txt.center(20)
print(x)

# 4. count() function (returns the number of times a value appears in the string)
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apples")
print(x)

# 5. encode() function (encodes the string using specified encoding. Default is UTF-8)
txt = "My name is Stale"
x = txt.encode()
print(x)

# 6. endswith() function (returns true if the string ends with the specified value)
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

# 7. expandtabs() function (sets the tab size to the given number of whitespaces)
txt = "H\te\tl\tl\to"
x = txt.expandtabs(2)
print(x)

# 8. find() function (finds the first occurence of the given value)
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

# 9. format() function (formats the given value and inserts them inside the placeholder)
txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))

# 10. index() function (finds the first occurence of the specified value)
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

# 11. ljust() function (aligns the string to the left using a specified character as the fill character. Default is space)
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

# 12. maketrans() function (returns a mapping table that can be used with the translate() to replace specified characters)
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))

# 13. partition() (searches for a specified string and splits the string into a tuple containing three elements - part before, after the string and containing the string)
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

# 14. splitlines() function (splits the string into a list)
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)
