# Let us assume paper as the plane and a letter as a curve on the plane, then each letter divides the plane into
# regions. For example letters "A", "D", "O", "P", "R" divide the plane into two regions so we say these letters each
# have one hole. Similarly, letter "B" has two holes and letters such as "C", "E", "F", "K" have no holes. We say
# that the number of holes in the text is equal to the total number of holes in the letters of the text. Write a
# program to determine how many holes are in a given text.
#
# Input Format:
# The only line contains a non-empty text composed only of uppercase letters of English alphabet.
#
# Output Format:
# output a single line containing the number of holes in the corresponding text.
#
# Example-1
#
# Input:
# DRINKEATCODE
#
# Output:
# 5
#
#
# Explanation:
# D R A O D has one hole hence total number of holes in the text is 5.

l = input()
one_hole = ['A', 'D', 'O', 'P', 'R', 'Q']
total = 0
for i in l:
    if i in one_hole:
        total = total + 1
    elif i == 'B':
        total = total + 2

print(total, end='')