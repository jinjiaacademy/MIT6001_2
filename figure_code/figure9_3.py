def get_grades(fname):
    grades = []
    try:
        with open(fname, 'r') as grades_file:
            for line in grades_file:
                try:
                    grades.append(float(line))
                except:
                    raise ValueError('Cannot convert line to float')
    except IOError:
        raise ValueError('get_grades could not open ' + fname)
    return grades


try:
    grades = get_grades('quiz1grades.txt')
    grades.sort()
    median = grades[len(grades)//2]
    print('Median grade is', median)
except ValueError as error_msg:
    print('Whoops.', error_msg)
