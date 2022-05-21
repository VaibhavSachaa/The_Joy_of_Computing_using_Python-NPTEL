# Given a square matrix, you have to write a program to print it in a counter-clockwise spiral form.
#
#
# Input Format:
# The first line of the input contains a number n which represents the number of rows and columns in the matrix.
# From the second line contains the n rows with each row having n elements separated by a space.
#
# Output Format:
# Print the elements in a single line with each element separated by a space
#
# Example:
#
# Input:
# 4
# 25 1 29 7
# 24 20 4 32
# 16 38 29 1
# 48 25 21 19
#
# Output:
# 25 24 16 48 25 21 19 1 32 7 29 1 20 38 29 4

n = int(input())
a = []
for i in range(n):
    b = [int(x) for x in input().split()]
    a.append(b)


def rotateMatrix(m, n, mat):
    if not len(mat):
        return

    k = 0
    l = 0
    p = n - 1
    q = n - 1

    while k < m and l < n:
        for i in range(k, p + 1):
            if k == p and l == q:
                print(mat[i][k], end="")
            else:
                print(mat[i][k], end=" ")

        k += 1

        for i in range(k, q + 1):
            print(mat[q][i], end=" ")

        q -= 1

        for i in range(p - 1, l - 1, -1):
            print(mat[i][p], end=" ")

        p -= 1

        for i in range(p, l, -1):
            print(mat[l][i], end=" ")

        l += 1

    return mat


rotateMatrix(n, n, a)