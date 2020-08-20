def my_func(*args):
    args = list(args)
    args.remove(min(args))
    return sum(args)


print(my_func(131, 820, 200))
