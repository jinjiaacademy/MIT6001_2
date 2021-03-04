class Odd_field(Field):
    def __init__(self, numHoles, x_range, y_range):
        Field.__init__(self)
        self.wormholes = {}
        for w in range(numHoles):
            x = random.randint(-x_range, x_range)
            y = random.randint(-y_range, y_range)
            newX = random.randint(-x_range, x_range)
            newY = random.randint(-y_range, y_range)
            newLoc = Location(newX, newY)
            self.wormholes[(x, y)] = newLoc

    def move_drunk(self, drunk):
        Field.move_drunk(self, drunk)
        x = self.drunks[drunk].get_x()
        y = self.drunks[drunk].get_y()
        if (x, y) in self.wormholes:
            self.drunks[drunk] = self.wormholes[(x, y)]
