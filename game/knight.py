# knight.py

from piece import Piece

class Knight(Piece):
    """
    Represents a knight chess piece, inheriting from the Piece base class.
    """

    def __init__(self, color, position):
        """
        Initializes a Knight instance with a color and position.

        Parameters:
            color (str): The color of the knight, e.g., "white" or "black".
            position (tuple): The current position of the knight on the board.
        """
        super().__init__(color, position)

    def __str__(self):
        """
        Returns the Unicode character representing the knight, depending on its color.

        Returns:
            str: "♘" if the knight is white, "♞" if the knight is black.
        """
        return "♘" if self.__color__ == "white" else "♞"

    def check_move(self, positions, new_position):
        """
        Checks if moving to new_position is a valid move for the knight.

        Parameters:
            positions (list): The current state of the board.
            new_position (tuple): The position to move to.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)

        possible_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        for dx, dy in possible_moves:
            if (new_x, new_y) == (current_x + dx, current_y + dy):
                if self.is_in_bounds(new_x, new_y):
                    destination_piece = positions[new_x][new_y]
                    if destination_piece is None or destination_piece.__color__ != self.__color__:
                        return True
        return False
