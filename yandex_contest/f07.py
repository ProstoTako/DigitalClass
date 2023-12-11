string = input().lower()
separator = ', '

list_string = string.split(separator)
set_string = set(list_string)
new_list_string = list(set_string)
new_list_string.sort()

new_string = separator.join(new_list_string)
print(new_string)
