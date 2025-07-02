#pip install datetime
from datetime import datetime, date, time, timedelta
import pytz

#now method is used to get the current date and time
current = datetime.now()
print("Current Date & Time: ", current)

present_date = datetime.today()
print("Date: ", present_date)

#printing the today's date in this format: dd-mm-yyyy
present_date = current.strftime("%d-%m-%Y")
print(present_date)

#printing the today's date in this format: dd/mm/yyyy
present_date = current.strftime("%d/%m/%Y")
print(present_date)
print("Current Date: ", current.strftime("%d"))
print("Current Month in number: ", current.strftime("%m"))
print("Current Year: ", current.strftime("%Y"))
print("Current Year (Short-form): ", current.strftime("%y"))

#printing the date with month in words. represented in small m if M represent the minute
print("Current month (Short-form): ", current.strftime("%b"))
print("Current month (Full Name): ", current.strftime("%B"))
print("Current Day (Short-form): ", current.strftime("%a"))
print("Current Day (Full Name): ", current.strftime("%A"))
second_date = date(2003, 10, 3) #date(yyyy, m/mm, d/dd)
print("The given month (Short-form): ", second_date.strftime("%b"))
print("The given month (Full Name): ", second_date.strftime("%B"))
print("THe given Day (Short-form): ", second_date.strftime("%a"))
print("THe given Day (Full Name): ", second_date.strftime("%A"))

dob = datetime(2003, 10, 3, 12,10, 5) #datetime(yyyy, m/mm, d/dd, h/hh, m/mm, s/ss)
today = datetime(2025, 5, 14, 12, 57, 0) #today = datetime.now()
difference = today - dob
print("The duration b/w both the dates: ", difference)

day_number = current.timetuple().tm_yday
print("Day number of the year: ", day_number)

week_number = current.strftime("%U")
print("Day number of the year: ", week_number)

#printing the current hour, minute & second
print("Current Hour in 24H format: ", current.strftime("%H"))
print("Current Hour in 12H format: ", current.strftime("%I"))
print("Current Minute: ", current.strftime("%M"))
print("Current Second: ", current.strftime("%S"))

print("Current time in 12H format:", current.strftime("%I:%M %p"))
print("Current time in 24H format:", current.strftime("%H:%M %p"))

#printing date in different format
print("Date with hypens: ", current.strftime("%d-%M-%Y"))
print("Date with Month Name: ", current.strftime("%d-%b-%Y"))
print("Date with Month Name: ", current.strftime("%d %b %Y"))
print("Date: ", current.strftime("%b %d, %Y"))
print("Date: ", current.strftime("%d/%m/%y"))
print("Date with time(24H): ", current.strftime("%b %d, %Y %H:%M %p"))
print("Date with time(24H): ", current.strftime("%b %d, %Y %I:%M %p"))
print("Date with time(24H): ", current.strftime("%b %d, %Y %H:%M:%S %p"))
print("Date with time(24H): ", current.strftime("%b %d, %Y %I:%M:%S %p"))

#Converting the Date to String:"strftime" - String format time
#Converting the String to Date: "strptime" - String parse time
today = "14-05-2025"
converted_date = datetime.strptime(today, "%d-%m-%Y")
print("Modified the String to Date: ", converted_date)

#Checking the current timezone and time 
time_zone = datetime.now(pytz.timezone('Asia/Kolkata'))
time_zone_dubai = datetime.now(pytz.timezone('Asia/Dubai'))
time_zone_ny = datetime.now(pytz.timezone('America/New_York'))
time_zone_gmt = datetime.now(pytz.timezone('Africa/Lome'))
print("Current Timezone's Time: ", time_zone)
print("Dubai Time: ", time_zone_dubai)
print("NewYork Time: ", time_zone_ny)
print("Greenwich Mean Time: ", time_zone_gmt)

#Add or Subtract Days from current date
next_day = current + timedelta(days=1)
prev_day = current - timedelta(days=1)
print("Tomorrow: ", next_day.strftime("%d-%m-%Y"))
print("Yesterday: ", prev_day.strftime("%d-%m-%Y"))