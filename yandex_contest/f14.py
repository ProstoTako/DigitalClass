def get_popular_name_from_file(filename: str) -> str:
    repeat_names_count = dict()
    with open(filename, 'rt') as fin:
        for line in fin:
            name, _ = line.split()
            repeat_names_count[name] = repeat_names_count.get(name, 0) + 1

    popular_score = max(repeat_names_count.values())
    popular_names = filter(lambda name: repeat_names_count[name] == popular_score, repeat_names_count)

    return ", ".join(sorted(popular_names))