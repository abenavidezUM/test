# test_board.py

import unittest
from game.board import Board
from game.king import King
from game.queen import Queen
from game.pawn import Pawn
from game.moves import PieceError, MovePieceInvalid, MoveError, KingError

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.white_king = self.board.get_piece(7, 4)
        self.black_king = self.board.get_piece(0, 4)

    def test_initial_setup(self):
        # Ensure that kings are in their correct starting positions
        self.assertIsInstance(self.white_king, King)
        self.assertEqual(self.white_king.color, "white")
        self.assertIsInstance(self.black_king, King)
        self.assertEqual(self.black_king.color, "black")

    def test_move_piece(self):
        # Move a pawn forward
        pawn = self.board.get_piece(6, 4)
        self.board.move(pawn, (4, 4))
        self.assertIs(self.board.get_piece(4, 4), pawn)
        self.assertIsNone(self.board.get_piece(6, 4))
        self.assertEqual(pawn.position, (4, 4))

    def test_move_invalid(self):
        # Attempt an invalid move
        pawn = self.board.get_piece(6, 4)
        with self.assertRaises(MovePieceInvalid):
            self.board.move(pawn, (3, 4))

    def test_capture_opponent_piece(self):
        # Move white pawn to capture black pawn
        white_pawn = self.board.get_piece(6, 0)
        self.board.move(white_pawn, (4, 0))
        black_pawn = self.board.get_piece(1, 1)
        self.board.move(black_pawn, (3, 1))
        self.board.move(white_pawn, (3, 1))
        self.assertIs(self.board.get_piece(3, 1), white_pawn)
        self.assertIsNone(self.board.get_piece(1, 1))
        self.assertEqual(white_pawn.position, (3, 1))

    def test_capture_own_piece(self):
        # Attempt to capture own piece
        pawn = self.board.get_piece(6, 0)
        with self.assertRaises(MoveError):
            self.board.move(pawn, (7, 0))

    def test_capture_king(self):
        # Attempt to capture opponent's king
        queen = self.board.get_piece(7, 3)
        self.board.set_piece_on_board(1, 4, None)  # Remove pawn blocking the king
        self.board.set_piece_on_board(2, 4, None)
        self.board.set_piece_on_board(3, 4, None)
        self.board.set_piece_on_board(4, 4, None)
        self.board.set_piece_on_board(5, 4, None)
        self.board.set_piece_on_board(6, 4, None)
        self.board.move(queen, (0, 4))
        with self.assertRaises(KingError):
            self.board.validate_move(queen, (0, 4))

if __name__ == '__main__':
    unittest.main()
