# In this program, create a list of numbers from 1 to 50 named list_1. The numbers should be present in the
# increasing order: Ex list_1 = [1,2,3,4,5,....,50] i.e. index zero should be 1, index one should be 2,
# index two should be 3 and so on.

# Given an input let's say a, you have to print the number of elements of list_1 which are divisible by a,
# excluding the element which is equal to a.
#
# Input: Number a
#
# Output: In a single line, the number of elements (i.e. the count and not the elements) which are divisible by a.


list_1 = []
for i in range(1, 51):
    list_1.append(i)
a = input()
a = int(a)
count = 0
for i in list_1:
    if i != a and i % a == 0:
        count = count + 1
print(count)
