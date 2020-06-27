STATUS_VALUE = 0
FLAGGED = 4

game_board = [[1, 2], [2, 3], [3, 4], [4, 5]]


def get_flagged_cells():
    flagged_cells = list()

    for cell in game_board:
        if cell[STATUS_VALUE] == FLAGGED:
            flagged_cells.append(cell)
    return flagged_cells


if __name__ == "__main__":
    print(get_flagged_cells())
