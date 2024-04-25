## How to print
- Basic syntax
    print("whatever you want to print", var)

```run-python
print("Hello world")
```
```run-python
x = 7
print("the value of x is", x)
```
## Variables
- Basic syntax
    var_name = value
- Variable types
    - string
    - integer
    - float
    - tuple
    - dict
- To print the type of the variable
    - print(type(var_name)) - type(var_name) stores the type of variable
```run-python
string = "Whatever"
integer = 2409
float = 24.09
tuple = (2, 6, "angel")
dict = {"uhm": "like this", "i think": "maybe"}

print(type(string))
print(type(integer))
print(type(float))
print(type(tuple))
print(type(dict))
```

## How to take inputs and use them
- Basic syntax 
     var_name = input("Prompt for the input")
```run-python
name = input("Enter your name: ")
print("Hello", name)
```

## F-strings
- F-strings are just another way of printing strings 
- Basic syntax
    - print(f"whatever you want to print {var}")
```run-python
name = input("Enter your name: ")
print(f"Nice to meet you {name}")
```
## How to create functions and call them 
- To define functions - 
    - def func_name(parameters):
         whatever you want the function to do
- To call functions -
    - func_name(arguements)
```run-python
A = int(input("Enter first number: "))
B = int(input("Enter second number: "))

def sum(a,b):
    print(a+b)
    
sum(A,B)
```
