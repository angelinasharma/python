# 1. Create numpy array to find sum of all elements in an array

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

total_sum = np.sum(arr)
print("Sum of all elements in the array:", total_sum)

# 2. Create numpy array of (3,3) dimension. Now find sum of all rows & columns individually. 
# Also find 2nd maximum element in the array.  

arr_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

row_sums = np.sum(arr_2d, axis=1)
print("Sum of each row:", row_sums)

column_sums = np.sum(arr_2d, axis=0)
print("Sum of each column:", column_sums)

second_max = np.partition(arr_2d.flatten(), -2)[-2]
print("Second maximum element in the array:", second_max)

# 3. Perform Matrix multiplication of any 2 n*n matrices.

mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])

result = np.dot(mat1, mat2)
print("Matrix multiplication result:")
print(result)

# 4. Write a Pandas program to get the powers of an array values element-wise. 

import pandas as pd

data = {'X': [78, 85, 96, 80, 86], 'Y': [84, 94, 89, 83, 86], 'Z': [86, 97, 96, 72, 83]}
df = pd.DataFrame(data)

powers = df.applymap(lambda x: x ** 2)
print(powers)

# 5. Write a Pandas program to get the first 3 rows of a given DataFrame.

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)

first_three_rows = df.head(3)
print("First three rows of the data frame:")
print(first_three_rows)

# 6. Write a Pandas program to find and replace the missing values in a given DataFrame 
# which do not have any valuable information.

import pandas as pd

data = {'A': [1, 2, None, 4, None],
        'B': [5, None, None, 8, 9],
        'C': [None, 12, 13, None, 15]}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

threshold = 0.7

missing_percentage = df.isnull().sum() / len(df)

for column in df.columns:
    if missing_percentage[column] < threshold:
        df[column].fillna(value="Unknown", inplace=True)

print("\nDataFrame after replacing missing values:")
print(df)

# 7. Create a program to demonstrate different visual forms using Matplotlib.

import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Line plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='sin(x)', color='blue', linestyle='-')
plt.title('Line Plot')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.show()

# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, label='sin(x)', color='red', marker='o')
plt.title('Scatter Plot')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.show()

# Bar plot
categories = ['A', 'B', 'C', 'D', 'E']
values = [20, 35, 30, 25, 40]
plt.figure(figsize=(8, 6))
plt.bar(categories, values, color='green')
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(axis='y')
plt.show()

# Histogram
data = np.random.randn(1000)
plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, color='purple', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()

# Pie chart
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen'])
plt.title('Pie Chart')
plt.axis('equal')
plt.show()





