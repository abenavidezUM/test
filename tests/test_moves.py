# test_moves.py

import unittest
from game.moves import (
    ChessInvalid, PieceError, PositionInvalid, LocationError,
    MoveError, MovePieceInvalid, KingError
)

class TestMoves(unittest.TestCase):
    def test_chess_invalid_exception(self):
        with self.assertRaises(ChessInvalid) as context:
            raise ChessInvalid("Custom error message.")
        self.assertEqual(str(context.exception), "Custom error message.")

    def test_piece_error_exception(self):
        with self.assertRaises(PieceError):
            raise PieceError("Piece not found.")

    def test_position_invalid_exception(self):
        with self.assertRaises(PositionInvalid):
            raise PositionInvalid("Invalid position.")

    def test_location_error_exception(self):
        with self.assertRaises(LocationError):
            raise LocationError("Cannot move a piece of a different color.")

    def test_move_error_exception(self):
        with self.assertRaises(MoveError):
            raise MoveError("Invalid move.")

    def test_move_piece_invalid_exception(self):
        with self.assertRaises(MovePieceInvalid):
            raise MovePieceInvalid("Invalid piece movement.")

    def test_king_error_exception(self):
        with self.assertRaises(KingError):
            raise KingError("You can't capture the opponent's king.")

if __name__ == '__main__':
    unittest.main()
