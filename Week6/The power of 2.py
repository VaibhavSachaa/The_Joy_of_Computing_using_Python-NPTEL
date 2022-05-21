# Write a program to find whether a given number is a power of 2 or not.
# Input format:
# The first line of the input contains the number n for which you have to find whether it is a power of 2 or not.
#
# Output Format:
# Print 'YES' or 'NO' accordingly without quotes.

def isPowerOfTwo(n):
    if n == 0:
        return False
    while n != 1:
        if n % 2 != 0:
            return False
        n = n // 2

    return True


a = int(input())

if isPowerOfTwo(a):
    print('YES')
else:
    print('NO')
