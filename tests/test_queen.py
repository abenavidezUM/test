# test_queen.py

import unittest
from queen import Queen
from piece import Piece, WHITE, BLACK

class TestQueen(unittest.TestCase):
    def setUp(self):
        """
        Configuración inicial para cada prueba.
        Crea un tablero vacío y coloca una reina en una posición específica.
        """
        # Crear un tablero 8x8 lleno de None
        self.board = [[None for _ in range(8)] for _ in range(8)]
        
        # Inicializar una reina blanca en la posición (3, 3)
        self.queen = Queen(color=WHITE, position=(3, 3))
        self.board[3][3] = self.queen

    def test_initialization(self):
        """
        Verifica que la reina se inicializa correctamente.
        """
        self.assertEqual(self.queen.color, WHITE)
        self.assertEqual(self.queen.position, (3, 3))
        self.assertEqual(str(self.queen), "♕")

    def test_valid_horizontal_move(self):
        """
        Verifica un movimiento horizontal válido.
        """
        new_position = (3, 6)  # Mover de (3,3) a (3,6)
        result = self.queen.check_move(self.board, new_position)
        self.assertTrue(result)

    def test_valid_vertical_move(self):
        """
        Verifica un movimiento vertical válido.
        """
        new_position = (6, 3)  # Mover de (3,3) a (6,3)
        result = self.queen.check_move(self.board, new_position)
        self.assertTrue(result)

    def test_valid_diagonal_move(self):
        """
        Verifica un movimiento diagonal válido.
        """
        new_position = (6, 6)  # Mover de (3,3) a (6,6)
        result = self.queen.check_move(self.board, new_position)
        self.assertTrue(result)

    def test_invalid_move_same_position(self):
        """
        Verifica que mover la reina a su misma posición es inválido.
        """
        new_position = (3, 3)  # Mismo lugar
        result = self.queen.check_move(self.board, new_position)
        self.assertFalse(result)

    def test_invalid_move_out_of_bounds(self):
        """
        Verifica que mover la reina fuera de los límites del tablero es inválido.
        """
        new_position = (8, 8)  # Fuera del tablero
        result = self.queen.check_move(self.board, new_position)
        self.assertFalse(result)

    def test_invalid_move_capture_own_piece(self):
        """
        Verifica que la reina no pueda capturar una pieza del mismo color.
        """
        # Colocar una pieza propia en la nueva posición
        own_piece = Queen(color=WHITE, position=(3, 6))
        self.board[3][6] = own_piece

        new_position = (3, 6)  # Intentar mover a (3,6) donde hay una pieza propia
        result = self.queen.check_move(self.board, new_position)
        self.assertFalse(result)

    def test_invalid_move_path_blocked_horizontal(self):
        """
        Verifica que la reina no pueda mover horizontalmente si el camino está bloqueado.
        """
        # Colocar una pieza en el camino horizontal
        blocking_piece = Piece(color=BLACK, position=(3, 4))
        self.board[3][4] = blocking_piece

        new_position = (3, 6)  # Intentar mover a (3,6) pasando por (3,4) y (3,5)
        result = self.queen.check_move(self.board, new_position)
        self.assertFalse(result)

    def test_invalid_move_path_blocked_diagonal(self):
        """
        Verifica que la reina no pueda mover diagonalmente si el camino está bloqueado.
        """
        # Colocar una pieza en el camino diagonal
        blocking_piece = Piece(color=BLACK, position=(4, 4))
        self.board[4][4] = blocking_piece

        new_position = (6, 6)  # Intentar mover a (6,6) pasando por (4,4) y (5,5)
        result = self.queen.check_move(self.board, new_position)
        self.assertFalse(result)

    def test_valid_move_capture_enemy_piece(self):
        """
        Verifica que la reina pueda capturar una pieza enemiga.
        """
        # Colocar una pieza enemiga en la nueva posición
        enemy_piece = Piece(color=BLACK, position=(3, 6))
        self.board[3][6] = enemy_piece

        new_position = (3, 6)  # Intentar mover a (3,6) donde hay una pieza enemiga
        result = self.queen.check_move(self.board, new_position)
        self.assertTrue(result)

    def test_invalid_move_not_straight_or_diagonal(self):
        """
        Verifica que la reina no pueda mover de una manera que no sea horizontal, vertical o diagonal.
        """
        new_position = (5, 4)  # Movimiento no permitido (ejemplo: en L como la torre)
        result = self.queen.check_move(self.board, new_position)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
