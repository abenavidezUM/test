import unittest
from game.king import King
from game.piece import Piece, WHITE, BLACK
from abc import ABC, abstractmethod

# Crear una clase MockPiece para usar en las pruebas
class MockPiece(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def check_move(self, positions, new_position):
        # Implementación dummy, ya que no se utiliza en estas pruebas
        pass

class TestKing(unittest.TestCase):
    def setUp(self):
        # Inicializa un rey blanco en la posición (4, 4)
        self.white_king = King(WHITE, (4, 4))
        # Inicializa un rey negro en la posición (0, 0)
        self.black_king = King(BLACK, (0, 0))
    
    def test_initialization(self):
        # Prueba la inicialización del rey blanco
        self.assertEqual(self.white_king.color, WHITE)
        self.assertEqual(self.white_king.position, (4, 4))
        
        # Prueba la inicialización del rey negro
        self.assertEqual(self.black_king.color, BLACK)
        self.assertEqual(self.black_king.position, (0, 0))
    
    def test_str_representation(self):
        # Prueba la representación en cadena del rey blanco
        self.assertEqual(str(self.white_king), "♔")
        
        # Prueba la representación en cadena del rey negro
        self.assertEqual(str(self.black_king), "♚")
    
    def test_check_move_valid(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Prueba movimientos válidos para el rey blanco
        valid_moves = [
            (5, 5), (5, 4), (5, 3),
            (4, 5),        (4, 3),
            (3, 5), (3, 4), (3, 3)
        ]
        
        for move in valid_moves:
            with self.subTest(move=move):
                self.assertTrue(self.white_king.check_move(board, move))
    
    def test_check_move_invalid_out_of_range(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Movimientos inválidos que están fuera del rango de un movimiento de rey
        invalid_moves = [
            (6, 6), (7, 7), (2, 2),
            (4, 6), (6, 4), (2, 4)
        ]
        
        for move in invalid_moves:
            with self.subTest(move=move):
                self.assertFalse(self.white_king.check_move(board, move))
    
    def test_check_move_capture_opposite_color(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        # Coloca una pieza enemiga en (5, 5)
        board[5][5] = MockPiece(BLACK, (5, 5))
        
        # El rey blanco intenta moverse a (5, 5) donde hay una pieza negra
        self.assertTrue(self.white_king.check_move(board, (5, 5)))
    
    def test_check_move_capture_same_color(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        # Coloca una pieza amiga en (5, 5)
        board[5][5] = MockPiece(WHITE, (5, 5))
        
        # El rey blanco intenta moverse a (5, 5) donde hay una pieza blanca
        self.assertFalse(self.white_king.check_move(board, (5, 5)))

if __name__ == '__main__':
    unittest.main()
