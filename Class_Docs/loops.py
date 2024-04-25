# for loop

languages = ['Switf', 'Python', 'go']

for i in languages:
    print(i)
print()


language = 'Python'
for i in language:
    print(i)
print()


for i in range(4):
    print(i)
print()


#while loop
number = 1

while number <= 3:
    print(number)
    number = number + 1
print()

sum = 0
count = 0

while count < 5:
    value = (int(input("Enter a number: ")))
    sum += value
    count += 1
print(f'The sum is {sum}')
print()


current_lvl = 1
final_lvl = 4
game_completed = True

while current_lvl <= final_lvl:
    if game_completed:
        print(f'Welcome to level {current_lvl}')
        current_lvl += 1
print("Game Over!")
print()

for i in range(5):
    if i == 3:
        break
    print(i)
print()


for i in range(5):
    if i == 3:
        continue
    print(i)
print()


n = 10
if n > 10:
    pass
print("Hello")