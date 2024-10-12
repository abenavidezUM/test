import unittest
from knight import Knight
from piece import Piece, WHITE, BLACK
from abc import ABC, abstractmethod

# Crear una clase MockPiece para usar en las pruebas
class MockPiece(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def check_move(self, positions, new_position):
        # Implementación dummy, ya que no se utiliza en estas pruebas
        pass

class TestKnight(unittest.TestCase):
    def setUp(self):
        # Inicializa un caballo blanco en la posición (4, 4)
        self.white_knight = Knight(WHITE, (4, 4))
        # Inicializa un caballo negro en la posición (0, 0)
        self.black_knight = Knight(BLACK, (0, 0))
    
    def test_initialization(self):
        # Prueba la inicialización del caballo blanco
        self.assertEqual(self.white_knight.color, WHITE)
        self.assertEqual(self.white_knight.position, (4, 4))
        
        # Prueba la inicialización del caballo negro
        self.assertEqual(self.black_knight.color, BLACK)
        self.assertEqual(self.black_knight.position, (0, 0))
    
    def test_str_representation(self):
        # Prueba la representación en cadena del caballo blanco
        self.assertEqual(str(self.white_knight), "♘")
        
        # Prueba la representación en cadena del caballo negro
        self.assertEqual(str(self.black_knight), "♞")
    
    def test_check_move_valid(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Define movimientos válidos para un caballo desde (4, 4)
        valid_moves = [
            (6, 5), (6, 3), (2, 5), (2, 3),
            (5, 6), (5, 2), (3, 6), (3, 2)
        ]
        
        for move in valid_moves:
            with self.subTest(move=move):
                self.assertTrue(self.white_knight.check_move(board, move))
    
    def test_check_move_invalid_not_L_shape(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Define movimientos inválidos que no siguen la forma de 'L'
        invalid_moves = [
            (4, 5), (5, 5), (4, 6), (6, 6),
            (4, 3), (3, 3), (4, 2), (2, 2),
            (5, 4), (3, 4)
        ]
        
        for move in invalid_moves:
            with self.subTest(move=move):
                self.assertFalse(self.white_knight.check_move(board, move))
    
    def test_check_move_capture_opposite_color(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        # Coloca una pieza enemiga en una posición válida de captura
        board[6][5] = MockPiece(BLACK, (6, 5))
        
        # El caballo blanco intenta moverse a (6, 5) donde hay una pieza negra
        self.assertTrue(self.white_knight.check_move(board, (6, 5)))
    
    def test_check_move_capture_same_color(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        # Coloca una pieza amiga en una posición válida de movimiento
        board[6][5] = MockPiece(WHITE, (6, 5))
        
        # El caballo blanco intenta moverse a (6, 5) donde hay una pieza blanca
        self.assertFalse(self.white_knight.check_move(board, (6, 5)))
    
    def test_check_move_out_of_bounds(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Define movimientos fuera del tablero
        out_of_bounds_moves = [
            (-1, -2), (8, 8), (7, 6), (6, 7)
        ]
        
        for move in out_of_bounds_moves:
            with self.subTest(move=move):
                self.assertFalse(self.white_knight.check_move(board, move))

if __name__ == '__main__':
    unittest.main()
