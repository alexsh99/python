first = float(input("Result on the first day: "))
result = float(input("Desired result: "))
days = 1

while result >= first:
    first *= 1.1
    days += 1

print(f"Achieved results on day {days}")
