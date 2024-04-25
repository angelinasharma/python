# | operator compares each bit and sets it to 1 if both are 1, otherwise it is set to 0
print(6 | 3)

# ^ operator compares each bit and sets it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0
print (2 ^ 6)

# << operator inserts the specified number of 0's from the right and let the same amount of leftmost bits fall off
print(2 << 7)

# >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0'
print(4 >> 9)

# & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0
print(2 & 3)

# ~ operator inverts all the bits
print(~8)



