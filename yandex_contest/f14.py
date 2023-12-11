def get_popular_name_from_file(filename: str) -> str:
    dict_names = dict()
    with open(filename, 'rt') as fin:
        for line in fin:
            name, second_name = line.split()
            if name in dict_names:
                dict_names[name] += 1
            else:
                dict_names[name] = 1

    max_count_repeat = 0
    list_popular_names = list()
    for name, count_repeat in dict_names.items():
        if count_repeat > max_count_repeat:
            list_popular_names.clear()
            list_popular_names.append(name)
            max_count_repeat = count_repeat
        elif count_repeat == max_count_repeat:
            list_popular_names.append(name)

    separator = ', '
    popular_names = separator.join(list_popular_names)
    return popular_names
