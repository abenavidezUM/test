from abc import ABC, abstractmethod

WHITE = "white"
BLACK = "black"

class Piece(ABC):
    """
    Base class for all chess pieces.
    """

    def __init__(self, color, position):
        """
        Initializes a Piece with a color and position.

        Parameters:
            color (str): The color of the piece, e.g., "white" or "black".
            position (tuple): The current position of the piece on the board as (row, column).
        """
        self.__color__ = color
        self.__position__ = position

    @property
    def color(self):
        """
        Gets the color of the piece.

        Returns:
            str: The color of the piece.
        """
        return self.__color__

    @property
    def position(self):
        """
        Gets the current position of the piece.

        Returns:
            tuple: The current position as (row, column).
        """
        return self.__position__

    @position.setter
    def position(self, new_position):
        """
        Sets the position of the piece.

        Parameters:
            new_position (tuple): The new position as (row, column).
        """
        self.__position__ = new_position

    def __str__(self):
        """
        Returns a string representation of the piece.

        Returns:
            str: A placeholder character for an unspecified piece.
        """
        return "?"

    @abstractmethod
    def check_move(self, positions, new_position):
        """
        Abstract method to check if a move is valid for the piece.
        Must be implemented by subclasses.

        Parameters:
            positions (list): The current state of the board.
            new_position (tuple): The position to move to.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        pass

    def get_coordinates(self, new_position):
        """
        Returns the coordinates for the current and new positions.

        Parameters:
            new_position (tuple): The new position as (row, column).

        Returns:
            tuple: A tuple containing new_x, new_y, current_x, current_y.
        """
        new_x, new_y = new_position
        current_x, current_y = self.__position__
        return new_x, new_y, current_x, current_y

    def is_path_clear(self, positions, current_position, new_position):
        """
        Verifica si el camino entre la posición actual y la nueva posición está libre.

        Parámetros:
            positions (list): El estado actual del tablero.
            current_position (tuple): Coordenada actual como (x, y).
            new_position (tuple): Nueva coordenada como (x, y).

        Returns:
            bool: True si el camino está libre, False de lo contrario.
        """
        current_x, current_y = current_position
        new_x, new_y = new_position

        # Calcular la dirección del movimiento
        step_x = 0
        step_y = 0

        if new_x > current_x:
            step_x = 1
        elif new_x < current_x:
            step_x = -1

        if new_y > current_y:
            step_y = 1
        elif new_y < current_y:
            step_y = -1

        x, y = current_x + step_x, current_y + step_y

        while (x, y) != (new_x, new_y):
            if not self.is_in_bounds(x, y):
                return False
            if positions[x][y] is not None:
                return False
            x += step_x
            y += step_y

        return True

    def can_move(self, positions, new_position, movement_type):
        """
        Verifica si un movimiento es válido basado en el tipo de movimiento y si el camino está libre.

        Parámetros:
            positions (list): El estado actual del tablero.
            new_position (tuple): La posición a la que se quiere mover.
            movement_type (str): Tipo de movimiento ('horizontal', 'vertical', 'diagonal').

        Returns:
            bool: True si el movimiento es válido y el camino está libre, False de lo contrario.
        """
        current_position = self.position
        new_x, new_y = new_position
        current_x, current_y = current_position
        x_diff, y_diff = new_x - current_x, new_y - current_y

        is_valid = True  # Variable para almacenar el estado de validez

        if movement_type == 'diagonal':
            if abs(x_diff) != abs(y_diff):
                is_valid = False
        elif movement_type == 'horizontal':
            if new_x != current_x:
                is_valid = False
        elif movement_type == 'vertical':
            if new_y != current_y:
                is_valid = False
        else:
            # Tipo de movimiento no reconocido
            is_valid = False

        if is_valid:
            is_valid = self.is_path_clear(positions, current_position, new_position)

        return is_valid

    def diagonal_move(self, positions, new_position):
        """
        Verifica si el movimiento diagonal es válido y el camino está libre.

        Parámetros:
            positions (list): El estado actual del tablero.
            new_position (tuple): La posición a la que se quiere mover.

        Returns:
            bool: True si el movimiento es válido y el camino está libre, False de lo contrario.
        """
        return self.can_move(positions, new_position, 'diagonal')

    def horizontal_move(self, positions, new_position):
        """
        Verifica si el movimiento horizontal es válido y el camino está libre.

        Parámetros:
            positions (list): El estado actual del tablero.
            new_position (tuple): La posición a la que se quiere mover.

        Returns:
            bool: True si el movimiento es válido y el camino está libre, False de lo contrario.
        """
        return self.can_move(positions, new_position, 'horizontal')

    def vertical_move(self, positions, new_position):
        """
        Verifica si el movimiento vertical es válido y el camino está libre.

        Parámetros:
            positions (list): El estado actual del tablero.
            new_position (tuple): La posición a la que se quiere mover.

        Returns:
            bool: True si el movimiento es válido y el camino está libre, False de lo contrario.
        """
        return self.can_move(positions, new_position, 'vertical')

    def is_in_bounds(self, x, y):
        """
        Checks if the given coordinates are within the board boundaries.

        Parameters:
            x (int): The row index.
            y (int): The column index.

        Returns:
            bool: True if within boundaries, False otherwise.
        """
        return 0 <= x < 8 and 0 <= y < 8
