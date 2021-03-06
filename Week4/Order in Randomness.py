# You all have used the random library of python. You have seen in the screencast how powerful it is.
# In this assignment, you will sort a list let's say list_1 of numbers in increasing order using the random library.
#
# Following are the steps to sort the numbers using the random library.
#
# Step 1: Import the randint definition of the random library of python.
#
# Step 2: Take the elements of the list_1 as input.
#
# Step 3: randomly choose two indexes i and j within the range of the size of list_1.
#
# Step 4: Swap the elements present at the indexes i and j. After doing this, check whether the list_1 is sorted or not.
#
# Step 5: Repeat step 3 and 4 until the array is not sorted.
#
# Input Format:
# The first line contains a single number n which signifies the number of elements in the list_1.
# From the second line, the elements of the list_1 are given with each number in a new line.
#
# Output Format:
# Print the elements of the list_1 in a single line with each element separated by a space.
# NOTE 1: There should not be any space after the last element.

# NOTE 2: There are many ways to sort the elements of a list. The purpose of this assignment is to show the power of
# randomness, and obviously the Joy.

from random import randint

n = int(input())
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

sorted = True

while sorted:
    j = randint(0, n - 1)
    i = randint(0, n - 1)
    arr[i], arr[j] = arr[j], arr[i]
    for k in range(0, n - 1):
        if arr[k] > arr[k + 1]:
            sorted = False

    if sorted:
        break
    else:
        sorted = True

for i in range(n):
    if i == n - 1:
        print(arr[i])
    else:
        print(arr[i], end=" ")

