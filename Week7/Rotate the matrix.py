# Given a square matrix with n rows and n columns, you have to write a program to rotate this matrix such that each
# element is shifted by one place in a clockwise manner. For example, given the following matrix
#
# 1 2 3
# 4 5 6
# 7 8 9
#
# The output should be
#
# 4 1 2
# 7 5 3
# 8 9 6
#
# Input Format:
# The first line of the input contains a number n representing the number of rows and columns.
# After this, there are n rows with each row containing n elements separated by a space
#
# Output Format: Print the elements of the modified matrix with each row in a new line and all the elements in each
# row is separated by a space.

n = int(input())
a = []
for i in range(n):
    b = [int(x) for x in input().split()]
    a.append(b)


def rotateMatrix(a):
    if not len(a):
        return
    """
    top: starting row index
    bottom: ending row index
    left: starting column index
    right: ending colum index
  
    """
    top = 0
    bottom = len(a[0]) - 1
    left = 0
    right = len(a[0]) - 1

    while left < right and top < bottom:
        # store the first element of next row
        # this will replace the first element of current row
        prev = a[top + 1][left]

        # move elements of top row one step right
        for i in range(left, right + 1):
            curr = a[top][i]
            a[top][i] = prev
            prev = curr

        top += 1

        # move elements of right most column one step downward
        for i in range(top, bottom + 1):
            curr = a[i][right]
            a[i][right] = prev
            prev = curr

        right -= 1

        # move elements of bottom row one step left
        for i in range(right, left - 1, -1):
            curr = a[bottom][i]
            a[bottom][i] = prev
            prev = curr

        bottom -= 1

        # move elements of last row column upwards
        for i in range(bottom, top - 1, -1):
            curr = a[i][left]
            a[i][left] = prev
            prev = curr

        left += 1

    return a


def printMatrix(a):
    for i in range(n):
        for j in range(n):
            if i + j < i + n - 1:
                print(a[i][j], end=" ")
            else:
                print(a[i][j], end="")

        if i < n - 1:
            print()
        # else:
        # return


matrix = rotateMatrix(a)
# Print modified matrix
printMatrix(matrix)
