# You are a poor person in an island. There is only one shop in this island, this shop is open on all days of the
# week except for Sunday. Consider following constraints:
#
# N – Maximum unit of food you can buy each day. S – Number of days you are required to survive. M – Unit of food
# required each day to survive. Currently, it’s Monday, and you need to survive for the next S days. Find the minimum
# number of days (ceil value) on which you need to buy food from the shop so that you can survive the next S days,
# or determine that it isn’t possible to survive.
#
# Input Format:
# The first line of the input contains three numbers S, N and M separated by space.
#
# Output Format:
# If it is possible to survive the print the number of days, otherwise print 'NO' without quotes.

S, N, M = map(int, input().split())

if M > N or (6 * (N - M)) < M:
    print('NO', end="")
else:
    print(((S * M) // N) + 1, end="")
