def isValidChessBoard(board: dict) -> bool:
    if "bking" not in board.values() or "wking" not in board.values():
        return False
    # count players pawns
    black_amount= 0
    white_amount = 0
    white_pawns_count = 0
    black_pawns_count = 0
    for count in board.values():
        if count[0] == 'b':
            black_amount += 1
        elif count[0] == 'w':
            white_amount += 1
        elif count == "wpawn":
            white_pawns_count += 1
        elif count == "bpawn":
            black_pawns_count += 1

    if black_amount > 16 or white_amount > 16 or black_pawns_count > 8 or white_pawns_count > 8:
        return False

    for space in board.keys():
        if int(space[0]) > 8 or int(space[0]) < 1:
            return False
    return True


# print(isValidChessBoard({"1h": "bking", "6c": "wqueen", "2g": "bbishop", "5h": "bqueen", "3e": "wking"}))
# print(isValidChessBoard({"1a": "bpawn", "2a": "wking"}))
# print(isValidChessBoard({"1a": "wking", "2a": "wking", "3c": "bbishop"}))
# print(isValidChessBoard({"1a": "bking", "9z": "wking"}))
