# 2.1 & 2.2
min = 60
sec = 60
hour = min * sec
seconds_per_hour = hour
result = f'2.1 & 2.2 : {seconds_per_hour}'
print(result)

# 2.3 & 2.4
seconds_per_day = seconds_per_hour * 24
result = f'2.3 & 2.4 : {seconds_per_day}'
print(result)

# 2.5
result = seconds_per_day/seconds_per_hour
print(result)

# 2.6
result = seconds_per_day//seconds_per_hour
print(result)