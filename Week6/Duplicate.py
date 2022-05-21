# With a given list L, write a program to print L after removing all duplicate values with original order reserved.
#
# Example:
#
# If the input list is
#
# 12 24 35 24 88 120 155 88 120 155
#
# Then the output should be
#
# 12 24 35 88 120 155

def remove(duplicate):
    final_list = []

    for num in duplicate:
        if num not in final_list:
            final_list.append(num)

    return final_list

duplicate = [int(x) for x in input().split()]

final_list = remove(duplicate)

for i in final_list:
    print(i, end=' ')