# queen.py

from .piece import Piece

class Queen(Piece):
    """
    Represents a queen chess piece, inheriting from the Piece base class.
    """

    def __init__(self, color, position):
        """
        Initializes a Queen instance with a color and position.

        Parameters:
            color (str): The color of the queen, e.g., "white" or "black".
            position (tuple): The current position of the queen on the board.
        """
        super().__init__(color, position)

    def __str__(self):
        """
        Returns the Unicode character representing the queen, depending on its color.

        Returns:
            str: "♕" if the queen is white, "♛" if the queen is black.
        """
        return "♕" if self.__color__ == "white" else "♛"

    def check_move(self, positions, new_position):
        """
        Checks if moving to new_position is a valid move for the queen.

        Parameters:
            positions (list): The current state of the board.
            new_position (tuple): The position to move to.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        destination_piece = positions[new_position[0]][new_position[1]]
        if destination_piece is not None and destination_piece.__color__ == self.__color__:
            return False
        return (
            self.diagonal_move(positions, new_position) or
            self.horizontal_move(positions, new_position) or
            self.vertical_move(positions, new_position)
        )
