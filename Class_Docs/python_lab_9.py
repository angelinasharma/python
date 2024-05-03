# 1.Create a class of student (name, sap id, marks[phy,chem,maths] ). Create 3 objects by               
# taking inputs from the user and display details of all students.

class Student:
    def __init__(self, name, sap_id, phy_marks, chem_marks, maths_marks):
        self.name = name
        self.sap_id = sap_id
        self.phy_marks = phy_marks
        self.chem_marks = chem_marks
        self.maths_marks = maths_marks

    def display_details(self):
        print("Name:", self.name)
        print("SAP ID:", self.sap_id)
        print("Physics Marks:", self.phy_marks)
        print("Chemistry Marks:", self.chem_marks)
        print("Maths Marks:", self.maths_marks)

# Creating 3 objects by taking inputs from the user
print("Enter details for 3 students:")
students = []
for i in range(3):
    name = input("Enter name: ")
    sap_id = input("Enter SAP ID: ")
    phy_marks = float(input("Enter Physics marks: "))
    chem_marks = float(input("Enter Chemistry marks: "))
    maths_marks = float(input("Enter Maths marks: "))
    students.append(Student(name, sap_id, phy_marks, chem_marks, maths_marks))

# Display details of all students
print("\nStudent Details:")
for student in students:
    student.display_details()


# 2. Add constructor in the above class to initialize student details of n students 
#    and implement following methods:
#   a) Display() student details
#   b) Find Marks_percentage() of each student
#   c)  Display result() [Note: if marks in each subject >40% than Pass else Fail]

class Student:
    def __init__(self, name, sap_id, phy_marks, chem_marks, maths_marks):
        self.name = name
        self.sap_id = sap_id
        self.phy_marks = phy_marks
        self.chem_marks = chem_marks
        self.maths_marks = maths_marks

    def display(self):
        print("Name:", self.name)
        print("SAP ID:", self.sap_id)
        print("Physics Marks:", self.phy_marks)
        print("Chemistry Marks:", self.chem_marks)
        print("Maths Marks:", self.maths_marks)

    def marks_percentage(self):
        return ((self.phy_marks + self.chem_marks + self.maths_marks) / 300) * 100

    def result(self):
        if self.marks_percentage() >= 40:
            return "Pass"
        else:
            return "Fail"

    def class_average(students):
        total_percentage = sum(student.marks_percentage() for student in students)
        return total_percentage / len(students)

# 3. Create programs to implement different types of inheritances.

# Single Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()  
dog.bark()   

# Multilevel Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Labrador(Dog):
    def color(self):
        print("Labrador is brown")

labrador = Labrador()
labrador.speak() 
labrador.bark()  
labrador.color() 

# Hierarchical Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

dog = Dog()
dog.speak()  
dog.bark()   

cat = Cat()
cat.speak() 
cat.meow()   


# 4. Create a class to implement method Overriding.
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

animal = Animal()
dog = Dog()

animal.speak()  
dog.speak()  

'''Create a class for operator overloading which adds two Point Objects where Point has x & y values
e.g. if
P1(x=10,y=20)
P2(x=12,y=15)
P3=P1+P2 => P3(x=22,y=35)'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Overloading the addition operator."""
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type(s) for +: '{}' and '{}'".format(
                type(self).__name__, type(other).__name__))

    def __repr__(self):
        """String representation of the Point object."""
        return "Point(x={}, y={})".format(self.x, self.y)

P1 = Point(10, 20)
P2 = Point(12, 15)
P3 = P1 + P2

print(P3)  

