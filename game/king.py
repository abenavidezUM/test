from piece import Piece

class King(Piece):
    """
    Represents a king chess piece, inheriting from the Piece base class.
    """

    def __init__(self, color, position):
        """
        Initializes a King instance with a color and position.

        Parameters:
            color (str): The color of the king, e.g., "white" or "black".
            position (tuple): The current position of the king on the board.
        """
        super().__init__(color, position)

    def __str__(self):
        """
        Returns the Unicode character representing the king, depending on its color.

        Returns:
            str: "♔" if the king is white, "♚" if the king is black.
        """
        return "♔" if self.__color__ == "white" else "♚"

    def check_move(self, positions, new_position):
        """
        Checks if moving to new_position is a valid move for the king.

        Parameters:
            positions (list): The current state of the board.
            new_position (tuple): The position to move to.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)

        if abs(new_x - current_x) <= 1 and abs(new_y - current_y) <= 1:
            destination_piece = positions[new_x][new_y]
            if destination_piece is None or destination_piece.__color__ != self.__color__:
                return True
        return False
