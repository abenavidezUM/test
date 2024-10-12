import unittest
from game.pawn import Pawn
from game.piece import Piece, WHITE, BLACK
from abc import ABC, abstractmethod

# Crear una clase MockPiece para usar en las pruebas
class MockPiece(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)

    def check_move(self, positions, new_position):
        # Implementación dummy, ya que no se utiliza en estas pruebas
        pass

class TestPawn(unittest.TestCase):
    def setUp(self):
        # Inicializa un peón blanco en la posición (6, 4) (fila inicial para blancos)
        self.white_pawn_initial = Pawn(WHITE, (6, 4))
        # Inicializa un peón blanco en una posición no inicial (5, 4)
        self.white_pawn = Pawn(WHITE, (5, 4))
        
        # Inicializa un peón negro en la posición (1, 3) (fila inicial para negros)
        self.black_pawn_initial = Pawn(BLACK, (1, 3))
        # Inicializa un peón negro en una posición no inicial (2, 3)
        self.black_pawn = Pawn(BLACK, (2, 3))
    
    def test_initialization(self):
        # Prueba la inicialización del peón blanco en posición inicial
        self.assertEqual(self.white_pawn_initial.color, WHITE)
        self.assertEqual(self.white_pawn_initial.position, (6, 4))
        
        # Prueba la inicialización del peón blanco en posición no inicial
        self.assertEqual(self.white_pawn.color, WHITE)
        self.assertEqual(self.white_pawn.position, (5, 4))
        
        # Prueba la inicialización del peón negro en posición inicial
        self.assertEqual(self.black_pawn_initial.color, BLACK)
        self.assertEqual(self.black_pawn_initial.position, (1, 3))
        
        # Prueba la inicialización del peón negro en posición no inicial
        self.assertEqual(self.black_pawn.color, BLACK)
        self.assertEqual(self.black_pawn.position, (2, 3))
    
    def test_str_representation(self):
        # Prueba la representación en cadena del peón blanco
        self.assertEqual(str(self.white_pawn_initial), "♙")
        
        # Prueba la representación en cadena del peón negro
        self.assertEqual(str(self.black_pawn_initial), "♟")
    
    def test_check_move_forward_one_white(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Peón blanco en (5, 4) intenta mover a (4, 4)
        self.assertTrue(self.white_pawn.check_move(board, (4, 4)))
    
    def test_check_move_forward_two_white_initial(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Peón blanco en posición inicial (6, 4) intenta mover a (4, 4)
        self.assertTrue(self.white_pawn_initial.check_move(board, (4, 4)))
    
    def test_check_move_forward_two_white_not_initial(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Peón blanco en posición no inicial (5, 4) intenta mover a (3, 4)
        self.assertFalse(self.white_pawn.check_move(board, (3, 4)))
    
    def test_check_move_forward_one_blocked_white(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        # Coloca una pieza en la posición a la que el peón intenta moverse
        board[4][4] = MockPiece(BLACK, (4, 4))
        
        # Peón blanco en (5, 4) intenta mover a (4, 4) pero está bloqueado
        self.assertFalse(self.white_pawn.check_move(board, (4, 4)))
    
    def test_check_move_capture_diagonal_white(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        # Coloca una pieza enemiga en la diagonal derecha
        board[4][5] = MockPiece(BLACK, (4, 5))
        # Coloca una pieza enemiga en la diagonal izquierda
        board[4][3] = MockPiece(BLACK, (4, 3))
        
        # Peón blanco en (5, 4) intenta capturar a (4, 5)
        self.assertTrue(self.white_pawn.check_move(board, (4, 5)))
        
        # Peón blanco en (5, 4) intenta capturar a (4, 3)
        self.assertTrue(self.white_pawn.check_move(board, (4, 3)))
    
    def test_check_move_capture_diagonal_same_color_white(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        # Coloca una pieza amiga en la diagonal derecha
        board[4][5] = MockPiece(WHITE, (4, 5))
        
        # Peón blanco en (5, 4) intenta capturar a (4, 5) donde hay una pieza blanca
        self.assertFalse(self.white_pawn.check_move(board, (4, 5)))
    
    def test_check_move_forward_one_black(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Peón negro en (2, 3) intenta mover a (3, 3)
        self.assertTrue(self.black_pawn.check_move(board, (3, 3)))
    
    def test_check_move_forward_two_black_initial(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Peón negro en posición inicial (1, 3) intenta mover a (3, 3)
        self.assertTrue(self.black_pawn_initial.check_move(board, (3, 3)))
    
    def test_check_move_forward_two_black_not_initial(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Peón negro en posición no inicial (2, 3) intenta mover a (4, 3)
        self.assertFalse(self.black_pawn.check_move(board, (4, 3)))
    
    def test_check_move_forward_one_blocked_black(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        # Coloca una pieza en la posición a la que el peón intenta moverse
        board[3][3] = MockPiece(WHITE, (3, 3))
        
        # Peón negro en (2, 3) intenta mover a (3, 3) pero está bloqueado
        self.assertFalse(self.black_pawn.check_move(board, (3, 3)))
    
    def test_check_move_capture_diagonal_black(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        # Coloca una pieza enemiga en la diagonal derecha
        board[3][4] = MockPiece(WHITE, (3, 4))
        # Coloca una pieza enemiga en la diagonal izquierda
        board[3][2] = MockPiece(WHITE, (3, 2))
        
        # Peón negro en (2, 3) intenta capturar a (3, 4)
        self.assertTrue(self.black_pawn.check_move(board, (3, 4)))
        
        # Peón negro en (2, 3) intenta capturar a (3, 2)
        self.assertTrue(self.black_pawn.check_move(board, (3, 2)))
    
    def test_check_move_capture_diagonal_same_color_black(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        # Coloca una pieza amiga en la diagonal derecha
        board[3][4] = MockPiece(BLACK, (3, 4))
        
        # Peón negro en (2, 3) intenta capturar a (3, 4) donde hay una pieza negra
        self.assertFalse(self.black_pawn.check_move(board, (3, 4)))
    
    def test_check_move_invalid_direction_white(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Peón blanco en (5, 4) intenta mover hacia atrás a (6, 4)
        self.assertFalse(self.white_pawn.check_move(board, (6, 4)))
    
    def test_check_move_invalid_direction_black(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Peón negro en (2, 3) intenta mover hacia atrás a (1, 3)
        self.assertFalse(self.black_pawn.check_move(board, (1, 3)))
    
    def test_check_move_out_of_bounds(self):
        # Crea un tablero vacío
        board = [[None for _ in range(8)] for _ in range(8)]
        
        # Movimientos fuera del tablero para peón blanco
        out_of_bounds_moves_white = [
            (7, 4),  # Mover hacia atrás
            (4, 4),  # Desde inicial, pero (4,4) es válido, solo limitar
            (-1, -1),
            (8, 8)
        ]
        for move in out_of_bounds_moves_white:
            with self.subTest(move=move):
                # Evitamos incluir (4,4) ya que es un movimiento válido
                if not (move == (4, 4)):
                    self.assertFalse(self.white_pawn_initial.check_move(board, move))
        
        # Movimientos fuera del tablero para peón negro
        out_of_bounds_moves_black = [
            (0, 3),  # Mover hacia atrás
            (3, 3),  # Desde inicial, pero (3,3) es válido, solo limitar
            (-1, -1),
            (8, 8)
        ]
        for move in out_of_bounds_moves_black:
            with self.subTest(move=move):
                # Evitamos incluir (3,3) ya que es un movimiento válido
                if not (move == (3, 3)):
                    self.assertFalse(self.black_pawn_initial.check_move(board, move))

if __name__ == '__main__':
    unittest.main()
