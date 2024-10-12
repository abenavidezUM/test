# test_queen.py

import unittest
from game.piece import WHITE, BLACK
from game.queen import Queen

class MockPiece:
    """
    Mock class para simular otras piezas en el tablero.
    """
    def __init__(self, color):
        self.__color__ = color

    @property
    def color(self):
        return self.__color__

class TestQueen(unittest.TestCase):
    def setUp(self):
        """
        Configuración inicial antes de cada prueba.
        """
        # Crear un tablero vacío 8x8
        self.empty_board = [[None for _ in range(8)] for _ in range(8)]
        
        # Crear una instancia de Queen blanca en la posición central (3, 3)
        self.queen_white = Queen(WHITE, (3, 3))
        self.empty_board[3][3] = self.queen_white
        
        # Crear una instancia de Queen negra en la posición central (4, 4)
        self.queen_black = Queen(BLACK, (4, 4))
        self.empty_board[4][4] = self.queen_black

    # ### Pruebas para la Reina Blanca ###

    def test_white_queen_valid_diagonal_move(self):
        """
        Prueba un movimiento diagonal válido sin obstáculos para la reina blanca.
        """
        new_position = (5, 5)  # Movimiento diagonal hacia arriba a la derecha
        result = self.queen_white.check_move(self.empty_board, new_position)
        self.assertTrue(result, "La reina blanca debería poder moverse diagonalmente sin obstáculos.")

    def test_white_queen_valid_horizontal_move(self):
        """
        Prueba un movimiento horizontal válido sin obstáculos para la reina blanca.
        """
        new_position = (3, 7)  # Movimiento horizontal hacia la derecha
        result = self.queen_white.check_move(self.empty_board, new_position)
        self.assertTrue(result, "La reina blanca debería poder moverse horizontalmente sin obstáculos.")

    def test_white_queen_valid_vertical_move(self):
        """
        Prueba un movimiento vertical válido sin obstáculos para la reina blanca.
        """
        new_position = (0, 3)  # Movimiento vertical hacia arriba
        result = self.queen_white.check_move(self.empty_board, new_position)
        self.assertTrue(result, "La reina blanca debería poder moverse verticalmente sin obstáculos.")

    def test_white_queen_invalid_non_linear_move(self):
        """
        Prueba un movimiento que no es ni diagonal ni lineal para la reina blanca.
        """
        new_position = (5, 4)  # Movimiento no válido
        result = self.queen_white.check_move(self.empty_board, new_position)
        self.assertFalse(result, "La reina blanca no debería poder moverse de manera no diagonal ni lineal.")

    def test_white_queen_move_out_of_bounds(self):
        """
        Prueba un movimiento que sale de los límites del tablero para la reina blanca.
        """
        new_position = (8, 8)  # Fuera de los límites
        result = self.queen_white.check_move(self.empty_board, new_position)
        self.assertFalse(result, "La reina blanca no debería poder moverse fuera de los límites del tablero.")

    def test_white_queen_move_to_same_position(self):
        """
        Prueba intentar mover la reina blanca a su posición actual.
        """
        new_position = (3, 3)  # Misma posición
        result = self.queen_white.check_move(self.empty_board, new_position)
        self.assertFalse(result, "La reina blanca no debería poder moverse a su posición actual.")

    def test_white_queen_capture_enemy_piece_diagonal(self):
        """
        Prueba que la reina blanca puede capturar una pieza enemiga en una posición diagonal.
        """
        enemy_piece = MockPiece(BLACK)
        self.empty_board[5][5] = enemy_piece  # Posición diagonal válida
        
        new_position = (5, 5)
        result = self.queen_white.check_move(self.empty_board, new_position)
        self.assertTrue(result, "La reina blanca debería poder capturar una pieza enemiga en diagonal.")

    def test_white_queen_capture_enemy_piece_horizontal(self):
        """
        Prueba que la reina blanca puede capturar una pieza enemiga en una posición horizontal.
        """
        enemy_piece = MockPiece(BLACK)
        self.empty_board[3][7] = enemy_piece  # Posición horizontal válida
        
        new_position = (3, 7)
        result = self.queen_white.check_move(self.empty_board, new_position)
        self.assertTrue(result, "La reina blanca debería poder capturar una pieza enemiga en horizontal.")

    def test_white_queen_capture_enemy_piece_vertical(self):
        """
        Prueba que la reina blanca puede capturar una pieza enemiga en una posición vertical.
        """
        enemy_piece = MockPiece(BLACK)
        self.empty_board[0][3] = enemy_piece  # Posición vertical válida
        
        new_position = (0, 3)
        result = self.queen_white.check_move(self.empty_board, new_position)
        self.assertTrue(result, "La reina blanca debería poder capturar una pieza enemiga en vertical.")

    def test_white_queen_capture_friendly_piece_diagonal(self):
        """
        Prueba que la reina blanca no puede capturar una pieza amiga en una posición diagonal.
        """
        friendly_piece = MockPiece(WHITE)
        self.empty_board[5][5] = friendly_piece  # Posición diagonal con pieza amiga
        
        new_position = (5, 5)
        result = self.queen_white.check_move(self.empty_board, new_position)
        self.assertFalse(result, "La reina blanca no debería poder capturar una pieza amiga en diagonal.")

    def test_white_queen_capture_friendly_piece_horizontal(self):
        """
        Prueba que la reina blanca no puede capturar una pieza amiga en una posición horizontal.
        """
        friendly_piece = MockPiece(WHITE)
        self.empty_board[3][7] = friendly_piece  # Posición horizontal con pieza amiga
        
        new_position = (3, 7)
        result = self.queen_white.check_move(self.empty_board, new_position)
        self.assertFalse(result, "La reina blanca no debería poder capturar una pieza amiga en horizontal.")

    def test_white_queen_capture_friendly_piece_vertical(self):
        """
        Prueba que la reina blanca no puede capturar una pieza amiga en una posición vertical.
        """
        friendly_piece = MockPiece(WHITE)
        self.empty_board[0][3] = friendly_piece  # Posición vertical con pieza amiga
        
        new_position = (0, 3)
        result = self.queen_white.check_move(self.empty_board, new_position)
        self.assertFalse(result, "La reina blanca no debería poder capturar una pieza amiga en vertical.")

    def test_white_queen_blocked_diagonal_path(self):
        """
        Prueba que la reina blanca no puede moverse diagonalmente si el camino está bloqueado por una pieza.
        """
        blocking_piece = MockPiece(WHITE)
        self.empty_board[4][4] = blocking_piece  # Bloquea el camino hacia (5,5)
        
        new_position = (5, 5)
        result = self.queen_white.check_move(self.empty_board, new_position)
        self.assertFalse(result, "La reina blanca no debería poder moverse diagonalmente si el camino está bloqueado.")

    def test_white_queen_blocked_horizontal_path(self):
        """
        Prueba que la reina blanca no puede moverse horizontalmente si el camino está bloqueado por una pieza.
        """
        blocking_piece = MockPiece(BLACK)
        self.empty_board[3][5] = blocking_piece  # Bloquea el camino hacia (3,7)
        
        new_position = (3, 7)
        result = self.queen_white.check_move(self.empty_board, new_position)
        self.assertFalse(result, "La reina blanca no debería poder moverse horizontalmente si el camino está bloqueado.")

    def test_white_queen_blocked_vertical_path(self):
        """
        Prueba que la reina blanca no puede moverse verticalmente si el camino está bloqueado por una pieza.
        """
        blocking_piece = MockPiece(WHITE)
        self.empty_board[2][3] = blocking_piece  # Bloquea el camino hacia (0,3)
        
        new_position = (0, 3)
        result = self.queen_white.check_move(self.empty_board, new_position)
        self.assertFalse(result, "La reina blanca no debería poder moverse verticalmente si el camino está bloqueado.")

    # ### Pruebas para la Reina Negra ###

    def test_black_queen_valid_diagonal_move(self):
        """
        Prueba un movimiento diagonal válido sin obstáculos para la reina negra.
        """
        new_position = (2, 2)  # Movimiento diagonal hacia abajo a la izquierda
        result = self.queen_black.check_move(self.empty_board, new_position)
        self.assertTrue(result, "La reina negra debería poder moverse diagonalmente sin obstáculos.")

    def test_black_queen_valid_horizontal_move(self):
        """
        Prueba un movimiento horizontal válido sin obstáculos para la reina negra.
        """
        new_position = (4, 0)  # Movimiento horizontal hacia la izquierda
        result = self.queen_black.check_move(self.empty_board, new_position)
        self.assertTrue(result, "La reina negra debería poder moverse horizontalmente sin obstáculos.")

    def test_black_queen_valid_vertical_move(self):
        """
        Prueba un movimiento vertical válido sin obstáculos para la reina negra.
        """
        new_position = (7, 4)  # Movimiento vertical hacia abajo
        result = self.queen_black.check_move(self.empty_board, new_position)
        self.assertTrue(result, "La reina negra debería poder moverse verticalmente sin obstáculos.")

    def test_black_queen_invalid_non_linear_move(self):
        """
        Prueba un movimiento que no es ni diagonal ni lineal para la reina negra.
        """
        new_position = (5, 6)  # Movimiento no válido
        result = self.queen_black.check_move(self.empty_board, new_position)
        self.assertFalse(result, "La reina negra no debería poder moverse de manera no diagonal ni lineal.")

    def test_black_queen_move_out_of_bounds(self):
        """
        Prueba un movimiento que sale de los límites del tablero para la reina negra.
        """
        new_position = (9, 9)  # Fuera de los límites
        result = self.queen_black.check_move(self.empty_board, new_position)
        self.assertFalse(result, "La reina negra no debería poder moverse fuera de los límites del tablero.")

    def test_black_queen_move_to_same_position(self):
        """
        Prueba intentar mover la reina negra a su posición actual.
        """
        new_position = (4, 4)  # Misma posición
        result = self.queen_black.check_move(self.empty_board, new_position)
        self.assertFalse(result, "La reina negra no debería poder moverse a su posición actual.")

    def test_black_queen_capture_enemy_piece_diagonal(self):
        """
        Prueba que la reina negra puede capturar una pieza enemiga en una posición diagonal.
        """
        enemy_piece = MockPiece(WHITE)
        self.empty_board[2][2] = enemy_piece  # Posición diagonal válida
        
        new_position = (2, 2)
        result = self.queen_black.check_move(self.empty_board, new_position)
        self.assertTrue(result, "La reina negra debería poder capturar una pieza enemiga en diagonal.")

    def test_black_queen_capture_enemy_piece_horizontal(self):
        """
        Prueba que la reina negra puede capturar una pieza enemiga en una posición horizontal.
        """
        enemy_piece = MockPiece(WHITE)
        self.empty_board[4][0] = enemy_piece  # Posición horizontal válida
        
        new_position = (4, 0)
        result = self.queen_black.check_move(self.empty_board, new_position)
        self.assertTrue(result, "La reina negra debería poder capturar una pieza enemiga en horizontal.")

    def test_black_queen_capture_enemy_piece_vertical(self):
        """
        Prueba que la reina negra puede capturar una pieza enemiga en una posición vertical.
        """
        enemy_piece = MockPiece(WHITE)
        self.empty_board[7][4] = enemy_piece  # Posición vertical válida
        
        new_position = (7, 4)
        result = self.queen_black.check_move(self.empty_board, new_position)
        self.assertTrue(result, "La reina negra debería poder capturar una pieza enemiga en vertical.")

    def test_black_queen_capture_friendly_piece_diagonal(self):
        """
        Prueba que la reina negra no puede capturar una pieza amiga en una posición diagonal.
        """
        friendly_piece = MockPiece(BLACK)
        self.empty_board[2][2] = friendly_piece  # Posición diagonal con pieza amiga
        
        new_position = (2, 2)
        result = self.queen_black.check_move(self.empty_board, new_position)
        self.assertFalse(result, "La reina negra no debería poder capturar una pieza amiga en diagonal.")

    def test_black_queen_capture_friendly_piece_horizontal(self):
        """
        Prueba que la reina negra no puede capturar una pieza amiga en una posición horizontal.
        """
        friendly_piece = MockPiece(BLACK)
        self.empty_board[4][0] = friendly_piece  # Posición horizontal con pieza amiga
        
        new_position = (4, 0)
        result = self.queen_black.check_move(self.empty_board, new_position)
        self.assertFalse(result, "La reina negra no debería poder capturar una pieza amiga en horizontal.")

    def test_black_queen_capture_friendly_piece_vertical(self):
        """
        Prueba que la reina negra no puede capturar una pieza amiga en una posición vertical.
        """
        friendly_piece = MockPiece(BLACK)
        self.empty_board[7][4] = friendly_piece  # Posición vertical con pieza amiga
        
        new_position = (7, 4)
        result = self.queen_black.check_move(self.empty_board, new_position)
        self.assertFalse(result, "La reina negra no debería poder capturar una pieza amiga en vertical.")

    def test_black_queen_blocked_diagonal_path(self):
        """
        Prueba que la reina negra no puede moverse diagonalmente si el camino está bloqueado por una pieza.
        """
        blocking_piece = MockPiece(WHITE)
        self.empty_board[3][3] = blocking_piece  # Bloquea el camino hacia (2,2)
        
        new_position = (2, 2)
        result = self.queen_black.check_move(self.empty_board, new_position)
        self.assertFalse(result, "La reina negra no debería poder moverse diagonalmente si el camino está bloqueado.")

    def test_black_queen_blocked_horizontal_path(self):
        """
        Prueba que la reina negra no puede moverse horizontalmente si el camino está bloqueado por una pieza.
        """
        blocking_piece = MockPiece(BLACK)
        self.empty_board[4][2] = blocking_piece  # Bloquea el camino hacia (4,0)
        
        new_position = (4, 0)
        result = self.queen_black.check_move(self.empty_board, new_position)
        self.assertFalse(result, "La reina negra no debería poder moverse horizontalmente si el camino está bloqueado.")

    def test_black_queen_blocked_vertical_path(self):
        """
        Prueba que la reina negra no puede moverse verticalmente si el camino está bloqueado por una pieza.
        """
        blocking_piece = MockPiece(WHITE)
        self.empty_board[6][4] = blocking_piece  # Bloquea el camino hacia (7,4)
        
        new_position = (7, 4)
        result = self.queen_black.check_move(self.empty_board, new_position)
        self.assertFalse(result, "La reina negra no debería poder moverse verticalmente si el camino está bloqueado.")

    # ### Pruebas Comunes ###

    def test_queen_move_invalid_color(self):
        """
        Prueba que una reina con un color inválido no pueda moverse.
        """
        invalid_color_queen = Queen("blue", (3, 3))
        self.empty_board[3][3] = invalid_color_queen

        new_position = (5, 5)
        result = invalid_color_queen.check_move(self.empty_board, new_position)
        self.assertFalse(result, "Una reina con un color inválido no debería poder moverse.")

    def test_queen_move_invalid_position_type(self):
        """
        Prueba que una reina no pueda moverse a una posición con un tipo inválido (no tuple).
        """
        new_position = "invalid_position"
        with self.assertRaises(TypeError):
            self.queen_white.check_move(self.empty_board, new_position)

    def test_queen_move_invalid_position_value(self):
        """
        Prueba que una reina no pueda moverse a una posición con valores inválidos (no enteros).
        """
        new_position = (5.5, 5.5)
        with self.assertRaises(TypeError):
            self.queen_white.check_move(self.empty_board, new_position)

if __name__ == '__main__':
    unittest.main()
