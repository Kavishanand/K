#assignment 12

year=int(input('which year is leap year'))
print(year)

if (year %400 ==0) or (year %4 ==0) and (year %100!=0):
    print('leap year')
else:
    print('not leap year')