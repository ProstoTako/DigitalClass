def gift_count(budget: int, month: int, birthdays: dict):
    sorted_birthdays = sorted(birthdays.items(), key=lambda item: item[1].day)
    string = f"Именинники в месяце {month}: "
    count_birthday_man = 0
    for birthday_man in sorted_birthdays:
        if birthday_man[1].month == month:
            string += f"{birthday_man[0]} {birthday_man[1].strftime('(%d.%m.%Y)')}, "
            count_birthday_man += 1
    if count_birthday_man == 0:
        print("В этом месяце нет именинников.")
    else:
        string = string[:len(string) - 2] + ". "
        gift_money = int(budget / count_birthday_man)
        string += f"При бюджете {budget} они получат по {gift_money} рублей."
        print(string)
