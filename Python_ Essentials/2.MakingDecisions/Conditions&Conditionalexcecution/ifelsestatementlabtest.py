year = int(input("Enter a year: "))

if year < 1582 :
    year ="Not within the Gregorian calender period"
elif year % 4 != 0:
    year = 'common year'
elif year % 100 != 0:
    year = "leap year"
elif year % 400 != 0:
    year = "common year"
else:
    year= "leap year"
    
  



print(year)