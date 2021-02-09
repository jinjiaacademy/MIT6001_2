'''
Since 1958, Canadian Thanksgiving has occured on the second Monday
in October. Write a function that takes a year (>1957) as a parameter,
and returns the number of days between Canadian Thanksgiving and Xmas.
'''
import calendar as cal

def find_thanksgiving_canada(year):
	month = cal.monthcalendar(year, 10)
	if month[0][cal.MONDAY] != 0:
		thanksgiving = month[1][cal.MONDAY]
	else:
		thanksgiving = month[2][cal.MONDAY]
	return thanksgiving

def main():
	year = int(input('Enter a year: '))
	thanksgiving_day_canada = find_thanksgiving_canada(year)
	days_thanks_xmas = 31 - thanksgiving_day_canada + 30 + 24
	print(f'In the year of {year}, there are {days_thanks_xmas} days between thanksgiving and Xmas in Canada.')

if __name__ == '__main__':
	main()	