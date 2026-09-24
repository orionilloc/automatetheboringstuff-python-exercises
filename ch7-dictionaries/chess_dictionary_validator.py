# In this chapter, we used the dictionary value {'h1': 'bK', 'c6': 'wQ', 'g2': 'bB', 'h5': 'bQ', 'e3': 'wK'} to represent a chessboard. Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on whether the board is valid.

# A valid board will have exactly one black king and exactly one white king. Each player can have at most 16 pieces, of which only eight can be pawns, and all pieces must be on a valid square from '1a' to '8h'. That is, a piece can’t be on square '9z'. The piece names should begin with either a 'w' or a 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. This function should detect when a bug has resulted in an improper chessboard. (This isn’t an exhaustive list of requirements, but it is close enough for this exercise.)


def isValidChessBoard(sample_chessboard):
    # define white player's chessboard counts
    white_total_piece_count = 0
    white_king_count = 0
    white_pawn_count = 0
    # define black player's chessboard counts
    black_total_piece_count = 0
    black_king_count = 0
    black_pawn_count = 0
    # define valid chess piece and setup parameter per exercise requirements
    valid_chessboard_columns = "abcdefgh"
    valid_chessboard_rows = "12345678"
    valid_chess_pieces = ("pawn", "knight", "bishop", "rook", "queen", "king")
    valid_chess_colors = ("b", "w")

    # need to loop through and add a counter based on any matched value
    for chess_square, chess_piece in sample_chessboard.items():
        if chess_square[0] in valid_chessboard_columns and chess_square[1] in valid_chessboard_rows



# isValidChessBoard(board) -> True/False

# input is a dict and no other paramters

#exactly one 'bK' and exactly one 'wK' total
#per color: max 16 pieces, of which max 8 pawns
#every square key is valid: 'a'-'h' + '1'-'8', two chars
#every piece value is valid format: 'w'/'b' + piece-type letter/name
#one loop over board.items() can tally counts and check square/piece format as it goes
#return True only if every rule above holds, otherwise False

