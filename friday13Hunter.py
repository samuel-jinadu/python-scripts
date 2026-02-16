try:
	import time, datetime, calendar
	from tabulate import tabulate
	
	fri13dates_forward = []
	fri13dates_backward = []
	HOW_MANY_DATES = 13
	
	present = datetime.datetime.now()
	current_year = int(present.strftime("%Y"))
	future_year = int((present + datetime.timedelta(days = 365 *1000)).strftime("%Y"))
	past_year = int((present - datetime.timedelta(days = 365 *1000)).strftime("%Y"))
	years_forward = list(range(current_year, future_year))
	years_backward = list(range(current_year, past_year, -1))
except Exception as e:
	print(e)
	input()



try:
	for year in years_forward:
		for month_index in range(1, 13):
			date = datetime.date(year, month_index, 13)
			if date.weekday() == 4 and date > present.date() and len(fri13dates_forward) < HOW_MANY_DATES:
				fri13dates_forward.append(date)
		if len(fri13dates_forward) == HOW_MANY_DATES:
			break
except Exception as e:
	print(e)
	input()



try:
	for year in years_backward:
		for month_index in range(1, 13):
			date = datetime.date(year, month_index, 13)
			if date.weekday() == 4 and date < present.date() and len(fri13dates_backward) < HOW_MANY_DATES:
				fri13dates_backward.append(date)
		if len(fri13dates_backward) == HOW_MANY_DATES:
			break
except Exception as e:
	print(e)
	input()


try:
	print(tabulate([[d.strftime("%B %Y")] for d in fri13dates_forward], headers=["Future Friday the 13th Dates"]), "\n")
	print(tabulate([[d.strftime("%B %Y")] for d in fri13dates_backward], headers=["Past Friday the 13th Dates"]))
	input()
except Exception as e:
	print(e)
	input()