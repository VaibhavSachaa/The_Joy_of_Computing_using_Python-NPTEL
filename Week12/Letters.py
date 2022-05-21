# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#
# Input Format:
# The first line of the input contains a statement.
#
# Output Format:
# Print the number of upper case and lower case respectively separated by a space.
#
# Example:
#
# Input:
# Hello world!
#
# Output:
# 1 9

s = input()
count_upper = 0
count_lower = 0

for i in range(len(s)):
    if s[i].isalpha():
        if s[i].isupper():
            count_upper += 1
        else:
            count_lower += 1

print(count_upper, count_lower, end='')