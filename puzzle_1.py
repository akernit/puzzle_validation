"""
The playing field of the logic puzzle has a square shape of 9 × 9 cells.
The playing field contains cells of different colors that are used in the
game and white areas that are not used for the game.
The address of the repository in the GitHub repository:
https://github.com/akernit/puzzle_validation
"""

def validate_board(input_list: list) -> bool:
    """
    The function sets whether the logic puzzle playing field is ready to start
    the game.     The cells of the playing field before the start of the game
    must be filled according
    to the following rules:
    1. The colored cells of each line must contain the numbers 1 to 9 without
    repetition.
    2. The colored cells of each column must contain numbers from 1 to 9 without
    repetition.
    3. Each block of cells of the same color must contain numbers from 1 to 9
    without repetition.
    The validate_board (board) function must return a Boolean value.
    >>> validate_board(board)
    False
    """
    if len(input_list[0]) != len(input_list) != 9:
        raise ValueError("Puzzle dimension should be 9x9")

    def validate_row(board: list) -> bool:
        """
        This function validate the correctness of the rows.
        """
        for row in board:
            current_row = [int(x) for x in row if x.isdigit()]
            if len(set(current_row)) != len(current_row):
                return False
        return True

    def validate_columns(board: list) -> bool:
        """
        This function validate the correctness of the columns.
        """
        for i in range(len(board)):
            block = []
            for j in range(len(board[i])):
                block.append(board[j][i])

            board.append("".join(x for x in block))

        columns = board[int(len(board) / 2):]

        return validate_row(columns)

    def validate_blocks(board: list) -> bool:
        """
        This function validate the correctness of the blocks.
        """
        colour_board = []
        start_y, start_x = 4, 0

        for _ in range(5):
            colour_block = []
            coord_y, coord_x = start_y, start_x
            for _ in range(4):
                colour_block.append(board[coord_y][coord_x])
                coord_y += 1
            for _ in range(5):
                colour_block.append(board[coord_y][coord_x])
                coord_x += 1

            colour_board.append(colour_block)
            start_y -= 1
            start_x += 1

        return validate_row(colour_board)

    return validate_row(input_list) & validate_columns(input_list) & \
    validate_blocks(input_list)
