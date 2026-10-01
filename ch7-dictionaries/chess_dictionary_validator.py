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
        if chess_square[0] in valid_chessboard_columns and chess_square[1] in valid_chessboard_rows:

            piece_color = chess_piece[0]
            piece_type = chess_piece[1:]

            if piece_color in valid_chess_colors and piece_type in valid_chess_pieces:

                if piece_color == "w":
                    white_total_piece_count += 1
                    if piece_type == "pawn":
                        white_pawn_count += 1
                    if piece_type == "king":
                        white_king_count += 1
                elif piece_color == "b":
                    black_total_piece_count += 1
                    if piece_type == "pawn":
                        black_pawn_count += 1
                    if piece_type == "king":
                        black_king_count += 1

            else:
                return False

        else:
            return False  #

    # check piece counts
    if white_pawn_count > 8:
        return False
    if black_pawn_count > 8:
        return False
    if white_king_count != 1:
        return False
    if black_king_count != 1:
        return False
    if white_total_piece_count > 16:
        return False
    if black_total_piece_count > 16:
        return False

    return True
