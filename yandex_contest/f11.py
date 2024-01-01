def lists_sum(*args: list, unique=False):
    list_nums = []
    for nums in args:
        list_nums.extend(nums)
    return sum(list_nums) if not unique else sum(set(list_nums))