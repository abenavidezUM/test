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

        # Verificar si el camino está libre
        return self.is_path_clear(positions, current_x, current_y, step_x, step_y, max(abs(delta_x), abs(delta_y)))

    def is_path_clear(self, positions, current_x, current_y, step_x, step_y, distance):
        """
        Verifica si el camino está libre para el movimiento.

        Parameters:
            positions (list): El estado actual del tablero.
            current_x (int): Coordenada x actual.
            current_y (int): Coordenada y actual.
            step_x (int): Paso en la dirección x.
            step_y (int): Paso en la dirección y.
            distance (int): Distancia total del movimiento.

        Returns:
            bool: True si el camino está libre, False en caso contrario.
        """
        for i in range(1, distance):
            intermediate_x = current_x + i * step_x
            intermediate_y = current_y + i * step_y
            if positions[intermediate_x][intermediate_y] is not None:
                return False
        return True
