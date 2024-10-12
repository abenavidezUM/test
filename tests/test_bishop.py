# test_bishop.py

import unittest
from game.bishop import Bishop
from game.moves import MovePieceInvalid

class TestBishop(unittest.TestCase):
    def setUp(self):
        self.bishop = Bishop("white", (4, 4))
        self.positions = [[None for _ in range(8)] for _ in range(8)]
        self.positions[4][4] = self.bishop

    def test_valid_moves(self):
        # Test diagonal moves
        valid_moves = [
            (0, 0), (7, 7), (1, 7), (7, 1)
        ]
        for move in valid_moves:
            with self.subTest(move=move):
                self.assertTrue(self.bishop.check_move(self.positions, move))

    def test_invalid_moves(self):
        # Moves that are not diagonal
        invalid_moves = [
            (4, 5), (5, 4), (4, 0), (0, 4)
        ]
        for move in invalid_moves:
            with self.subTest(move=move):
                self.assertFalse(self.bishop.check_move(self.positions, move))

    def test_blocked_path(self):
        # Place a piece in the path of the bishop
        blocking_piece = Bishop("white", (5, 5))
        self.positions[5][5] = blocking_piece
        self.assertFalse(self.bishop.check_move(self.positions, (7, 7)))

    def test_capture_opponent_piece(self):
        # Place an opponent's piece at the destination
        opponent_piece = Bishop("black", (7, 7))
        self.positions[7][7] = opponent_piece
        self.assertTrue(self.bishop.check_move(self.positions, (7, 7)))

    def test_blocked_by_friendly_piece_at_destination(self):
        # Place a friendly piece at the destination
        friendly_piece = Bishop("white", (7, 7))
        self.positions[7][7] = friendly_piece
        self.assertFalse(self.bishop.check_move(self.positions, (7, 7)))

if __name__ == '__main__':
    unittest.main()
