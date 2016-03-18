import unittest
from game_of_life import *


class test_game_of_life(unittest.TestCase):

    def test_next_generation_of_empty_pattern_is_empty(self):
        self.assertEquals(next([]),[])

    def test_single_cell_dies(self):
        self.assertEquals(next([0,0]),[])

    def test_2_neighbours_lives(self):
        pattern=[(-1,0),(0,0),(1,0)]
        self.assertEquals(next(pattern),(0,0))
    def test_4_neighbours_dies(self):
        pattern=[(-1,-1),     (1,-1),
                        (0,0),
                 (1,-1),      (1,1)]
        self.assertEquals(next(pattern),[])

    def test_counts_live_neighbours_in_cell(self):
        pattern=[(-1,-1),     (1,-1),
                        (0,0),
                 (-1,1),      (1,1)]
        self.assertEquals(living_neighbours(pattern,(0,0)),4)

