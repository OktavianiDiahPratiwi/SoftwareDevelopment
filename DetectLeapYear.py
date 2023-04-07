def DetectLeapYear(year):
 if year % 4 == 0:
       if year % 100 == 0:
           if year % 400 == 0:
               return True
           else:
               return False
       else:
           return True
 else:
       return False

year = 2003
if DetectLeapYear(year):
   print(year, "is a leap year")
else:
   print(year, "is not a leap year")