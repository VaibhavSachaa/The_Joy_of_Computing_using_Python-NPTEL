# Given a string S having characters from English alphabets ['a' - 'z'] and '.' as the special character (without
# quotes). Write a program to construct the lexicographically smallest palindrome by filling each of the faded
# character ('.') with a lower case alphabet.
#
# Definition: The smallest lexicographical order is an order relation where string s is smaller than t,
# given the first character of s (s1 ) is smaller than the first character of t (t1 ), or in case they are
# equivalent, the second character, etc.
#
# For example "aaabbb" is smaller than "aaac" because although the first three characters
# are equal, the fourth character b is smaller than the fourth character c.
#
# Input Format:
# String S
#
# Output Format:
# Print lexicographically smallest palindrome after filling each '.' character, if it
# possible to construct one. Print -1 otherwise.

s = input()
l = []

for i in range(len(s)):
    if s[i] == s[-1 - i]:
        if s[i] != '.':
            l.append(s[i])
        else:
            l.append('a')

    else:
        print(-1, end='')
        break

    print(l[i], end='')
