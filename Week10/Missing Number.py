# Given a list of n-1 numbers ranging from 1 to n, your task is to find the missing number. There are no duplicates.
#
# Input Format:
# The first line contains n-1 numbers with each number separated by a space.
#
# Output Format:
# Print the missing number
#
# Example:
#
# Input:
# 1 2 4 6 3 7 8
#
# Output:
# 5
#
# Explanation:
# In the above list of numbers 5 is missing and hence 5 is the input

num = [int(x) for x in input().split()]

sum = 0
found = 0
a = len(num) + 1
for i in num:
    sum = sum + i

found = (a * (a + 1)) // 2 - sum
print(found, end="")