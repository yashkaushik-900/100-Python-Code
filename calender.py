#to create caleneder using library
import calendar
""" # Create a plain text calendar
cal = calendar.TextCalendar() 
# Display the calendar for a specific month and year
year = 2023
month = 3
print(cal.formatmonth(year, month))
 """
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))
calendar=calendar.month(year,month)
print(calendar)