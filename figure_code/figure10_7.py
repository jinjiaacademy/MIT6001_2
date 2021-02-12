import datetime


class Person(object):

    def __init__(self, name):
        '''Assumes name a string. Create a person'''
        self._name = name
        try:
            last_blank = name.rindex(' ')
            self._last_name = name[last_blank+1:]
        except:
            self._last_name = name
        self.birthday = None

    def get_name(self):
        '''Returns self's full name'''
        return self._name

    def get_last_name(self):
        '''Returns self's last name'''
        return self._last_name

    def set_birthday(self, birthdate):
        '''Assumes birthdate is of type datetime.date
        Sets self's birthday to birthdate'''
        self._birthday = birthdate

    def get_age(self):
        '''Returns self's current age in days'''
        if self._birthday == None:
            raise ValueError
        return (datetime.date.today() - self._birthday).days

    def __lt__(self, other):
        '''Assumes other a Person
        Returns True if self precedes other in alphabetical
        order, and False otherwise. Comparison is based on last
        names, but if these are the same full names are compared.'''
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name

    def __str__(self):
        '''Returns self's name'''
        return self._name


class MIT_person(Person):

    _next_id_num = 0  # identification number

    def __init__(self, name):
        super().__init__(name)
        self._id_num = MIT_person._next_id_num
        MIT_person._next_id_num += 1

    def get_id_num(self):
        return self._id_num

    def is_student(self):
        return isinstance(self, Student)

    def __lt__(self, other):
        return self._id_num < other._id_num


class Student(MIT_person):
    pass


class UG(Student):
    def __init__(self, name, class_year):
        super().__init__(name)
        self._year = class_year

    def get_class(self):
        return self._year


class Grad(Student):
    pass


class Grades(object):

    def __init__(self):
        '''Create empty grade book'''
        self._students = []
        self._grades = {}
        self._is_sorted = True

    def add_student(self, student):
        '''Assumes: student is of type Student
        Add student to the grade book'''
        if student in self._students:
            raise ValueError('Duplicate student')
        self._students.append(student)
        self._grades[student.get_id_num()] = []
        self._is_sorted = False

    def add_grade(self, student, grade):
        '''Assumes: grade is a float
        Add grade to the list of grades for student'''
        try:
            self._grades[student.get_id_num()].append(grade)
        except:
            raise ValueError('Student not in mapping')

    def get_grades(self, student):
        '''Return a list of grades for student'''
        try:
            return self._grades[student.get_id_num()][:]
        except:
            raise ValueError('Student not in mapping')

    def get_students(self):
        '''Return a sorted list of the students in the grade book'''
        if not self._is_sorted:
            self._students.sort()
            self._is_sorted = True
        for s in self._students:
            yield s

    def get_students_above(self, grade):
        '''Return the students a mean grade > g one at a time'''
        for s in course.get_students():
            tot = 0.0
            num_grades = 0
            for g in course.get_grades(s):
                tot += g
                num_grades += 1
            try:
                average = tot/num_grades
                yield average
            except ZeroDivisionError:
                print('no grades available')

def grade_report(course):
    '''Assumes course is of type Grades'''
    report = ''
    for s in course.get_students():
        tot = 0.0
        num_grades = 0
        for g in course.get_grades(s):
            tot += g
            num_grades += 1
        try:
            average = tot/num_grades
            report = f"{report}\n{s}'s mean grade is {average}"
        except ZeroDivisionError:
            report = f"{report}\n{s} has no grades"
    return report


ug1 = UG('Jane Doe', 2021)
ug2 = UG('Pierce Addison', 2041)
ug3 = UG('David Henry', 2003)
g1 = Grad('Billy Buckner')
g2 = Grad('Bucky F. Dent')
six_hundred = Grades()
six_hundred.add_student(ug1)
six_hundred.add_student(ug2)
six_hundred.add_student(g1)
six_hundred.add_student(g2)
for s in six_hundred.get_students():
    six_hundred.add_grade(s, 75)
six_hundred.add_grade(g1, 25)
six_hundred.add_grade(g2, 100)
six_hundred.add_student(ug3)
print(grade_report(six_hundred))
# book = Grades()
# book.add_student(Grad('Julie'))
# book.add_student(Grad('Lisa'))
# for s in book.get_students():
#     print(s)
