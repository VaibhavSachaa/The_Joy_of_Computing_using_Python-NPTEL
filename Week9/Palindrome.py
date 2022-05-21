# Given a string, write a program to check if it is palindrome or not. A string is said to be a palindrome if the
# reverse of the string is the same as string. For example, "NITIN" is a palindrome but "AMIT" is not.
#
# Input Format:
# The first line of input contains the string (all characters in lower case) which has to be checked.
#
# Output Format:
# Print 'YES' or 'NO' accordingly.

def isPalindrome(s):
    if s != s[::-1]:
        print("NO")
    else:
        print("YES")


s = input()
isPalindrome(s)
