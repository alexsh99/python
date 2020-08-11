user_input = int(input('Time in seconds: '))
user_input = user_input % 86400
hour = user_input // 3600
minute = (user_input % 3600) // 60
sec = user_input - hour * 3600 - minute * 60
print(f"{hour:02}:{minute:02}:{sec:02}")
