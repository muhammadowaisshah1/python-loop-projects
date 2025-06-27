# 1. Counting Positive Numbers

# Problem: Given a list of numbers, count how many are positive.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]


number = [1, -2, 3, -4, 5, 6, -7, 8, 9, -10]
positive_number = 0

for num in number:
    if num > 0:
        positive_number += 1

print("Final Count of Positie number is :", positive_number)
