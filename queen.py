# queen.py

from piece import Piece, WHITE, BLACK

class Queen(Piece):
    """
    Represents a queen chess piece, inheriting from the Piece base class.
    """

    def __init__(self, color, position):
        """
        Initializes a Queen instance with a color and position.

        Parameters:
            color (str): The color of the queen, e.g., "white" or "black".
            position (tuple): The current position of the queen on the board as (row, column).
        """
        super().__init__(color, position)

    def __str__(self):
        """
        Returns the Unicode character representing the queen, depending on its color.

        Returns:
            str: "♕" if the queen is white, "♛" if the queen is black.
        """
        return "♕" if self.color == WHITE else "♛"

    def check_move(self, positions, new_position):
        """
        Checks if moving to new_position is a valid move for the queen.

        Parameters:
            positions (list): The current state of the board.
            new_position (tuple): The position to move to.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        current_x, current_y = self.position
        new_x, new_y = new_position

        # Verificar si la nueva posición está dentro de los límites del tablero
        if not self.is_in_bounds(new_x, new_y):
            return False

        # Verificar si la reina intenta moverse a su posición actual
        if (new_x, new_y) == (current_x, current_y):
            return False

        destination_piece = positions[new_x][new_y]
        if destination_piece is not None and destination_piece.color == self.color:
            return False

        # Determinar la dirección del movimiento
        delta_x = new_x - current_x
        delta_y = new_y - current_y

        # Normalizar los pasos para dirección
        step_x = (delta_x > 0) - (delta_x < 0)
        step_y = (delta_y > 0) - (delta_y < 0)

        # Verificar si el movimiento es válido (horizontal, vertical o diagonal)
        if step_x != 0 and step_y != 0:
            # Movimiento diagonal
            if abs(delta_x) != abs(delta_y):
                return False
        elif step_x == 0 and step_y == 0:
            # No se mueve
            return False
        # Si solo uno de step_x o step_y es diferente de cero, es horizontal o vertical

        # Verificar si el camino está libre utilizando el método de la clase base
        return self.is_path_clear(positions, self.position, new_position)
