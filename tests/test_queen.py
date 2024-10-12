# test_queen.py

import unittest
from game.queen import Queen
from game.moves import MovePieceInvalid

class TestQueen(unittest.TestCase):
    def setUp(self):
        self.queen = Queen("white", (4, 4))
        self.positions = [[None for _ in range(8)] for _ in range(8)]
        self.positions[4][4] = self.queen

    def test_valid_moves(self):
        # Test horizontal, vertical, and diagonal moves
        valid_moves = [
            # Horizontal and vertical
            (4, 0), (4, 7), (0, 4), (7, 4),
            # Diagonals
            (0, 0), (7, 7), (1, 7), (7, 1)
        ]
        for move in valid_moves:
            with self.subTest(move=move):
                self.assertTrue(self.queen.check_move(self.positions, move))

    def test_invalid_moves(self):
        # Moves that are not in straight lines or diagonals
        invalid_moves = [
            (5, 6), (2, 5), (3, 6)
        ]
        for move in invalid_moves:
            with self.subTest(move=move):
                self.assertFalse(self.queen.check_move(self.positions, move))

    def test_blocked_path(self):
        # Place a piece in the path of the queen
        blocking_piece = Queen("white", (4, 6))
        self.positions[4][6] = blocking_piece
        self.assertFalse(self.queen.check_move(self.positions, (4, 7)))

    def test_capture_opponent_piece(self):
        # Place an opponent's piece at the destination
        opponent_piece = Queen("black", (4, 6))
        self.positions[4][6] = opponent_piece
        self.assertTrue(self.queen.check_move(self.positions, (4, 6)))

    def test_blocked_by_friendly_piece_at_destination(self):
        # Place a friendly piece at the destination
        friendly_piece = Queen("white", (4, 6))
        self.positions[4][6] = friendly_piece
        self.assertFalse(self.queen.check_move(self.positions, (4, 6)))

if __name__ == '__main__':
    unittest.main()
