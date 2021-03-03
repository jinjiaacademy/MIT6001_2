class Location(object):
    def __init__(self, x, y):
        '''x and y are numbers'''
        self._x, self._y = x, y

    def move(self, delta_x, delta_y):
        '''delta_x and delta_y are numbers'''
        return Location(self._x + delta_x, self._y + delta_y)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def dist_from(self, other):
        ox, oy = other._x, other._y
        x_dist, y_dist = self._x - ox, self._y - oy
        return (x_dist**2 + y_dist**2)**0.5

    def __str__(self):
        return f'<{self._x}, {self._y}>'


class Field(object):
    def __init__(self):
        self._drunks = {}

    def add_drunk(self, drunk, loc):
        if drunk in self._drunks:
            raise ValueError('Duplicate drunk')
        else:
            self._drunks[drunk] = loc

    def move_drunk(self, drunk):
        if drunk not in self._drunks:
            raise ValueError('Drunk not in field')
        x_dist, y_dist = drunk.take_step()
        current_location = self._drunks[drunk]
        # use move method of Location to get new Location
        self._drunks[drunk] = current_location.move(x_dist, y_dist)

    def get_loc(self, drunk):
        if drunk not in self._drunks:
            raise ValueError('Drunk not in field')
        return self._drunks[drunk]
