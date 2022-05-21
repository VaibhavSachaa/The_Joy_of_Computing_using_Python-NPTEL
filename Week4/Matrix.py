# You saw how to create Magic Square of different sizes. It is very important to understand the way the matrices are
# represented and printed in python. In this assignment, you will be provided with the number of rows i.e. r and
# columns i.e. c as the input and your job is to create a matrix of size rxc. Also, the matrix should have elements
# starting from 1 to rxc with an increment of one in row manner.

# Example:

# if r = 2 and c = 3 then the output is

# 1 2 3
# 4 5 6

# Input Format:
# Two numbers r and c in a single line separated by a space.
#
# Output Format:
# Elements of the generated matrix.
# Each row should be printed in a new line with each element separated by a space

# NOTE: There should not be any extra space after the elements of the last column and no extra newline after the last
# row of the matrix.

r, c = map(int, input().split())

count = 1
m = []
for i in range(1, r + 1):
    l = []
    for j in range(1, c + 1):
        l.append(count)
        count += 1
    m.append(l)

for i in range(r):
    for j in range(c):
        if j == c - 1:
            print(m[i][j], end="")
        else:
            print(m[i][j], end=" ")
    if i != r - 1:
        print()
