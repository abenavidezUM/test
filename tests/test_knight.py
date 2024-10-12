# test_knight.py

import unittest
from game.piece import WHITE, BLACK
from game.knight import Knight

class MockPiece:
    """
    Mock class para simular otras piezas en el tablero.
    """
    def __init__(self, color):
        self.__color__ = color

    @property
    def color(self):
        return self.__color__

class TestKnight(unittest.TestCase):
    def setUp(self):
        """
        Configuración inicial antes de cada prueba.
        """
        # Crear un tablero vacío 8x8
        self.empty_board = [[None for _ in range(8)] for _ in range(8)]
        
        # Crear una instancia de Knight blanca en la posición (4, 4)
        self.knight = Knight(WHITE, (4, 4))
        self.empty_board[4][4] = self.knight

    def test_valid_move_top_right(self):
        """
        Prueba un movimiento válido del caballo hacia arriba a la derecha.
        """
        new_position = (6, 5)  # Movimiento en L: +2 filas, +1 columna
        result = self.knight.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El movimiento válido hacia arriba a la derecha debería ser permitido.")

    def test_valid_move_bottom_left(self):
        """
        Prueba un movimiento válido del caballo hacia abajo a la izquierda.
        """
        new_position = (3, 2)  # Movimiento en L: -1 filas, -2 columnas
        result = self.knight.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El movimiento válido hacia abajo a la izquierda debería ser permitido.")

    def test_invalid_move_same_position(self):
        """
        Prueba intentar mover el caballo a su posición actual.
        """
        new_position = (4, 4)
        result = self.knight.check_move(self.empty_board, new_position)
        self.assertFalse(result, "Mover el caballo a su posición actual debería ser rechazado.")

    def test_invalid_move_non_L_shape(self):
        """
        Prueba un movimiento que no sigue la forma en 'L' del caballo.
        """
        new_position = (5, 5)  # Movimiento no válido: +1 fila, +1 columna
        result = self.knight.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El movimiento que no sigue la forma en 'L' debería ser rechazado.")

    def test_move_out_of_bounds_positive(self):
        """
        Prueba un movimiento que sale de los límites del tablero hacia posiciones positivas.
        """
        new_position = (8, 5)  # Fuera de los límites (filas 0-7)
        result = self.knight.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El movimiento fuera de los límites hacia posiciones positivas debería ser rechazado.")

    def test_move_out_of_bounds_negative(self):
        """
        Prueba un movimiento que sale de los límites del tablero hacia posiciones negativas.
        """
        new_position = (2, -1)  # Fuera de los límites (columnas 0-7)
        result = self.knight.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El movimiento fuera de los límites hacia posiciones negativas debería ser rechazado.")

    def test_capture_enemy_piece(self):
        """
        Prueba la captura de una pieza enemiga en una posición válida.
        """
        # Colocar una pieza enemiga en la posición de destino
        enemy_piece = MockPiece(BLACK)
        self.empty_board[6][5] = enemy_piece  # Posición válida de captura

        new_position = (6, 5)
        result = self.knight.check_move(self.empty_board, new_position)
        self.assertTrue(result, "Capturar una pieza enemiga debería ser permitido.")

    def test_capture_friendly_piece(self):
        """
        Prueba el intento de capturar una pieza amiga, lo cual debería ser inválido.
        """
        # Colocar una pieza amiga en la posición de destino
        friendly_piece = MockPiece(WHITE)
        self.empty_board[6][5] = friendly_piece  # Posición válida pero con pieza amiga

        new_position = (6, 5)
        result = self.knight.check_move(self.empty_board, new_position)
        self.assertFalse(result, "Capturar una pieza amiga debería ser rechazado.")

    def test_move_over_pieces(self):
        """
        Prueba que el caballo puede saltar sobre otras piezas.
        """
        # Colocar piezas bloqueando el camino (aunque el caballo puede saltar)
        blocking_piece1 = MockPiece(WHITE)
        blocking_piece2 = MockPiece(BLACK)
        self.empty_board[5][4] = blocking_piece1
        self.empty_board[5][5] = blocking_piece2

        new_position = (6, 5)  # Movimiento en L: +2 filas, +1 columna
        result = self.knight.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El caballo debería poder saltar sobre otras piezas.")

    def test_invalid_move_not_enough_L(self):
        """
        Prueba un movimiento que casi sigue la forma en 'L' pero no lo hace completamente.
        """
        new_position = (7, 6)  # Movimiento en L incompleto: +3 filas, +2 columnas
        result = self.knight.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El movimiento que no sigue completamente la forma en 'L' debería ser rechazado.")

    def test_multiple_valid_moves(self):
        """
        Prueba múltiples movimientos válidos del caballo.
        """
        valid_moves = [
            (6, 5),  # +2 filas, +1 columna
            (6, 3),  # +2 filas, -1 columna
            (5, 6),  # +1 fila, +2 columnas
            (5, 2),  # +1 fila, -2 columnas
            (3, 6),  # -1 fila, +2 columnas
            (3, 2),  # -1 fila, -2 columnas
            (2, 5),  # -2 filas, +1 columna
            (2, 3)   # -2 filas, -1 columna
        ]
        for pos in valid_moves:
            with self.subTest(new_position=pos):
                result = self.knight.check_move(self.empty_board, pos)
                self.assertTrue(result, f"El movimiento válido a {pos} debería ser permitido.")

    def test_move_to_invalid_positions(self):
        """
        Prueba movimientos que no son posibles para el caballo.
        """
        invalid_moves = [
            (4, 5),  # +0 filas, +1 columna
            (5, 4),  # +1 fila, +0 columnas
            (7, 7),  # Movimiento no válido
            (0, 0),  # Movimiento no válido
            (4, 6),  # Movimiento no en 'L'
            (6, 6)   # Movimiento no en 'L'
        ]
        for pos in invalid_moves:
            with self.subTest(new_position=pos):
                result = self.knight.check_move(self.empty_board, pos)
                self.assertFalse(result, f"El movimiento inválido a {pos} debería ser rechazado.")

if __name__ == '__main__':
    unittest.main()
