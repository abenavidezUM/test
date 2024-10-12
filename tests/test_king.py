# test_king.py

import unittest
from game.piece import WHITE, BLACK
from game.king import King

class MockPiece:
    """
    Mock class para simular otras piezas en el tablero.
    """
    def __init__(self, color):
        self.__color__ = color

    @property
    def color(self):
        return self.__color__

class TestKing(unittest.TestCase):
    def setUp(self):
        """
        Configuración inicial antes de cada prueba.
        """
        # Crear un tablero vacío 8x8
        self.empty_board = [[None for _ in range(8)] for _ in range(8)]
        
        # Crear una instancia de King blanca en la posición (4, 4)
        self.king = King(WHITE, (4, 4))
        self.empty_board[4][4] = self.king

    def test_valid_move_up(self):
        """
        Prueba un movimiento válido hacia arriba.
        """
        new_position = (3, 4)
        result = self.king.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El movimiento hacia arriba debería ser permitido.")

    def test_valid_move_down(self):
        """
        Prueba un movimiento válido hacia abajo.
        """
        new_position = (5, 4)
        result = self.king.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El movimiento hacia abajo debería ser permitido.")

    def test_valid_move_left(self):
        """
        Prueba un movimiento válido hacia la izquierda.
        """
        new_position = (4, 3)
        result = self.king.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El movimiento hacia la izquierda debería ser permitido.")

    def test_valid_move_right(self):
        """
        Prueba un movimiento válido hacia la derecha.
        """
        new_position = (4, 5)
        result = self.king.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El movimiento hacia la derecha debería ser permitido.")

    def test_valid_move_up_left(self):
        """
        Prueba un movimiento válido hacia arriba a la izquierda.
        """
        new_position = (3, 3)
        result = self.king.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El movimiento hacia arriba a la izquierda debería ser permitido.")

    def test_valid_move_up_right(self):
        """
        Prueba un movimiento válido hacia arriba a la derecha.
        """
        new_position = (3, 5)
        result = self.king.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El movimiento hacia arriba a la derecha debería ser permitido.")

    def test_valid_move_down_left(self):
        """
        Prueba un movimiento válido hacia abajo a la izquierda.
        """
        new_position = (5, 3)
        result = self.king.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El movimiento hacia abajo a la izquierda debería ser permitido.")

    def test_valid_move_down_right(self):
        """
        Prueba un movimiento válido hacia abajo a la derecha.
        """
        new_position = (5, 5)
        result = self.king.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El movimiento hacia abajo a la derecha debería ser permitido.")

    def test_invalid_move_two_squares(self):
        """
        Prueba un movimiento inválido de dos casillas hacia arriba.
        """
        new_position = (2, 4)
        result = self.king.check_move(self.empty_board, new_position)
        self.assertFalse(result, "Mover dos casillas hacia arriba debería ser rechazado.")

    def test_invalid_move_out_of_bounds_positive(self):
        """
        Prueba un movimiento fuera de los límites del tablero (superior derecho).
        """
        new_position = (8, 8)
        result = self.king.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El movimiento fuera de los límites debería ser rechazado.")

    def test_invalid_move_out_of_bounds_negative(self):
        """
        Prueba un movimiento fuera de los límites del tablero (inferior izquierdo).
        """
        new_position = (-1, -1)
        result = self.king.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El movimiento fuera de los límites con índices negativos debería ser rechazado.")

    def test_capture_enemy_piece(self):
        """
        Prueba la captura de una pieza enemiga en una posición adyacente.
        """
        # Colocar una pieza enemiga en la posición de destino
        enemy_piece = MockPiece(BLACK)
        self.empty_board[3][4] = enemy_piece  # Movimiento hacia arriba
        new_position = (3, 4)
        result = self.king.check_move(self.empty_board, new_position)
        self.assertTrue(result, "Capturar una pieza enemiga debería ser permitido.")

    def test_capture_friendly_piece(self):
        """
        Prueba el intento de capturar una pieza amiga, lo cual debería ser inválido.
        """
        # Colocar una pieza amiga en la posición de destino
        friendly_piece = MockPiece(WHITE)
        self.empty_board[3][4] = friendly_piece  # Movimiento hacia arriba
        new_position = (3, 4)
        result = self.king.check_move(self.empty_board, new_position)
        self.assertFalse(result, "Capturar una pieza amiga debería ser rechazado.")

    def test_move_to_same_position(self):
        """
        Prueba intentar mover el rey a su posición actual.
        """
        new_position = (4, 4)
        result = self.king.check_move(self.empty_board, new_position)
        self.assertFalse(result, "Mover el rey a su posición actual debería ser rechazado.")

    def test_move_diagonal_no_capture_enemy(self):
        """
        Prueba un movimiento diagonal válido sin capturar ninguna pieza.
        """
        new_position = (3, 3)
        result = self.king.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El movimiento diagonal válido sin capturar debería ser permitido.")

    def test_move_diagonal_with_enemy_blocking(self):
        """
        Prueba un movimiento diagonal donde hay una pieza enemiga en la casilla de destino.
        """
        # Colocar una pieza enemiga en la posición de destino
        enemy_piece = MockPiece(BLACK)
        self.empty_board[3][3] = enemy_piece
        new_position = (3, 3)
        result = self.king.check_move(self.empty_board, new_position)
        self.assertTrue(result, "Capturar una pieza enemiga en un movimiento diagonal debería ser permitido.")

    def test_move_diagonal_with_friendly_blocking(self):
        """
        Prueba un movimiento diagonal donde hay una pieza amiga en la casilla de destino.
        """
        # Colocar una pieza amiga en la posición de destino
        friendly_piece = MockPiece(WHITE)
        self.empty_board[3][3] = friendly_piece
        new_position = (3, 3)
        result = self.king.check_move(self.empty_board, new_position)
        self.assertFalse(result, "Capturar una pieza amiga en un movimiento diagonal debería ser rechazado.")

    def test_move_non_adjacent_square(self):
        """
        Prueba un movimiento no adyacente, como saltar varias casillas.
        """
        new_position = (6, 6)
        result = self.king.check_move(self.empty_board, new_position)
        self.assertFalse(result, "Mover a una casilla no adyacente debería ser rechazado.")

    def test_move_knight_like_move(self):
        """
        Prueba un movimiento en forma de 'L' (como el caballo), que debería ser inválido.
        """
        new_position = (2, 5)  # Movimiento de dos hacia arriba y una hacia la derecha
        result = self.king.check_move(self.empty_board, new_position)
        self.assertFalse(result, "Mover en forma de 'L' debería ser rechazado.")

    def test_move_with_obstacle_not_in_destination(self):
        """
        Prueba un movimiento adyacente válido cuando hay una pieza bloqueando una dirección diferente.
        """
        # Colocar una pieza en una dirección diferente
        blocking_piece = MockPiece(BLACK)
        self.empty_board[3][5] = blocking_piece  # No afecta el movimiento hacia (3,4)
        
        new_position = (3, 4)
        result = self.king.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El movimiento adyacente válido debería ser permitido incluso con otras piezas bloqueando.")

    def test_move_to_edge_of_board(self):
        """
        Prueba un movimiento válido hacia el borde del tablero.
        """
        # Colocar el rey en una posición cercana al borde
        self.king.position = (0, 0)
        self.empty_board[4][4] = None  # Limpiar la posición anterior
        self.empty_board[0][0] = self.king

        new_position = (0, 1)
        result = self.king.check_move(self.empty_board, new_position)
        self.assertTrue(result, "Mover el rey hacia el borde del tablero debería ser permitido.")

    def test_move_to_corner_out_of_bounds(self):
        """
        Prueba un movimiento hacia una esquina fuera de los límites del tablero.
        """
        # Colocar el rey en una posición cercana al borde
        self.king.position = (0, 0)
        self.empty_board[4][4] = None  # Limpiar la posición anterior
        self.empty_board[0][0] = self.king

        new_position = (-1, -1)
        result = self.king.check_move(self.empty_board, new_position)
        self.assertFalse(result, "Mover el rey a una esquina fuera de los límites debería ser rechazado.")

if __name__ == '__main__':
    unittest.main()
