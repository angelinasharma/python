import module1 as m1

# modules are considered the same as a library

# a file containing a set of functions you want to include in the code 

m1.greeting("Angelina")

a = m1.person1["age"]
print(a)

'''

modules can be given aliases using:
    import *module_name* as *alias*

it will be used as 
    a = *alias*.function_name(arguement)

'''