# Scan n values in the range 0-3 and print the number of times each value has occurred:

counts = [0] * 4
n = int(input("Enter the number of values: "))
for _ in range(n):
    value = int(input("Enter a value between 0 and 3: "))
    if 0 <= value <= 3:
        counts[value] += 1
for i in range(4):
    print("Value", i, "occurred", counts[i], "times")

#Create a tuple to store n numeric values and find the average of all values:

n = int(input("Enter the number of values: "))
values = tuple(float(input("Enter a numeric value: ")) for _ in range(n))
average = sum(values) / n
print("Average of the values:", average)

# Write a program to input a list of scores for N students in a list data type. Find the score of the runner-up and print the output:

N = int(input("Enter the number of students: "))
scores = list(map(int, input("Enter the scores of the students separated by space: ").split()))
unique_scores = sorted(set(scores), reverse=True)
print("Runner-up score:", unique_scores[1])

'''    
Create a dictionary of n persons where the key is the name and the value is the city.
    a) Display all names
    b) Display all city names
    c) Display student name and city of all students.
    d) Count the number of students in each city.
'''

n = int(input("Enter the number of persons: "))
person_dict = {}
for i in range(n):
    name = input("Enter name of person {}: ".format(i+1))
    city = input("Enter city of person {}: ".format(i+1))
    person_dict[name] = city

# a) Display all names
print("Names of all persons:", ', '.join(person_dict.keys()))

# b) Display all city names
print("City names:", ', '.join(set(person_dict.values())))

# c) Display student name and city of all students.
print("Details of all persons:")
for name, city in person_dict.items():
    print("Name:", name, "| City:", city)

# d) Count the number of students in each city.
city_counts = {}
for city in person_dict.values():
    city_counts[city] = city_counts.get(city, 0) + 1
print("Number of students in each city:")
for city, count in city_counts.items():
    print(city, "-", count)

'''
Store details of n movies in a dictionary by taking input from the user. Each movie must store details like name, year, director name, production cost, collection made (earning) & perform the following:
    a) Print all movie details
    b) Display names of movies released before 2015
    c) Print movies that made a profit.
    d) Print movies directed by a particular director.
'''

n = int(input("Enter the number of movies: "))
movies = []
for i in range(n):
    name = input("Enter name of movie {}: ".format(i+1))
    year = int(input("Enter year of release for {}: ".format(name)))
    director = input("Enter director name for {}: ".format(name))
    production_cost = float(input("Enter production cost for {}: ".format(name)))
    collection = float(input("Enter collection made for {}: ".format(name)))
    movies.append({"name": name, "year": year, "director": director, "production_cost": production_cost, "collection": collection})

# a) Print all movie details
print("Details of all movies:")
for movie in movies:
    print("Name:", movie["name"], "| Year:", movie["year"], "| Director:", movie["director"], "| Production Cost:", movie["production_cost"], "| Collection:", movie["collection"])

# b) Display names of movies released before 2015
print("Movies released before 2015:")
for movie in movies:
    if movie["year"] < 2015:
        print(movie["name"])

# c) Print movies that made a profit.
print("Movies that made a profit:")
for movie in movies:
    if movie["collection"] > movie["production_cost"]:
        print(movie["name"])

# d) Print movies directed by a particular director.
director_name = input("Enter the name of the director to search for: ")
print("Movies directed by {}:".format(director_name))
for movie in movies:
    if movie["director"] == director_name:
        print(movie["name"])