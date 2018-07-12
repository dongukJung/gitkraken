import datetime

name = raw_input("What is your name? ")
today = datetime.date.today()
day = today.day
month = today.month
if(day < 10): daystr = "0" + str(day)
else: daystr = str(day)
if(month < 10): mstr = "0" + str(month)
else: mstr = str(month)
tstr = mstr + "/" + daystr + "/" + str(today.year)
print("Hello, %s! Today is %s"%(name, tstr))
