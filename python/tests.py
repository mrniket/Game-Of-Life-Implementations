import unittest
from world import World

class TestWorld(unittest.TestCase):

    def test_populate_with_seed(self):
        seed = [(1,1), (0,3),(1,3), (2,3), (2,2)]
        world = World(5, 5, seed)

        cell = world.cell_at(1, 1)

        self.assertIsNotNone(cell)

    def test_neighbours_around(self):
        seed = [(1,1), (0,3),(1,3), (2,3), (2,2)]
        world = World(5, 5, seed)

        expected = world.neighbours_around(world.cell_at(2, 3))
        actual = [world.cell_at(1,3), world.cell_at(2, 2)]

        self.assertEqual(expected, actual)

    def test_tick(self):
        seed = [(1,1), (0,3),(1,3), (2,3), (2,2)]
        world = World(5, 5, seed)

        world.tick()
        actual = World(5, 5, [(0,2), (2,2), (1,3), (2,3), (1,4)])

        self.assertEqual(world, actual)
