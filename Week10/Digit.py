# You are provided with a number D containing only digits 0's and 1's. Your aim is to convert this number to have all
# the digits same. For that, you will change exactly one digit i.e. from 0 to 1 or from 1 to 0. If it is possible to
# make all digits equal (either all 0's or all 1's) by flipping exactly 1 digit then output "YES", else print "NO" (
# quotes for clarity).
#
# Input Format:
# The first line of the input contains the number D made of only digits 1's and 0's.
#
# Output:
# Print 'YES' or 'NO' depending on whether its possible to make it all 0s or 1s or not.
#
# Example-1:
#
# Input:
# 101
#
# Output:
# YES

# Example-2:
#
# Input:
# 11
#
# Output:
# NO
#
# Explanation: In the first example, it is possible to make all the digits same by flipping the middle digit from 0
# to 1. In the second example it is not possible.

n = input()
count_0 = 0
count_1 = 0
for digit in n:
    if digit == '0':
        count_0 = count_0 + 1
    if digit == '1':
        count_1 = count_1 + 1

if count_0 == 1 or count_1 == 1:
    print("YES", end="")
else:
    print("NO", end="")
