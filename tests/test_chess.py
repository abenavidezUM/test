# test_chess.py

import unittest
from game.chess import Chess
from game.moves import PieceError, MovePieceInvalid, PositionInvalid, LocationError

class TestChess(unittest.TestCase):
    def setUp(self):
        self.game = Chess()

    def test_initial_turn(self):
        self.assertEqual(self.game.turn, "WHITE")

    def test_change_turn(self):
        self.game.change_turn()
        self.assertEqual(self.game.turn, "BLACK")

    def test_valid_move(self):
        result = self.game.move('E2', 'E4')
        self.assertTrue(result)
        self.assertEqual(self.game.turn, "BLACK")

    def test_invalid_move(self):
        with self.assertRaises(MovePieceInvalid):
            self.game.move('E2', 'E5')

    def test_move_wrong_turn(self):
        with self.assertRaises(LocationError):
            self.game.move('E7', 'E5')

    def test_translate_input(self):
        self.assertEqual(self.game.translate_input('A1'), (0, 0))
        self.assertEqual(self.game.translate_input('H8'), (7, 7))

    def test_invalid_input(self):
        with self.assertRaises(PositionInvalid):
            self.game.translate_input('I1')
        with self.assertRaises(ValueError):
            self.game.translate_input('A')

    def test_victory_condition(self):
        # Simulate removing all black pieces
        self.game.board.clean_board()
        self.game.board.set_piece_on_board(0, 0, self.game.board.get_piece(7, 4))  # Place white king
        result = self.game.check_victory()
        self.assertEqual(result, "White wins")

if __name__ == '__main__':
    unittest.main()
