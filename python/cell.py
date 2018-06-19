class Cell:

    def __init__(self, x, y, alive=False):
        self.x = x
        self.y = y
        self.alive = alive
        self.next_state = None
        # This will be an array
        self.neighbours = None

    def to_char(self):
        return 'o' if self.alive else ' '

    def __eq__(self, other):
        if isinstance(other, Cell):
            return self.x == other.x and self.y == other.y and self.alive == other.alive
        return False

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")" + " Alive: " + str(self.alive)
