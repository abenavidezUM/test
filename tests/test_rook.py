# test_rook.py

import unittest
from game.rook import Rook
from game.moves import MovePieceInvalid

class TestRook(unittest.TestCase):
    def setUp(self):
        self.rook = Rook("white", (4, 4))
        self.positions = [[None for _ in range(8)] for _ in range(8)]
        self.positions[4][4] = self.rook

    def test_valid_moves(self):
        # Test horizontal and vertical moves
        valid_moves = [
            (4, 0), (4, 7), (0, 4), (7, 4)
        ]
        for move in valid_moves:
            with self.subTest(move=move):
                self.assertTrue(self.rook.check_move(self.positions, move))

    def test_invalid_moves(self):
        # Moves that are not horizontal or vertical
        invalid_moves = [
            (5, 5), (3, 3), (2, 6)
        ]
        for move in invalid_moves:
            with self.subTest(move=move):
                self.assertFalse(self.rook.check_move(self.positions, move))

    def test_blocked_path(self):
        # Place a piece in the path of the rook
        blocking_piece = Rook("white", (4, 6))
        self.positions[4][6] = blocking_piece
        self.assertFalse(self.rook.check_move(self.positions, (4, 7)))

    def test_capture_opponent_piece(self):
        # Place an opponent's piece at the destination
        opponent_piece = Rook("black", (4, 7))
        self.positions[4][7] = opponent_piece
        self.assertTrue(self.rook.check_move(self.positions, (4, 7)))

    def test_blocked_by_friendly_piece_at_destination(self):
        # Place a friendly piece at the destination
        friendly_piece = Rook("white", (4, 7))
        self.positions[4][7] = friendly_piece
        self.assertFalse(self.rook.check_move(self.positions, (4, 7)))

if __name__ == '__main__':
    unittest.main()
