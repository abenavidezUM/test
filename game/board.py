from piece import Piece
from bishop import Bishop
from king import King
from knight import Knight
from pawn import Pawn
from queen import Queen
from rook import Rook
from moves import PieceError, MoveError, MovePieceInvalid, KingError

class Board:
    """
    Represents the chess board and manages the state of the game.
    """

    def __init__(self, for_test=False):
        """
        Initializes the chess board with pieces set up in their starting positions,
        unless 'for_test' is True, in which case the board is initialized empty.

        Parameters:
            for_test (bool): If True, the board will be empty for testing purposes.
        """
        self.positions = [[None for _ in range(8)] for _ in range(8)]

        if not for_test:
            self.setup_pieces()

    def setup_pieces(self):
        """
        Sets up all the chess pieces on the board in their initial positions.
        """
        # Black pieces
        self.positions[0][0] = Rook("black", (0, 0))
        self.positions[0][1] = Knight("black", (0, 1))
        self.positions[0][2] = Bishop("black", (0, 2))
        self.positions[0][3] = Queen("black", (0, 3))
        self.positions[0][4] = King("black", (0, 4))
        self.positions[0][5] = Bishop("black", (0, 5))
        self.positions[0][6] = Knight("black", (0, 6))
        self.positions[0][7] = Rook("black", (0, 7))

        for i in range(8):
            self.positions[1][i] = Pawn("black", (1, i))
            self.positions[6][i] = Pawn("white", (6, i))

        # White pieces
        self.positions[7][0] = Rook("white", (7, 0))
        self.positions[7][1] = Knight("white", (7, 1))
        self.positions[7][2] = Bishop("white", (7, 2))
        self.positions[7][3] = Queen("white", (7, 3))
        self.positions[7][4] = King("white", (7, 4))
        self.positions[7][5] = Bishop("white", (7, 5))
        self.positions[7][6] = Knight("white", (7, 6))
        self.positions[7][7] = Rook("white", (7, 7))

    def get_piece(self, row, col):
        """
        Retrieves the piece at a specific position on the board.

        Parameters:
            row (int): The row index (0-7) on the board.
            col (int): The column index (0-7) on the board.

        Returns:
            Piece or None: The piece at the specified position, or None if the position is empty.
        """
        return self.positions[row][col]

    def set_piece_on_board(self, row, col, piece):
        """
        Places a piece at a specific position on the board.

        Parameters:
            row (int): The row index (0-7) where the piece will be placed.
            col (int): The column index (0-7) where the piece will be placed.
            piece (Piece): The chess piece to place on the board.
        """
        self.positions[row][col] = piece

    def find_piece(self, piece):
        """
        Finds the current position of a given piece on the board.

        Parameters:
            piece (Piece): The chess piece to locate.

        Returns:
            tuple or None: A tuple (row, col) indicating the piece's position, or None if not found.
        """
        for row in range(8):
            for col in range(8):
                if self.positions[row][col] == piece:
                    return (row, col)
        return None

    def move(self, piece, destination):
        """
        Moves a piece from its current position to a new position if the move is valid.

        Parameters:
            piece (Piece): The piece to move.
            destination (tuple): A tuple (row, col) representing the destination position.

        Returns:
            bool: True if the move is successful.

        Raises:
            PieceError: If the piece is not found on the board.
            MovePieceInvalid: If the move is invalid for the piece.
            MoveError: If the destination is occupied by a friendly piece.
            KingError: If attempting to capture the opponent's king.
        """
        self.validate_move(piece, destination)
        self.execute_move(piece, destination)
        return True

    def validate_move(self, piece, destination):
        """
        Validates whether a move is legal according to the game rules.

        Parameters:
            piece (Piece): The piece attempting to move.
            destination (tuple): A tuple (row, col) representing the destination position.

        Raises:
            PieceError: If the piece is not on the board.
            MovePieceInvalid: If the move is invalid for the piece type.
            MoveError: If the destination is occupied by a friendly piece.
            KingError: If attempting to capture the opponent's king.
        """
        current_position = self.find_piece(piece)
        if current_position is None:
            raise PieceError("Piece not found on the board.")

        if not piece.check_move(self.positions, destination):
            raise MovePieceInvalid("Invalid piece movement.")

        dest_piece = self.get_piece(*destination)
        if dest_piece is not None:
            if dest_piece.color == piece.color:
                raise MoveError("You cannot move to a square occupied by your own piece.")
            if isinstance(dest_piece, King):
                raise KingError("You cannot capture the opponent's king.")

    def execute_move(self, piece, destination):
        """
        Executes a validated move on the board.

        Parameters:
            piece (Piece): The piece to move.
            destination (tuple): The destination position as a tuple (row, col).
        """
        current_row, current_col = self.find_piece(piece)
        dest_row, dest_col = destination
        captured_piece = self.get_piece(dest_row, dest_col)

        self.set_piece_on_board(dest_row, dest_col, piece)
        self.set_piece_on_board(current_row, current_col, None)
        piece.position = (dest_row, dest_col)

        if captured_piece is not None:
            captured_piece.position = None  # Remove the captured piece from the board

    def print_board(self):
        """
        Displays the current state of the chess board.
        """
        print("  A B C D E F G H")
        print("  ----------------")
        
        for row in range(7, -1, -1):
            line = f'{row+1}|'
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece is None:
                    line += '. '  # Empty space
                else:
                    line += f'{piece} '
            print(line + f'|{row+1}')
        
        print("  ----------------")
        print("  A B C D E F G H")

    def pieces_on_board(self):
        """
        Counts the number of white and black pieces remaining on the board.

        Returns:
            tuple: A tuple (white_pieces, black_pieces) representing the count of pieces for each color.
        """
        white_pieces = 0
        black_pieces = 0
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece is None:
                    continue
                else:
                    if piece.color == "white":
                        white_pieces += 1
                    else:
                        black_pieces += 1
        return (white_pieces, black_pieces)

    def color_pieces(self, x, y):
        """
        Gets the color of the piece at the specified position.

        Parameters:
            x (int): The row index (0-7) on the board.
            y (int): The column index (0-7) on the board.

        Returns:
            str: The color of the piece ("white" or "black").

        Raises:
            PieceError: If there is no piece at the specified position.
        """
        piece = self.get_piece(x, y)
        if piece is None:
            raise PieceError("Piece not found on the board.")
        else:
            return piece.color

    def clean_board(self):
        """
        Clears the board by removing all pieces.
        """
        self.positions = [[None for _ in range(8)] for _ in range(8)]
