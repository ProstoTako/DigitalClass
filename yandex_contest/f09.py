import time
sec_in_day = 24*60*60
date_format = "%d-%m-%Y"


entered_date = input()
struct_date = time.strptime(entered_date, date_format)
elapsed_day_from_monday = struct_date.tm_wday

if elapsed_day_from_monday == 0:
    print(entered_date)
else:
    elapsed_sec_from_monday = elapsed_day_from_monday * sec_in_day
    sec_utc_from_entered_date = time.mktime(struct_date)
    sec_utc_from_monday = sec_utc_from_entered_date - elapsed_sec_from_monday
    struct_date_of_monday = time.localtime(sec_utc_from_monday)
    date_of_monday = time.strftime(date_format, struct_date_of_monday)
    print(date_of_monday)
