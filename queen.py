# queen.py

from piece import Piece

WHITE = "white"
BLACK = "black"

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
        if not (0 <= new_x < 8 and 0 <= new_y < 8):
            return False

        # Verificar si la reina intenta moverse a su posición actual
        if (new_x, new_y) == (current_x, current_y):
            return False

        destination_piece = positions[new_x][new_y]
        if destination_piece is not None and destination_piece.color == self.color:
            return False

        return (
            self.diagonal_move(positions, new_position) or
            self.horizontal_move(positions, new_position) or
            self.vertical_move(positions, new_position)
        )

    def diagonal_move(self, positions, new_position):
        """
        Verifica si el movimiento es diagonal y el camino está libre.

        Parameters:
            positions (list): El estado actual del tablero.
            new_position (tuple): La posición a la que se desea mover.

        Returns:
            bool: True si el movimiento es diagonal y el camino está libre, False en caso contrario.
        """
        current_x, current_y = self.position
        new_x, new_y = new_position
        delta_x = new_x - current_x
        delta_y = new_y - current_y

        if abs(delta_x) != abs(delta_y):
            return False

        step_x = 1 if delta_x > 0 else -1
        step_y = 1 if delta_y > 0 else -1

        for i in range(1, abs(delta_x)):
            intermediate_x = current_x + i * step_x
            intermediate_y = current_y + i * step_y
            if positions[intermediate_x][intermediate_y] is not None:
                return False

        return True

    def horizontal_move(self, positions, new_position):
        """
        Verifica si el movimiento es horizontal y el camino está libre.

        Parameters:
            positions (list): El estado actual del tablero.
            new_position (tuple): La posición a la que se desea mover.

        Returns:
            bool: True si el movimiento es horizontal y el camino está libre, False en caso contrario.
        """
        current_x, current_y = self.position
        new_x, new_y = new_position

        if current_x != new_x:
            return False

        step = 1 if new_y > current_y else -1

        for y in range(current_y + step, new_y, step):
            if positions[current_x][y] is not None:
                return False

        return True

    def vertical_move(self, positions, new_position):
        """
        Verifica si el movimiento es vertical y el camino está libre.

        Parameters:
            positions (list): El estado actual del tablero.
            new_position (tuple): La posición a la que se desea mover.

        Returns:
            bool: True si el movimiento es vertical y el camino está libre, False en caso contrario.
        """
        current_x, current_y = self.position
        new_x, new_y = new_position

        if current_y != new_y:
            return False

        step = 1 if new_x > current_x else -1

        for x in range(current_x + step, new_x, step):
            if positions[x][current_y] is not None:
                return False

        return True
