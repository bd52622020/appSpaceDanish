#!/usr/bin/env python

from datetime import date, datetime

def checkdate():
	today = date.today()
	rn = datetime.now()
	day_of_year = (rn - datetime(today.year, 1, 1)).days + 1

	print("Current date and time: " , rn)
	print("Current year: " , today.strftime("%Y"))
	print("Current month of year: ", today.strftime("%B, of %Y"))
	print("Current day: ", today.strftime("%A") )
	print("Current Week number: " + str((today.isocalendar()[1]) ) + " of " + today.strftime("%Y") )
	print("Current Day of year: " , day_of_year)
	print("Current Day of the month: ", today.strftime("%d"))
	print( "Current Day of the week: " + str((today.isocalendar()[-1]) ) )

if __name__ == "__main__":
	checkdate()