# Python can easily handle large numbers. You can store a huge number easily in python.
# In this program, you have to calculate the Factorial of a number.
# Given a number k its factorial is i.e. k! = 1x2x3x4x....xk.
# For example, if k = 4, 4! = 1x2x3x4 = 24

# Input format: The number k in a single line
# Output Format: k! in a single line

k = int(input())
factorial = 1
for i in range(1, k + 1):
    factorial = factorial * i
print(factorial, end="")
