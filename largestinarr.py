import os

nums = raw_input("Enter the array elements with space ")

list = nums.split()

large = list[0]

for num in list:
    if large <= num:
        large = num;

print ("The largest in array is =", large)
         

