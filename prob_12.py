# QUES : 12

# Exercise 1: Sum of Elements in a List
# Objective: Write a Python program that calculates the sum of all elements in a given list.
# Example list
# numbers = [10, 20, 30, 40, 50]

#SOLUTION:

numbers = [10, 20, 30, 40, 50]
sum = 0

for elements in numbers:
    sum = sum + elements

print("The sum of all elements in the list is:", sum)