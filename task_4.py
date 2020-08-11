number = int(input("Positive integer: "))
max_num = 0
while number > 0:
    if max_num <= number % 10:
        max_num = number % 10
    number //= 10
print(f"Max numeral: {max_num}")
