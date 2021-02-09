"""
The playing field of the logic puzzle has a square shape of 9 × 9 cells.
The playing field contains cells of different colors that are used in the
game and white areas that are not used for the game.
"""

def validate_board(input_list: list) -> bool:
    if len(input_list[0]) != len(input_list) != 9:
        raise ValueError("Puzzle dimension should be 9x9")

    def validate_row(board: list) -> bool:
        for row in board:
            current_row = [int(x) for x in row if x.isdigit()]
            if len(set(current_row)) != len(current_row):
                return False
        return True

    def validate_columns(board: list) -> bool:

        for i in range(len(board)):
            block = []
            for j in range(len(board[i])):
                block.append(board[j][i])

            board.append("".join(x for x in block))

        columns = board[int(len(board) / 2):]

        return validate_row(columns)

    def validate_blocks(board: list) -> bool:
        colour_board = []
        start_y, start_x = 4, 0

        for _ in range(5):
            colour_block = []
            y, x = start_y, start_x
            for _ in range(4):
                colour_block.append(board[y][x])
                y += 1
            for _ in range(5):
                colour_block.append(board[y][x])
                x += 1

            colour_board.append(colour_block)
            start_y -= 1
            start_x += 1

        return validate_row(colour_board)

    return validate_row(input_list) & validate_columns(input_list) & validate_blocks(input_list)


if __name__ == '__main__':
    g_board = [
        "**** ****",
        "***1 ****",
        "**  3****",
        "* 4 1****",
        "     9 5 ",
        " 6  83  *",
        "3   7  **",
        "  8  2***",
        "  2  ****"
    ]

    print(validate_board(g_board))

