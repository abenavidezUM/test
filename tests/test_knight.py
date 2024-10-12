# test_knight.py

import unittest
from game.knight import Knight
from game.moves import MovePieceInvalid

class TestKnight(unittest.TestCase):
    def setUp(self):
        self.knight = Knight("white", (4, 4))
        self.positions = [[None for _ in range(8)] for _ in range(8)]
        self.positions[4][4] = self.knight

    def test_valid_moves(self):
        # Test all possible L-shaped moves
        valid_moves = [
            (6, 5), (6, 3), (2, 5), (2, 3),
            (5, 6), (5, 2), (3, 6), (3, 2)
        ]
        for move in valid_moves:
            with self.subTest(move=move):
                self.assertTrue(self.knight.check_move(self.positions, move))

    def test_invalid_moves(self):
        # Moves that are not L-shaped
        invalid_moves = [
            (4, 5), (5, 5), (4, 2), (2, 4)
        ]
        for move in invalid_moves:
            with self.subTest(move=move):
                self.assertFalse(self.knight.check_move(self.positions, move))

    def test_capture_opponent_piece(self):
        # Place an opponent's piece at a valid destination
        opponent_piece = Knight("black", (6, 5))
        self.positions[6][5] = opponent_piece
        self.assertTrue(self.knight.check_move(self.positions, (6, 5)))

    def test_blocked_by_friendly_piece_at_destination(self):
        # Place a friendly piece at a valid destination
        friendly_piece = Knight("white", (6, 5))
        self.positions[6][5] = friendly_piece
        self.assertFalse(self.knight.check_move(self.positions, (6, 5)))

if __name__ == '__main__':
    unittest.main()
