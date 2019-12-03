# year = int(input("please input a year: "))

# if year % 4 == 0 and year %100 != 0:
# 	print('True')
# elif year % 400 == 0:
# 	print('True')
# else:
# 	print('False')

year = int(input('请输入年份: '))

is_leap = (year % 4 == 0 and year %100 != 0) or \
(year % 400 == 0)

print is_leap(year)