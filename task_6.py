def my_func_upper(s: str):  # Да аннотация не нужна если переменна попадает из под input, просто попробовал
    result = []
    for i in s.split(" "):  # Специально сделано с " " для сохранения пробелов как в исходной строке
        result.append(i[0:1].upper() + i[1:])
    return " ".join(result)


def my_func_chr(s: str):
    result = []
    for i in s.split(" "):
        result.append((chr(ord(i[0:1]) - 32) if 97 <= ord(i[0:1]) <= 122 else i[0:1]) + i[1:])
    return " ".join(result)


in_str = input("Слово из маленьких латинских букв: ")
print(f"Вариант через .upper() = {my_func_upper(in_str)}")
print(f"Вариант через chr() и ord() = {my_func_chr(in_str)}")
print(f"Вариант через .title() = {in_str.title()}")
