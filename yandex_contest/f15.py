import json


def mean_age(json_string):
    data = json.loads(json_string)
    sum_ages = 0
    for item in data:
        sum_ages += item['age']
    mean_age = sum_ages / len(data)
    dict_mean_age = {'mean_age': mean_age}
    JSON_mean_age = json.dumps(dict_mean_age)
    return JSON_mean_age
