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


class Politician(Person):
    '''A politician is a person who can belong to a political party'''

    def __init__(self, name, party=None):
        '''name and party are string'''
        super().__init__(name)
        self._party = party

    def get_party(self):
        '''returns the party to which self belongs'''
        return self._party

    def might_agree(self, other):
        '''returns True if self and other belong to the same part
        or at least one of then does not belong to a party'''
        return self._party == other._party
