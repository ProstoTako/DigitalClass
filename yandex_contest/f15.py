import json
from functools import reduce


def mean_age(json_string):
    ages = [dictanory["age"] for dictanory in json.loads(json_string)]
    sum_ages = reduce(lambda x, y: x + y, ages)
    return json.dumps({"mean_age": sum_ages / len(ages)})