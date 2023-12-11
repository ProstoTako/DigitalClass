numbers = []
count = 5

while count:
    try:
        number = int(input())
    except:
        print("Oops, it's not number")
        continue
    numbers.append(number)
    count -= 1

numbers.sort(reverse=True)
for number in numbers:
    print(number)
