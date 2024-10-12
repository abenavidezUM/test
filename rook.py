# rook.py

from piece import Piece

class Rook(Piece):
    """
    Represents a rook chess piece, inheriting from the Piece base class.
    """

    def __init__(self, color, position):
        """
        Initializes a Rook instance with a color and position.

        Parameters:
            color (str): The color of the rook, e.g., "white" or "black".
            position (tuple): The current position of the rook on the board.
        """
        super().__init__(color, position)

    def __str__(self):
        """
        Returns the Unicode character representing the rook, depending on its color.

        Returns:
            str: "♖" if the rook is white, "♜" if the rook is black.
        """
        return "♖" if self.__color__ == "white" else "♜"

    def check_move(self, positions, new_position):
        """
        Checks if moving to new_position is a valid move for the rook.

        Parameters:
            positions (list): The current state of the board.
            new_position (tuple): The position to move to.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if self.horizontal_move(positions, new_position) or self.vertical_move(positions, new_position):
            # Check if destination is within the board boundaries
            if not self.is_in_bounds(*new_position):
                return False
            # Check if the destination is occupied by a friendly piece
            destination_piece = positions[new_position[0]][new_position[1]]
            if destination_piece is None or destination_piece.__color__ != self.__color__:
                return True
        return False
