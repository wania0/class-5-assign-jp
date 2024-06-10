# QUES : 11 

# 8. Write a Python program to get the largest number from a list and use for loop consider the list [3, 5, 2, 1, 4]
# output should be 5
# hint:
# create a variable x outside the loop and assign the value 0
# inside the loop compare the variable x with the local variable of loop

#SOLUTION:

all_item = [3, 5, 2, 1, 4]
x = 0

for i in all_item:
    if i > x:
        x = i

print("The largest number is:", x)