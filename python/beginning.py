import random
str = "UPES"
arr = bytes(str, 'utf-8')
print(arr)

var = "Hey I am a string".encode('ASCII')
print(var)

x = 1
y = 7826817673267
z = -98732546

print(type(x))
print(type(y))
print(type(z))

print(random.randrange(1, 10))


#strings - sequence of characters

a = "hello world"
print(a[7])

#looping through a string

for a in "banana":
    print(a, end=" ")


b = "Hello world"
print(len(b))

txt = "The best things in life are free"
if "expensive" not in txt:
    print("Yes")


txt = "The best things in life are free"
print("expensive" not in txt)

p = "Hello World!"
print(p[2:11:2]) # prints index 1 to 6 

f = "   Hello world    "
print(f)
print(f.strip()) #strip removes blank spaces 
print(f.replace("He", "J"))

d = "Hello # World"
print(d.split("#"))

