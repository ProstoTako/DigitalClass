from re import match


sum = 0
while True:
    value = input()
    if value == '':
        break

    is_not_int_number = match('[-][0-9]*[^0-9]', value)
    if is_not_int_number:
        continue

    number = int(value)
    if number % 2 == 0:
        sum += number

print(sum)
