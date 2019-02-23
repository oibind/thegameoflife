class Cell:

    def __init__(self, field, x, y):
        self.x = x
        self.y = y

        self.field = field

    def ns(self):
        return [n for n in [self.field.get((self.x -1, self.y -1), None), 
            self.field.get((self.x, self.y -1), None), 
            self.field.get((self.x + 1, self.y - 1), None), 
            self.field.get((self.x - 1, self.y), None), 
            self.field.get((self.x + 1, self.y), None), 
            self.field.get((self.x - 1, self.y + 1), None), 
            self.field.get((self.x, self.y +1), None), 
            self.field.get((self.x + 1, self.y +1), None)] if n]

    def lives(self) -> bool:
        if len(self.ns()) == 2 or len(self.ns()) == 3:
            return True
        return False


class Field:

    def __init__(self):
        self._cells = {}

    def add(self, x, y):
        cell = Cell(self._cells, x, y)
        self._cells[(x, y)] = cell

    def get(self, coords):
        return self._cells[coords]
