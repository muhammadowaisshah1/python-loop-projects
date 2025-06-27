# 5. Find the First Non-Repeated Character

# Problem: Given a string, find the first non-repeated character.

str = "hello"

for char in str:
    if str.count(char) == 1:
        print(char)
