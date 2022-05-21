# Write a Python program to add the digits of a positive integer repeatedly until the result has a single digit.
#
# Input Format:
# The first line of the input contains a number n.
#
# Output:
# Print the resultant number
#
# Example:
# Input:
# 48
#
# Output:
# 3

n = int(input())


def add_digits(n):
    return (n - 1) % 9 + 1 if n > 0 else 0


print(add_digits(n), end="")
