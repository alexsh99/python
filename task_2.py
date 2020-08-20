def my_print(**kwargs):
    print(", ".join(map(lambda x: f"{x}: {kwargs[x]}", kwargs.keys())))


my_print(name="Вася", lastname="Пупкин", year="1990", city="London", email="aaa@aaa.uk", telephone="+44999333111")
