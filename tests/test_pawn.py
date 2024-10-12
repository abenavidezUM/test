# test_pawn.py

import unittest
from game.piece import WHITE, BLACK
from game.pawn import Pawn

class MockPiece:
    """
    Mock class para simular otras piezas en el tablero.
    """
    def __init__(self, color):
        self.__color__ = color

    @property
    def color(self):
        return self.__color__

class TestPawn(unittest.TestCase):
    def setUp(self):
        """
        Configuración inicial antes de cada prueba.
        """
        # Crear un tablero vacío 8x8
        self.empty_board = [[None for _ in range(8)] for _ in range(8)]
        
        # Crear una instancia de Pawn blanca en la posición inicial (6, 4)
        self.pawn_white_initial = Pawn(WHITE, (6, 4))
        self.empty_board[6][4] = self.pawn_white_initial
        
        # Crear una instancia de Pawn negra en la posición inicial (1, 3)
        self.pawn_black_initial = Pawn(BLACK, (1, 3))
        self.empty_board[1][3] = self.pawn_black_initial

    # ### Pruebas para Peón Blanco ###

    def test_white_pawn_move_one_step_forward(self):
        """
        Prueba que un peón blanco puede moverse una casilla hacia adelante si está libre.
        """
        new_position = (5, 4)
        result = self.pawn_white_initial.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El peón blanco debería poder moverse una casilla hacia adelante.")

    def test_white_pawn_move_two_steps_forward_initial_position(self):
        """
        Prueba que un peón blanco puede moverse dos casillas hacia adelante desde la posición inicial si están libres.
        """
        new_position = (4, 4)
        result = self.pawn_white_initial.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El peón blanco debería poder mover dos casillas hacia adelante desde la posición inicial.")

    def test_white_pawn_move_two_steps_forward_non_initial_position(self):
        """
        Prueba que un peón blanco no puede mover dos casillas hacia adelante desde una posición no inicial.
        """
        # Mover el peón una casilla hacia adelante primero
        self.pawn_white_initial.position = (5, 4)
        self.empty_board[6][4] = None
        self.empty_board[5][4] = self.pawn_white_initial

        new_position = (3, 4)
        result = self.pawn_white_initial.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El peón blanco no debería poder mover dos casillas desde una posición no inicial.")

    def test_white_pawn_move_forward_blocked(self):
        """
        Prueba que un peón blanco no puede moverse hacia adelante si la casilla está ocupada.
        """
        # Colocar una pieza delante del peón blanco
        blocking_piece = MockPiece(BLACK)
        self.empty_board[5][4] = blocking_piece

        new_position = (5, 4)
        result = self.pawn_white_initial.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El peón blanco no debería poder moverse hacia adelante si la casilla está ocupada.")

    def test_white_pawn_capture_enemy_piece_diagonal_left(self):
        """
        Prueba que un peón blanco puede capturar una pieza enemiga en la diagonal izquierda.
        """
        enemy_piece = MockPiece(BLACK)
        self.empty_board[5][3] = enemy_piece

        new_position = (5, 3)
        result = self.pawn_white_initial.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El peón blanco debería poder capturar una pieza enemiga en la diagonal izquierda.")

    def test_white_pawn_capture_enemy_piece_diagonal_right(self):
        """
        Prueba que un peón blanco puede capturar una pieza enemiga en la diagonal derecha.
        """
        enemy_piece = MockPiece(BLACK)
        self.empty_board[5][5] = enemy_piece

        new_position = (5, 5)
        result = self.pawn_white_initial.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El peón blanco debería poder capturar una pieza enemiga en la diagonal derecha.")

    def test_white_pawn_capture_friendly_piece(self):
        """
        Prueba que un peón blanco no puede capturar una pieza amiga.
        """
        friendly_piece = MockPiece(WHITE)
        self.empty_board[5][3] = friendly_piece

        new_position = (5, 3)
        result = self.pawn_white_initial.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El peón blanco no debería poder capturar una pieza amiga.")

    def test_white_pawn_move_to_same_position(self):
        """
        Prueba que un peón blanco no puede moverse a su posición actual.
        """
        new_position = (6, 4)
        result = self.pawn_white_initial.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El peón blanco no debería poder moverse a su posición actual.")

    def test_white_pawn_move_out_of_bounds_positive(self):
        """
        Prueba que un peón blanco no puede moverse fuera de los límites del tablero hacia arriba.
        """
        new_position = (-1, 4)  # Fuera de los límites superiores
        result = self.pawn_white_initial.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El peón blanco no debería poder moverse fuera de los límites hacia arriba.")

    def test_white_pawn_move_out_of_bounds_negative(self):
        """
        Prueba que un peón blanco no puede moverse fuera de los límites del tablero lateralmente.
        """
        new_position = (5, -1)  # Fuera de los límites laterales
        result = self.pawn_white_initial.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El peón blanco no debería poder moverse fuera de los límites lateralmente.")

    def test_white_pawn_move_backward(self):
        """
        Prueba que un peón blanco no puede moverse hacia atrás.
        """
        new_position = (7, 4)  # Movimiento hacia atrás
        result = self.pawn_white_initial.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El peón blanco no debería poder moverse hacia atrás.")

    def test_white_pawn_move_sideways(self):
        """
        Prueba que un peón blanco no puede moverse lateralmente.
        """
        new_position = (6, 5)  # Movimiento lateral
        result = self.pawn_white_initial.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El peón blanco no debería poder moverse lateralmente.")

    # ### Pruebas para Peón Negro ###

    def test_black_pawn_move_one_step_forward(self):
        """
        Prueba que un peón negro puede moverse una casilla hacia adelante si está libre.
        """
        new_position = (2, 3)
        result = self.pawn_black_initial.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El peón negro debería poder moverse una casilla hacia adelante.")

    def test_black_pawn_move_two_steps_forward_initial_position(self):
        """
        Prueba que un peón negro puede moverse dos casillas hacia adelante desde la posición inicial si están libres.
        """
        new_position = (3, 3)
        result = self.pawn_black_initial.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El peón negro debería poder mover dos casillas hacia adelante desde la posición inicial.")

    def test_black_pawn_move_two_steps_forward_non_initial_position(self):
        """
        Prueba que un peón negro no puede mover dos casillas hacia adelante desde una posición no inicial.
        """
        # Mover el peón una casilla hacia adelante primero
        self.pawn_black_initial.position = (2, 3)
        self.empty_board[1][3] = None
        self.empty_board[2][3] = self.pawn_black_initial

        new_position = (4, 3)
        result = self.pawn_black_initial.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El peón negro no debería poder mover dos casillas desde una posición no inicial.")

    def test_black_pawn_move_forward_blocked(self):
        """
        Prueba que un peón negro no puede moverse hacia adelante si la casilla está ocupada.
        """
        # Colocar una pieza delante del peón negro
        blocking_piece = MockPiece(WHITE)
        self.empty_board[2][3] = blocking_piece

        new_position = (2, 3)
        result = self.pawn_black_initial.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El peón negro no debería poder moverse hacia adelante si la casilla está ocupada.")

    def test_black_pawn_capture_enemy_piece_diagonal_left(self):
        """
        Prueba que un peón negro puede capturar una pieza enemiga en la diagonal izquierda.
        """
        enemy_piece = MockPiece(WHITE)
        self.empty_board[2][2] = enemy_piece

        new_position = (2, 2)
        result = self.pawn_black_initial.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El peón negro debería poder capturar una pieza enemiga en la diagonal izquierda.")

    def test_black_pawn_capture_enemy_piece_diagonal_right(self):
        """
        Prueba que un peón negro puede capturar una pieza enemiga en la diagonal derecha.
        """
        enemy_piece = MockPiece(WHITE)
        self.empty_board[2][4] = enemy_piece

        new_position = (2, 4)
        result = self.pawn_black_initial.check_move(self.empty_board, new_position)
        self.assertTrue(result, "El peón negro debería poder capturar una pieza enemiga en la diagonal derecha.")

    def test_black_pawn_capture_friendly_piece(self):
        """
        Prueba que un peón negro no puede capturar una pieza amiga.
        """
        friendly_piece = MockPiece(BLACK)
        self.empty_board[2][2] = friendly_piece

        new_position = (2, 2)
        result = self.pawn_black_initial.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El peón negro no debería poder capturar una pieza amiga.")

    def test_black_pawn_move_to_same_position(self):
        """
        Prueba que un peón negro no puede moverse a su posición actual.
        """
        new_position = (1, 3)
        result = self.pawn_black_initial.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El peón negro no debería poder moverse a su posición actual.")

    def test_black_pawn_move_out_of_bounds_positive(self):
        """
        Prueba que un peón negro no puede moverse fuera de los límites del tablero hacia abajo.
        """
        new_position = (8, 3)  # Fuera de los límites inferiores
        result = self.pawn_black_initial.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El peón negro no debería poder moverse fuera de los límites hacia abajo.")

    def test_black_pawn_move_out_of_bounds_negative(self):
        """
        Prueba que un peón negro no puede moverse fuera de los límites del tablero lateralmente.
        """
        new_position = (2, -1)  # Fuera de los límites laterales
        result = self.pawn_black_initial.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El peón negro no debería poder moverse fuera de los límites lateralmente.")

    def test_black_pawn_move_backward(self):
        """
        Prueba que un peón negro no puede moverse hacia atrás.
        """
        new_position = (0, 3)  # Movimiento hacia atrás
        result = self.pawn_black_initial.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El peón negro no debería poder moverse hacia atrás.")

    def test_black_pawn_move_sideways(self):
        """
        Prueba que un peón negro no puede moverse lateralmente.
        """
        new_position = (1, 4)  # Movimiento lateral
        result = self.pawn_black_initial.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El peón negro no debería poder moverse lateralmente.")

    def test_black_pawn_move_over_pieces(self):
        """
        Prueba que un peón negro no puede mover hacia adelante si hay una pieza en el camino.
        """
        # Colocar piezas delante del peón negro
        blocking_piece1 = MockPiece(WHITE)
        blocking_piece2 = MockPiece(BLACK)
        self.empty_board[2][3] = blocking_piece1  # Bloquea un paso hacia adelante

        new_position = (3, 3)
        result = self.pawn_black_initial.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El peón negro no debería poder moverse hacia adelante si la casilla está ocupada.")

    def test_black_pawn_move_two_steps_forward_with_blocked_path(self):
        """
        Prueba que un peón negro no puede mover dos casillas hacia adelante si una de las casillas está ocupada.
        """
        # Colocar una pieza una casilla adelante del peón negro
        blocking_piece = MockPiece(WHITE)
        self.empty_board[2][3] = blocking_piece

        new_position = (3, 3)
        result = self.pawn_black_initial.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El peón negro no debería poder mover dos casillas hacia adelante si una casilla está ocupada.")

    def test_black_pawn_capture_diagonal_empty_square(self):
        """
        Prueba que un peón negro no puede capturar en una casilla diagonal vacía.
        """
        new_position = (2, 2)  # Casilla diagonal vacía
        result = self.pawn_black_initial.check_move(self.empty_board, new_position)
        self.assertFalse(result, "El peón negro no debería poder capturar en una casilla diagonal vacía.")

    # ### Pruebas Comunes ###

    def test_pawn_move_invalid_color(self):
        """
        Prueba que un peón con un color inválido no pueda moverse.
        """
        invalid_color_pawn = Pawn("blue", (6, 4))
        self.empty_board[6][4] = invalid_color_pawn

        new_position = (5, 4)
        result = invalid_color_pawn.check_move(self.empty_board, new_position)
        self.assertFalse(result, "Un peón con un color inválido no debería poder moverse.")

    def test_pawn_move_invalid_position_type(self):
        """
        Prueba que un peón no pueda moverse a una posición con un tipo inválido (no tuple).
        """
        new_position = "invalid_position"
        with self.assertRaises(TypeError):
            self.pawn_white_initial.check_move(self.empty_board, new_position)

    def test_pawn_move_invalid_position_value(self):
        """
        Prueba que un peón no pueda moverse a una posición con valores inválidos (no enteros).
        """
        new_position = (5.5, 4.2)
        with self.assertRaises(TypeError):
            self.pawn_white_initial.check_move(self.empty_board, new_position)

if __name__ == '__main__':
    unittest.main()
