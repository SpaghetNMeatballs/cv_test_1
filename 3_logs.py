import calendar

DD, Month, YYYY, time = input().split()
for i in range(1, 13):
    if calendar.month_abbr[i] == Month:
        month_number = str(i)
        if len(month_number) < 2:
            month_number = '0' + month_number
hours, minutes, seconds = time.split(":")
name = input()
version = input()
worktime = int(round(float(input()), 0))
load_flag = int(input()) >= 90
result = f'{YYYY}-{month_number}-{DD}_{hours}-{minutes}_{name}_v{version}_t{worktime}' + load_flag * '_hard'
print(result)
