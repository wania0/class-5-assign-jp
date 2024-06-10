# QUES : 16 

# Find Common Elements Between Two Lists
# Objective: Write a Python program that finds and prints the common elements between two lists.
# Example lists
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]

# SOLUTION:

list1 = [1, 2, 3, 4, 5]

list2 = [4, 5, 6, 7, 8]

common_elements = []

for i in list1 :
    if i in list1 and i in list2:
        common_elements.append(i)

print("The common elements between two lists are:", common_elements)