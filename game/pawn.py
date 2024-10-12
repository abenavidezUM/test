# pawn.py

from piece import Piece

class Pawn(Piece):
    """
    Represents a pawn chess piece, inheriting from the Piece base class.
    """

    def __init__(self, color, position):
        """
        Initializes a Pawn instance with a color and position.

        Parameters:
            color (str): The color of the pawn, e.g., "white" or "black".
            position (tuple): The current position of the pawn on the board.
        """
        super().__init__(color, position)

    def __str__(self):
        """
        Returns the Unicode character representing the pawn, depending on its color.

        Returns:
            str: "♙" if the pawn is white, "♟" if the pawn is black.
        """
        return "♙" if self.__color__ == "white" else "♟"

    def check_move(self, positions, new_position):
        """
        Checks if moving to new_position is a valid move for the pawn.

        Parameters:
            positions (list): The current state of the board.
            new_position (tuple): The position to move to.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if self.__color__ == "white":
            return self.is_valid_pawn_move(positions, new_position, -1, 6)
        elif self.__color__ == "black":
            return self.is_valid_pawn_move(positions, new_position, 1, 1)
        return False

    def is_valid_pawn_move(self, positions, new_position, direction, initial_row):
        """
        Checks if the pawn move is valid based on its direction and initial row.

        Parameters:
            positions (list): The current state of the board.
            new_position (tuple): The position to move to.
            direction (int): The direction the pawn moves (-1 for white, 1 for black).
            initial_row (int): The initial row of the pawn (6 for white, 1 for black).

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)

        # Forward move
        if new_y == current_y:
            # First move can be two steps
            if current_x == initial_row:
                if self.move_one_cell(positions, new_position, direction):
                    return True
                elif (new_x == current_x + 2 * direction and
                      positions[current_x + direction][current_y] is None and
                      positions[new_x][new_y] is None):
                    return True
            # Subsequent moves can only be one step
            elif self.move_one_cell(positions, new_position, direction):
                return True
        # Diagonal capture
        elif (new_x == current_x + direction and
              abs(new_y - current_y) == 1 and
              positions[new_x][new_y] is not None and
              positions[new_x][new_y].__color__ != self.__color__):
            return True
        return False

    def move_one_cell(self, positions, new_position, direction):
        """
        Checks if the pawn can move one cell forward.

        Parameters:
            positions (list): The current state of the board.
            new_position (tuple): The position to move to.
            direction (int): The direction the pawn moves (-1 for white, 1 for black).

        Returns:
            bool: True if the pawn can move one cell forward, False otherwise.
        """
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)
        return (new_x == current_x + direction and
                positions[new_x][new_y] is None)
