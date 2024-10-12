# test_bishop.py

import unittest
from unittest.mock import MagicMock
from game.piece import WHITE, BLACK
from game.bishop import Bishop

class MockPiece:
    """
    Mock class para simular otras piezas en el tablero.
    """
    def __init__(self, color):
        self.__color__ = color

    @property
    def color(self):
        return self.__color__

class TestBishop(unittest.TestCase):
    def setUp(self):
        """
        Configuración inicial antes de cada prueba.
        """
        # Crear un tablero vacío 8x8
        self.empty_board = [[None for _ in range(8)] for _ in range(8)]
        
        # Crear una instancia de Bishop blanca en la posición (4, 4)
        self.bishop = Bishop(WHITE, (4, 4))
        self.empty_board[4][4] = self.bishop

    def test_valid_move_diagonal_empty_path(self):
        """
        Prueba un movimiento diagonal válido sin obstáculos.
        """
        new_position = (6, 6)  # Movimiento diagonal hacia arriba a la derecha
        result = self.bishop.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El movimiento diagonal válido debería ser permitido.")

    def test_invalid_move_non_diagonal(self):
        """
        Prueba un movimiento no diagonal, que debería ser inválido.
        """
        new_position = (4, 6)  # Movimiento horizontal
        result = self.bishop.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El movimiento no diagonal debería ser rechazado.")

    def test_move_with_blocked_path(self):
        """
        Prueba un movimiento diagonal con una pieza bloqueando el camino.
        """
        # Colocar una pieza en el camino del alfil
        blocking_piece = MockPiece(WHITE)
        self.empty_board[5][5] = blocking_piece  # Bloquea el camino hacia (6,6)
        
        new_position = (6, 6)
        result = self.bishop.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El movimiento diagonal con obstáculos debería ser rechazado.")

    def test_move_out_of_bounds(self):
        """
        Prueba un movimiento que sale de los límites del tablero.
        """
        new_position = (8, 8)  # Fuera de los límites
        result = self.bishop.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El movimiento fuera de los límites debería ser rechazado.")

    def test_capture_enemy_piece(self):
        """
        Prueba la captura de una pieza enemiga en una posición diagonal válida.
        """
        # Colocar una pieza enemiga en la posición de destino
        enemy_piece = MockPiece(BLACK)
        self.empty_board[6][6] = enemy_piece
        
        new_position = (6, 6)
        result = self.bishop.check_move(self.empty_board, new_position)
        self.assertTrue(result, "Capturar una pieza enemiga debería ser permitido.")

    def test_capture_friendly_piece(self):
        """
        Prueba el intento de capturar una pieza amiga, lo cual debería ser inválido.
        """
        # Colocar una pieza amiga en la posición de destino
        friendly_piece = MockPiece(WHITE)
        self.empty_board[6][6] = friendly_piece
        
        new_position = (6, 6)
        result = self.bishop.check_move(self.empty_board, new_position)
        self.assertFalse(result, "Capturar una pieza amiga debería ser rechazado.")

    def test_move_to_same_position(self):
        """
        Prueba intentar mover el alfil a su posición actual.
        """
        new_position = (4, 4)
        result = self.bishop.check_move(self.empty_board, new_position)
        self.assertFalse(result, "Mover el alfil a su posición actual debería ser rechazado.")

    def test_move_negative_indices(self):
        """
        Prueba un movimiento con índices negativos, fuera de los límites del tablero.
        """
        new_position = (-1, -1)
        result = self.bishop.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El movimiento con índices negativos debería ser rechazado.")

    def test_move_partial_blocked_path(self):
        """
        Prueba un movimiento diagonal con una pieza bloqueando parcialmente el camino.
        """
        # Bloquear parcialmente el camino
        blocking_piece = MockPiece(BLACK)
        self.empty_board[5][5] = blocking_piece  # Bloquea el camino hacia (6,6)
        
        new_position = (6, 6)
        result = self.bishop.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El movimiento diagonal con una pieza bloqueando el camino debería ser rechazado.")

    def test_move_multiple_diagonals(self):
        """
        Prueba múltiples movimientos diagonales válidos y no válidos.
        """
        # Movimiento válido hacia abajo a la izquierda
        new_position = (2, 2)
        result = self.bishop.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El movimiento diagonal válido hacia abajo a la izquierda debería ser permitido.")
        
        # Movimiento válido hacia arriba a la izquierda
        new_position = (6, 2)
        result = self.bishop.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El movimiento diagonal válido hacia arriba a la izquierda debería ser permitido.")
        
        # Movimiento no diagonal hacia arriba
        new_position = (6, 4)
        result = self.bishop.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El movimiento no diagonal debería ser rechazado.")

    def test_move_long_diagonal_with_no_obstacles(self):
        """
        Prueba un movimiento diagonal largo sin obstáculos.
        """
        new_position = (0, 0)  # Movimiento diagonal largo hacia la esquina superior izquierda
        result = self.bishop.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El movimiento diagonal largo sin obstáculos debería ser permitido.")

    def test_move_long_diagonal_with_obstacles(self):
        """
        Prueba un movimiento diagonal largo con una pieza bloqueando el camino.
        """
        # Colocar una pieza en el camino del alfil
        blocking_piece = MockPiece(BLACK)
        self.empty_board[2][2] = blocking_piece  # Bloquea el camino hacia (0,0)
        
        new_position = (0, 0)
        result = self.bishop.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El movimiento diagonal largo con obstáculos debería ser rechazado.")

if __name__ == '__main__':
    unittest.main()
