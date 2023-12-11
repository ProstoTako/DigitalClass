def lists_sum(*args: list, unique=False):
    summ = 0
    if unique:
        args_set = set()
        for arg in args:
            args_set = args_set | set(arg)
        summ = sum(args_set)
    else:
        for arg in args:
            summ += sum(arg)
    return summ
