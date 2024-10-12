# test_piece.py

import unittest
from game.piece import Piece
from abc import ABC, abstractmethod

class TestPiece(unittest.TestCase):
    def setUp(self):
        # Create a concrete subclass of Piece for testing
        class TestConcretePiece(Piece):
            def check_move(self, positions, new_position):
                return True

        self.piece = TestConcretePiece("white", (0, 0))

    def test_initialization(self):
        self.assertEqual(self.piece.color, "white")
        self.assertEqual(self.piece.position, (0, 0))

    def test_position_property(self):
        self.piece.position = (1, 1)
        self.assertEqual(self.piece.position, (1, 1))

    def test_str_method(self):
        self.assertEqual(str(self.piece), "?")

    def test_get_coordinates(self):
        new_position = (2, 2)
        new_x, new_y, current_x, current_y = self.piece.get_coordinates(new_position)
        self.assertEqual((new_x, new_y), (2, 2))
        self.assertEqual((current_x, current_y), (0, 0))

    def test_is_in_bounds(self):
        self.assertTrue(self.piece.is_in_bounds(0, 0))
        self.assertTrue(self.piece.is_in_bounds(7, 7))
        self.assertFalse(self.piece.is_in_bounds(-1, 0))
        self.assertFalse(self.piece.is_in_bounds(0, 8))

    def test_abstract_check_move(self):
        # Ensure that calling check_move raises an error in the base class
        with self.assertRaises(TypeError):
            Piece("white", (0, 0))

if __name__ == '__main__':
    unittest.main()
