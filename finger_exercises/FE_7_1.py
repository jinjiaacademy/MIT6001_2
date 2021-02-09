'''
Write a function that meets the specification
'''
import calendar as cal

def find_thanksgiving(year):
	month = cal.monthcalendar(year, 11)
	if month[0][cal.THURSDAY] != 0:
		thanksgiving = month[3][cal.THURSDAY]
	else:
		thanksgiving = month[4][cal.THURSDAY]
	return thanksgiving


def shopping_days(year):
	'''year a number >= 1941
	returns the number of days between U.S. Thanksgiving and Xmas
	in year.'''
	return 30 - find_thanksgiving(year) + 24



def main():
	year = int(input('Enter a year: '))
	thanksgiving_day = shopping_days(year)
	print(f'In the year of {year}, there are {thanksgiving_day} days between thanksgiving and Xmas. ')

if __name__ == '__main__':
	main()	
