year = int(input('please enter your year of birth: '))
if (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
    print ('Hence, your year of birth is a leap year')
else:
    print(year, "is not a leap year.")
# if not divisible by both 400 and 4 (not a leap year)
