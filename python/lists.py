#lists are heterogenous in nature

list = ["apple", "banana", "cherry"]
print(list)
print(len(list))

list1 = ["abc", 34, True, 4.0, "male"]
print(list1)

print(list[0]) # prints the 0th index
print(list[-1]) # prints the 1st index from backward

list2 = [1, 3, 5, 7, 9]
list3 = [True, False, False]

print(list2)
print(list3)

print(type(list))
print(type(list2))
print(type(list3))

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
'''
print(thislist[2:5])
print(thislist[2:])
print(thislist[-4:-1])

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

thislist[1] = "blackcurrant" # add blackcurrant to the 1st index
print(thislist) 

thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist[1:3] = ["watermelon"]

thislist.insert(2, "guava")
print(thislist)

thislist.append("strawberry")
print(thislist)

tropical = ["pineapple, papaya"]
thislist.extend(tropical)
print(thislist)

thistuple = ("blackberry", "idk")
thislist.extend(thistuple)
print(thislist)

thislist.remove("apple")
print(thislist)
'''
thislist.pop(1)
print(thislist)

# del thislist removes this list from existance

thislist.clear()
print(thislist)



