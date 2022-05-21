# You have seen in the videos that how powerful dictionary data structure is. In this assignment, given a number n,
# you have to write a program that generates a dictionary d which contains (i, i*i), where i is from 1 to n (both
# included). Then you have to just print this dictionary d.


n = int(input())
dic = {}
for i in range(1, n + 1):
    dic[i] = i * i

print(dic)
