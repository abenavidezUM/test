# moves.py

class ChessInvalid(Exception):
    """
    Base class for chess-related exceptions.

    Attributes:
        message (str): Explanation of the error.
    """

    def __init__(self, message="An error occurred in the chess game."):
        """
        Initializes the ChessInvalid exception with an optional message.

        Parameters:
            message (str): An explanation of the error.
        """
        super().__init__(message)


class PieceError(ChessInvalid):
    """
    Exception raised when a piece is not found on the board.
    """
    pass


class PositionInvalid(ChessInvalid):
    """
    Exception raised for invalid positions on the chess board.
    """
    pass


class LocationError(ChessInvalid):
    """
    Exception raised when attempting to move a piece of a different color.
    """
    pass


class MoveError(ChessInvalid):
    """
    Exception raised for invalid moves in the chess game.
    """
    pass


class MovePieceInvalid(MoveError):
    """
    Exception raised for invalid piece movements.
    """
    pass


class KingError(ChessInvalid):
    """
    Exception raised when attempting to capture the opponent's king.
    """
    pass
