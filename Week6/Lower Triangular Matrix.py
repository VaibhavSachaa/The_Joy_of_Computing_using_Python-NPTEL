# A lower triangular matrix is a square matrix (where the number of rows and columns are equal)  where all the
# elements above the diagonal are zero. For example, the following is a lower triangular matrix with the number of
# rows and columns equal to 3.
#
# 1 0 0
# 4 5 0
# 7 8 9
#
# Write a program to convert a square matrix into a lower triangular matrix.

# Input Format:
# The first line of the input contains a number n which represents the number of rows and the number of columns.
# From the second line, take n lines input with each line containing n elements with each element separated by a space.
#
# Output format:
# Print the elements of the matrix with each row in a new line and each element separated by a space.

n = int(input())
a = []
for i in range(n):
    b = [int(x) for x in input().split()]
    a.append(b)

for i in range(n):
    for j in range(n):
        if j > i:
            a[i][j] = 0

for i in range(n - 1):
    for j in range(n - 1):
        print(a[i][j], end=' ')
    for k in range(n - 1, n):
        print(a[i][k], end='')
    print()

for i in range(n - 1, n):
    for j in range(n - 1):
        print(a[i][j], end=' ')

print(a[n - 1][n - 1], end='')
