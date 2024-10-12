from piece import Piece

WHITE = "white"
BLACK = "black"

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
            str: "♙" si el peón es blanco, "♟" si el peón es negro.
        """
        return "♙" if self.__color__ == WHITE else "♟"

    def check_move(self, positions, new_position):
        """
        Checks if moving to new_position is a valid move for the pawn.

        Parameters:
            positions (list): The current state of the board.
            new_position (tuple): The position to move to.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if self.__color__ == WHITE:
            valid = self.is_valid_pawn_move(positions, new_position, -1, 6)
        elif self.__color__ == BLACK:
            valid = self.is_valid_pawn_move(positions, new_position, 1, 1)
        else:
            valid = False
        return valid

    def is_valid_pawn_move(self, positions, new_position, direction, initial_row):
        """
        Checks if the pawn move is valid based on its direction and initial row.

        Parameters:
            positions (list): The current state of the board.
            new_position (tuple): The position to move to.
            direction (int): The direction the pawn moves (-1 for white, 1 for black).
            initial_row (int): The initial row of the pawn (6 for white, 1 for black).

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)
        valid_move = False

        # Movimiento hacia adelante
        if new_y == current_y:
            # Primer movimiento puede ser dos pasos
            if current_x == initial_row:
                if self.move_one_cell(positions, new_position, direction):
                    valid_move = True
                elif (new_x == current_x + 2 * direction and
                      positions[current_x + direction][current_y] is None and
                      positions[new_x][new_y] is None):
                    valid_move = True
            # Movimientos subsecuentes solo pueden ser un paso
            elif self.move_one_cell(positions, new_position, direction):
                valid_move = True
        # Captura diagonal
        elif (new_x == current_x + direction and
              abs(new_y - current_y) == 1 and
              positions[new_x][new_y] is not None and
              positions[new_x][new_y].__color__ != self.__color__):
            valid_move = True

        return valid_move

    def move_one_cell(self, positions, new_position, direction):
        """
        Checks if the pawn can move one cell forward.

        Parameters:
            positions (list): The current state of the board.
            new_position (tuple): The position to move to.
            direction (int): The direction the pawn moves (-1 for white, 1 for black).

        Returns:
            bool: True si el peón puede moverse una celda hacia adelante, False en caso contrario.
        """
        new_x, new_y, current_x, current_y = self.get_coordinates(new_position)
        return (new_x == current_x + direction and
                positions[new_x][new_y] is None)
