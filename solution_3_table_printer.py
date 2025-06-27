# 3. Multiplication Table Printer

# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = 8

for i in range(1, 10 + 1):
    if i == 5:
        continue
    print(f" {number} X {i} = {number * i} ")
