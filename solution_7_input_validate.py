# 7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.


while True:
    user_input = int(
        input(
            "Enter a Number Between 1 to 10 :",
        )
    )
    if 1 <= user_input <= 10:
        print(f"Thanks you Enter a Right number {user_input}")
        exit()
    else:
        print("Enter valid number ")
