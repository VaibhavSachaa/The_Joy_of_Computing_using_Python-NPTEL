# Write a Python program to push all zeros to the end of a given list a. The order of the elements should not change.
#
# Input Format: Elements of the list a with each element separated by a space.
#
# Output Format: Elements of the modified list with each element separated by a space. After the last element,
# there should not be any space.
#
# Example:
#
# Input:
# 0 2 3 4 6 7 10
#
# Output:
# 2 3 4 6 7 10 0

a = [int(x) for x in input().split()]

for i in range(len(a) - 1):
    for j in range(len(a) - i - 1):
        if a[j] == 0:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp

for i in range(len(a)):
    if i == len(a) - 1:
        print(a[i], end="")
    else:
        print(a[i], end=" ")