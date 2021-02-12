import calendar as cal


def find_thanksgiving(year):
    month = cal.monthcalendar(year, 11)
    if month[0][cal.THURSDAY] != 0:
        thanksgiving = month[3][cal.THURSDAY]
    else:
        thanksgiving = month[4][cal.THURSDAY]
    return thanksgiving


def main():
    year = int(input('Enter a year: '))
    thanksgiving_day = find_thanksgiving(year)
    print(f'In the year of {year}, the US Thanksgiving was on Nov. {thanksgiving_day}')


if __name__ == '__main__':
    main()
