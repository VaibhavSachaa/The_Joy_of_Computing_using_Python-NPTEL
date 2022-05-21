# Given the marks of five subjects, you have to calculate and print the average of the total marks.

# Input:Marks of different subjects in new line.
# Output: output the average number

s = 0
for i in range(5):
    x = int(input())
    s = s+x

num = s/5

print(num)
