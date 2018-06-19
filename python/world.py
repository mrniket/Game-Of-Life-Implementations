from random import randint
from cell import Cell

class World:

    class LocationOccupied(RuntimeError): pass

    def __init__(self, width, height, seed=[]):
        self.width = width
        self.height = height
        self.tick_count = 0
        self.cells = {}  # dict {string: Cell}

        self.populate_cells(seed)
        self.prepopulate_neighbours()

    def neighbours_around(self, cell):
        """
        Find all the neighbours of cell.
        Append to cell.neighbours and return it
        """
        pass

    def determine_actions(self):
        """
        Decide the fate of the cells on the next tick, as per the rules
        Store the result in cell.next_state
        """

        pass

    def execute_actions(self):
        """
        Apply the actions for the next tick using cell.next_state
        """
        pass

    def tick(self):
        self.determine_actions()
        self.execute_actions()
        self.tick_count += 1

    def render(self):
        rendering = ''
        for y in list(range(self.height)):
            for x in list(range(self.width)):
                cell = self.cell_at(x, y)
                rendering += cell.to_char()
            rendering += "\n"
        return rendering

    def populate_cells(self, seed):
        if seed:
            self.populate_cells_with_seed(seed)
        else:
            for y in list(range(self.height)):
                for x in list(range(self.width)):
                    alive = (randint(0, 100) <= 20)
                    self.add_cell(x, y, alive)

    def populate_cells_with_seed(self, seed):
        for x, y in seed:
            if x < self.width and y < self.height:
                cell = self.add_cell(x, y)
                cell.alive = True

    def prepopulate_neighbours(self):
        for key,cell in self.cells.items():
            self.neighbours_around(cell)

    def add_cell(self, x, y, alive = False):
        if self.cell_at(x, y) != None:
            raise World.LocationOccupied

        cell = Cell(x, y, alive)
        self.cells[str(x)+'-'+str(y)] = cell
        return self.cell_at(x, y)

    def cell_at(self, x, y):
        return self.cells.get(str(x)+'-'+str(y))

    def alive_neighbours_around(self, cell):
        alive_neighbours = 0
        for neighbour in self.neighbours_around(cell):
            if neighbour.alive:
                alive_neighbours += 1
        return alive_neighbours

    def __eq__(self, other):
        if isinstance(other, World):
            for key, cell in self.cells.items():
                other_cell = other.cells.get(key)
                if not cell == other_cell:
                    return False
            return True
        return False
