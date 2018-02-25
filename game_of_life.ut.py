import unittest
import numpy as np
from game_of_life import World
from game_of_life import Cell

class TestWorld(unittest.TestCase):

    def test_world_is_created(self):
        w = World(2,2)
        self.assertTrue(np.array_equal(w.world, np.array([[ 0,  0], [ 0,  0]])), "Arrays are not eqeual")

    def test_seed_is_integrated(self):
        w = World(4,4, seed= [[1, 1, 0, 0],
                              [1, 1, 0, 0],
                              [0, 0, 1, 1],
                              [0, 0, 1, 1]])
        self.assertTrue(np.array_equal(w.world, np.array([[1, 1, 0, 0],
                                                            [1, 1, 0, 0],
                                                            [0, 0, 1, 1],
                                                            [0, 0, 1, 1]])), "Arrays are not eqeual")

    
    def test_error_raised_if_seed_doesnt_fit(self):
        with self.assertRaises(ValueError):
            World(4, 4, [[1, 1, 0, 0],
                        [1, 1, 0, 0],
                        [0, 0, 1, 1],
                        [0, 0, 1, 1]], 1, 1)
        with self.assertRaises(ValueError):
            World(4, 4, [[1, 1, 0, 0],
                        [1, 1, 0, 0],
                        [0, 0, 1, 1],
                        [0, 0, 1, 1]], 0, 1) 

    def test_next_iteration_is_valid(self): 
        w = World(4,4, seed= [[1, 1, 0, 0],
                              [1, 1, 0, 0],
                              [0, 0, 1, 1],
                              [0, 0, 1, 1]])
        self.assertTrue(np.array_equal(w.next(), np.array([[1, 1, 0, 0],
                                                           [1, 0, 0, 0],
                                                           [0, 0, 0, 1],
                                                           [0, 0, 1, 1]])), "Next state is ivalid")
        self.assertTrue(np.array_equal(w.next(), np.array([[1, 1, 0, 0],
                                                           [1, 1, 0, 0],
                                                           [0, 0, 1, 1],
                                                           [0, 0, 1, 1]])), "Next state is ivalid")

    def test_beacon_has_a_period_of_two(self): 
        w = World(4,4, seed= [[1, 1, 0, 0],
                              [1, 1, 0, 0],
                              [0, 0, 1, 1],
                              [0, 0, 1, 1]])
        self.assertTrue(np.array_equal(w.let_it_live(2), np.array([[1, 1, 0, 0],
                                                                   [1, 1, 0, 0],
                                                                   [0, 0, 1, 1],
                                                                   [0, 0, 1, 1]])), "Next state is ivalid")

    def test_blinker_has_a_period_of_two(self): 
        blinker = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
        w = World(3, 3, blinker)
        self.assertTrue(np.array_equal(w.let_it_live(2), np.array(blinker)), "Next state is ivalid")

    def test_block_doesnt_change(self): 
        block = [[1, 1], [1, 1]]
        block_with_frame = [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1 ,0], [0, 0, 0, 0]]
        w = World(4, 4, block, 1, 1)
        self.assertTrue(np.array_equal(w.next(), np.array(block_with_frame)), "Block changed")
        self.assertTrue(np.array_equal(w.next(), np.array(block_with_frame)), "Block changed")

    def test_pulsar_has_a_period_of_two(self): 
        pulsar = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        
        w = World(19, 19, pulsar)
        self.assertTrue(np.array_equal(w.let_it_live(3), np.array(pulsar)), "Next state is ivalid")

                                             

class TestCell(unittest.TestCase):

    def test_empty_world_neighbours(self):
        for i in range(4):
            for j in range(4):
                self.assertEqual(0, Cell.get_alive_neighbours_number(i,j, np.zeros((4, 4), dtype=int)), "Wrong neighbours number")

    def test_beacon_world_neighbours(self):
        beacon = np.array([[1, 1, 0, 0],
                           [1, 1, 0, 0],
                           [0, 0, 1, 1],
                           [0, 0, 1, 1]])
        self.assertEqual(3, Cell.get_alive_neighbours_number(0, 0, beacon), "Wrong neighbours number")
        self.assertEqual(4, Cell.get_alive_neighbours_number(1, 1, beacon), "Wrong neighbours number")
        self.assertEqual(2, Cell.get_alive_neighbours_number(2, 0, beacon), "Wrong neighbours number")
        self.assertEqual(2, Cell.get_alive_neighbours_number(3, 1, beacon), "Wrong neighbours number")

    def test_beacon_cells_next_state(self):
        beacon = np.array([[1, 1, 0, 0],
                           [1, 1, 0, 0],
                           [0, 0, 1, 1],
                           [0, 0, 1, 1]])
        self.assertEqual(1, Cell.get_next_state(0, 0, beacon), "Wrong next state")
        self.assertEqual(0, Cell.get_next_state(1, 1, beacon), "Wrong next state")
        self.assertEqual(0, Cell.get_next_state(2, 0, beacon), "Wrong next state")
        self.assertEqual(0, Cell.get_next_state(3, 1, beacon), "Wrong next state")
        self.assertEqual(0, Cell.get_next_state(2, 2, beacon), "Wrong next state")
        self.assertEqual(1, Cell.get_next_state(3, 3, beacon), "Wrong next state")


if __name__ == '__main__':
    unittest.main()