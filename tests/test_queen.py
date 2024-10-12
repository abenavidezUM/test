# test_queen.py

import unittest
from game.queen import Queen
from game.piece import Piece, WHITE, BLACK
from abc import ABC, abstractmethod

# Crear una clase MockPiece para usar en las pruebas
class MockPiece(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def check_move(self, positions, new_position):
        # Implementación dummy, ya que no se utiliza en estas pruebas
        pass

class TestQueen(unittest.TestCase):
    def setUp(self):
        # Inicializa una reina blanca en la posición (3, 3)
        self.white_queen = Queen(WHITE, (3, 3))
        # Inicializa una reina negra en la posición (0, 0)
        self.black_queen = Queen(BLACK, (0, 0))

    def test_initialization(self):
        # Prueba la inicialización de la reina blanca
        self.assertEqual(self.white_queen.color, WHITE)
        self.assertEqual(self.white_queen.position, (3, 3))

        # Prueba la inicialización de la reina negra
        self.assertEqual(self.black_queen.color, BLACK)
        self.assertEqual(self.black_queen.position, (0, 0))

    def test_str_representation(self):
        # Prueba la representación en cadena de la reina blanca
        self.assertEqual(str(self.white_queen), "♕")

        # Prueba la representación en cadena de la reina negra
        self.assertEqual(str(self.black_queen), "♛")

    def test_check_move_valid_diagonal(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]

        # Define movimientos diagonales válidos para la reina blanca desde (3, 3)
        valid_diagonal_moves = [
            (4, 4), (5, 5), (2, 2), (1, 1),
            (4, 2), (5, 1), (2, 4), (1, 5)
        ]

        for move in valid_diagonal_moves:
            with self.subTest(move=move):
                self.assertTrue(self.white_queen.check_move(board, move))

    def test_check_move_valid_horizontal_vertical(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]

        # Define movimientos horizontales y verticales válidos para la reina blanca desde (3, 3)
        valid_linear_moves = [
            (3, 0), (3, 7),  # Horizontales
            (0, 3), (7, 3),  # Verticales
            (3, 4), (3, 2), (3, 5), (3, 1),  # Horizontales adicionales
            (4, 3), (2, 3), (5, 3), (1, 3)   # Verticales adicionales
        ]

        for move in valid_linear_moves:
            with self.subTest(move=move):
                self.assertTrue(self.white_queen.check_move(board, move))

    def test_check_move_invalid_not_straight_or_diagonal(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]

        # Define movimientos inválidos que no son ni diagonales ni lineales
        truly_invalid_moves = [
            (4, 5), (5, 6), (2, 5), (1, 6),
            (5, 2), (2, 4), (4, 1), (1, 5)
        ]

        for move in truly_invalid_moves:
            with self.subTest(move=move):
                self.assertFalse(self.white_queen.check_move(board, move))

    def test_check_move_capture_opposite_color(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        # Coloca una pieza enemiga en una posición diagonal válida
        board[4][4] = MockPiece(BLACK, (4, 4))
        # Coloca una pieza enemiga en una posición horizontal válida
        board[3][5] = MockPiece(BLACK, (3, 5))
        # Coloca una pieza enemiga en una posición vertical válida
        board[3][0] = MockPiece(BLACK, (3, 0))

        # La reina blanca intenta capturar en (4, 4), (3, 5) y (3, 0)
        self.assertTrue(self.white_queen.check_move(board, (4, 4)))
        self.assertTrue(self.white_queen.check_move(board, (3, 5)))
        self.assertTrue(self.white_queen.check_move(board, (3, 0)))

    def test_check_move_capture_same_color(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        # Coloca una pieza amiga en una posición diagonal válida
        board[4][4] = MockPiece(WHITE, (4, 4))
        # Coloca una pieza amiga en una posición horizontal válida
        board[3][5] = MockPiece(WHITE, (3, 5))
        # Coloca una pieza amiga en una posición vertical válida
        board[3][0] = MockPiece(WHITE, (3, 0))

        # La reina blanca intenta capturar en (4, 4), (3, 5) y (3, 0) donde hay piezas amigas
        self.assertFalse(self.white_queen.check_move(board, (4, 4)))
        self.assertFalse(self.white_queen.check_move(board, (3, 5)))
        self.assertFalse(self.white_queen.check_move(board, (3, 0)))

    def test_check_move_blocked_path_diagonal(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        # Coloca una pieza amiga en el camino diagonal
        board[4][4] = MockPiece(WHITE, (4, 4))

        # La reina blanca intenta moverse a (5, 5), pero el camino está bloqueado en (4,4)
        self.assertFalse(self.white_queen.check_move(board, (5, 5)))

    def test_check_move_blocked_path_horizontal(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        # Coloca una pieza amiga en el camino horizontal
        board[3][4] = MockPiece(WHITE, (3, 4))

        # La reina blanca intenta moverse a (3, 5), pero el camino está bloqueado en (3,4)
        self.assertFalse(self.white_queen.check_move(board, (3, 5)))

    def test_check_move_blocked_path_vertical(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        # Coloca una pieza amiga en el camino vertical
        board[2][3] = MockPiece(WHITE, (2, 3))

        # La reina blanca intenta moverse a (1, 3), pero el camino está bloqueado en (2,3)
        self.assertFalse(self.white_queen.check_move(board, (1, 3)))

    def test_check_move_out_of_bounds(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]

        # Define movimientos fuera del tablero
        out_of_bounds_moves = [
            (-1, -1), (8, 8), (3, 8), (8, 3), (-1, 3), (3, -1)
        ]

        for move in out_of_bounds_moves:
            with self.subTest(move=move):
                self.assertFalse(self.white_queen.check_move(board, move))

    def test_check_move_no_change_position(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]

        # La reina intenta moverse a su posición actual
        self.assertFalse(self.white_queen.check_move(board, (3, 3)))

if __name__ == '__main__':
    unittest.main()
