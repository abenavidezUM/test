# mock_piece.py

from piece import Piece

class MockPiece(Piece):
    """
    MockPiece es una clase concreta que hereda de Piece y se utiliza para pruebas.
    Implementa el método abstracto check_move con una implementación simple.
    """

    def check_move(self, positions, new_position):
        """
        Implementación simplificada de check_move para propósitos de prueba.
        Siempre devuelve False ya que esta pieza no realiza movimientos en las pruebas.
        
        Parameters:
            positions (list): El estado actual del tablero.
            new_position (tuple): La posición a la que se quiere mover.
        
        Returns:
            bool: Siempre False.
        """
        return False

    def __str__(self):
        """
        Retorna un carácter de marcador para identificar la MockPiece en el tablero.
        
        Returns:
            str: "M" para MockPiece.
        """
        return "M"
