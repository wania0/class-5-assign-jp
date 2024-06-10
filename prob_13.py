# QUES : 13

# Count Even and Odd Numbers in a List
# Objective: Write a Python program that counts the number of even and odd numbers in a given list.
# Example list
# numbers = [12, 7, 9, 24, 18, 5, 3, 20]

# SOLUTION:

numbers = [12, 7, 9, 24, 18, 5, 3, 20]

even_counter = 0

odd_counter = 0

for elements in numbers:
    if elements % 2 == 0:
        even_counter = even_counter + 1
    else:
        odd_counter = odd_counter + 1
        
print("The number of even numbers in the list is:", even_counter)

print("The number of odd numbers in the list is:", odd_counter)