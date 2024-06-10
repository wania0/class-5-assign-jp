# QUES : 14

# Print List Elements with Their Indices
# Objective: Write a Python program that prints each element of a list along with its index.
# Example list
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# output should like
# "Index: 0 Element: apple"
# "Index: 1 Element: banana"
# "Index: 2 Element: cherry"

# SOLUTION:

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for i in range(len(fruits)):
    print("Index:", i, "Element:", fruits[i])