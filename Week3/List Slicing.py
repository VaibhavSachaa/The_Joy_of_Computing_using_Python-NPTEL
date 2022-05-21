# In this program, create a list of numbers from 1 to 50 named list_1. The numbers should be present in the
# increasing order: Ex list_1 = [1,2,3,4,5,....,50] i.e. index zero should be 1, index one should be 2,
# index two should be 3 and so on. Given an input of two numbers, let's say a and b, you have to print the numbers
# returned by the following command list_1[a:b]
# Input:

# The first line of input contains two numbers a and b separated by a space.

# NOTE: You can take two inputs in a single line using the following command:

# a, b = input().split()

# Make sure you convert the strings in a and b into integers using the int() command

# Output: Print the numbers in new line

list_1 = []
for i in range(1, 51):
    list_1.append(i)
a, b = input().split()
a = int(a)
b = int(b)
for i in list_1[a:b]:
    print(i)
