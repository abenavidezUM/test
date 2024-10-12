# test_king.py

import unittest
from game.king import King
from game.moves import MovePieceInvalid

class TestKing(unittest.TestCase):
    def setUp(self):
        self.king = King("white", (4, 4))
        self.positions = [[None for _ in range(8)] for _ in range(8)]
        self.positions[4][4] = self.king

    def test_valid_moves(self):
        # Test all valid moves around the king
        valid_moves = [
            (3, 3), (3, 4), (3, 5),
            (4, 3),         (4, 5),
            (5, 3), (5, 4), (5, 5)
        ]
        for move in valid_moves:
            with self.subTest(move=move):
                self.assertTrue(self.king.check_move(self.positions, move))

    def test_invalid_moves(self):
        # Moves more than one square away
        invalid_moves = [
            (2, 4), (4, 2), (6, 4), (4, 6)
        ]
        for move in invalid_moves:
            with self.subTest(move=move):
                self.assertFalse(self.king.check_move(self.positions, move))

    def test_capture_opponent_piece(self):
        # Place an opponent's piece adjacent to the king
        opponent_piece = King("black", (3, 4))
        self.positions[3][4] = opponent_piece
        self.assertTrue(self.king.check_move(self.positions, (3, 4)))

    def test_blocked_by_friendly_piece(self):
        # Place a friendly piece adjacent to the king
        friendly_piece = King("white", (3, 4))
        self.positions[3][4] = friendly_piece
        self.assertFalse(self.king.check_move(self.positions, (3, 4)))

if __name__ == '__main__':
    unittest.main()
