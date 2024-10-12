# game/bishop.py

from .piece import Piece, WHITE, BLACK

class Bishop(Piece):
    """
    Represents a bishop chess piece, inheriting from the Piece base class.
    """

    def __init__(self, color, position):
        """
        Initializes a Bishop instance with a color and position.

        Parameters:
            color (str): The color of the bishop, e.g., "white" or "black".
            position (tuple): The current position of the bishop on the board.
        """
        super().__init__(color, position)

    def __str__(self):
        """
        Returns the Unicode character representing the bishop, depending on its color.

        Returns:
            str: "♗" if the bishop is white, "♝" if the bishop is black.
        """
        return "♗" if self.color == WHITE else "♝"

    def check_move(self, positions, new_position):
        """
        Checks if moving to new_position is a valid move for the bishop.

        Parameters:
            positions (list): The current state of the board.
            new_position (tuple): The position to move to.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        try:
            new_x, new_y, current_x, current_y = self.get_coordinates(new_position)
        except TypeError:
            # new_position no es una tupla de dos enteros
            return False

        # Verificar si la nueva posición está dentro de los límites del tablero
        if not self.is_in_bounds(new_x, new_y):
            return False

        destination_piece = positions[new_x][new_y]
        if destination_piece is not None and destination_piece.color == self.color:
            return False

        return self.diagonal_move(positions, new_position)
