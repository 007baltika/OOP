import time


# year = int(input())
# month = int(input())

day = 'February, 2015'
result = time.strptime(day, '%B, %Y')
month_first_day = result[6]
print(28 - 3 - month_first_day)

# print(f'{day:02}.{month:02}.{year:04}')