# Write a program that accepts a comma-separated sequence of words as input and prints the words in a comma-separated
# sequence after sorting them alphabetically.
#
# Input Format:
# The first line of input contains words separated by the comma.
#
# Output Format:
# Print the sorted words separated by the comma.
#
# Example:
#
# Input:
# without,hello,bag,world
#
# Output:
# bag,hello,without,world

words = [x for x in input().split(',')]

words_sorted = sorted(words)

for i in range(len(words_sorted) - 1):
    print(words_sorted[i], end=',')

print(words_sorted[-1], end='')